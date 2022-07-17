# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # DSLab Homework4 - More trains (PART I & II)
#
# ## Hand-in Instructions:
# - __Due: 11.05.2021 23:59:59 CET__
# - your project must be private
# - git push your final verion to the master branch of your group's Renku repository before the due date
# - check if Dockerfile, environment.yml and requirements.txt are properly written
# - add necessary comments and discussion to make your codes readable
#
# ## NS Streams
# For this homework, you will be working with the real-time streams of the NS, the train company of the Netherlands. You can see an example webpage that uses the same streams to display the train information on a map: https://spoorkaart.mwnn.nl/ . 
#
# To help you and avoid having too many connections to the NS streaming servers, we have setup a service that collects the streams and pushes them to our Kafka instance. The related topics are: 
#
# `ndovloketnl-arrivals`: For each arrival of a train in a station, describe the previous and next station, time of arrival (planned and actual), track number,...
#
# `ndovloketnl-departures`: For each departure of a train from a station, describe the previous and next station, time of departure (planned and actual), track number,...
#
# `ndovloketnl-gps`: For each train, describe the current location, speed, bearing.
#
# The events are serialized in JSON (actually converted from XML), with properties in their original language. Google translate could help you understand all of them, but we will provide you with some useful mappings.

# %% [markdown]
# ---

# %% [markdown]
# **Part I & II are in ipython kernel**

# %%
ipython = get_ipython()
print('Current kernel: {}'.format(ipython.kernel.kernel_info['implementation']))

# %% [markdown]
# ---

# %% [markdown]
# ## Create a Kafka client

# %%
import os
from pykafka import KafkaClient
from pykafka.common import OffsetType


username = os.environ['RENKU_USERNAME']

ZOOKEEPER_QUORUM = 'iccluster029.iccluster.epfl.ch:2181,' \
                   'iccluster044.iccluster.epfl.ch:2181,' \
                   'iccluster052.iccluster.epfl.ch:2181'

client = KafkaClient(zookeeper_hosts=ZOOKEEPER_QUORUM)

# %% [markdown]
# ---

# %% [markdown]
# ## PART I - Live Plot (30 points)
#
# The goal of this part is to obtain an interactive plot using the train positions from the GPS stream.

# %% [markdown]
# First, let's write a function to decode the messages from the `ndovloketnl-gps` topic.

# %%
import json
from pykafka.common import OffsetType

example_gps = client.topics[b'ndovloketnl-gps'].get_simple_consumer(
    auto_offset_reset=OffsetType.EARLIEST,
    reset_offset_on_start=True
).consume()

# String truncated for display
print(json.dumps(json.loads(example_gps.value), indent=2)[:2000])

# %% [markdown]
# We can see that the message has the following structure:
#
# ```
# {
#   'tns3:ArrayOfTreinLocation': {
#     'tns3:TreinLocation': [
#       <train_info_1>,
#       <train_info_2>,
#       ...
#     ]
#   }
# }
# ```
#
# Each `<train_info_x>` message contains:
# - `tns3:TreinNummer`: the train number. This number is used in passenger information displays.
# - `tns3:TreinMaterieelDelen`:
#     - `tns3:MaterieelDeelNummer`: the train car number. It identifies the physical train car.
#     - `tns3:Materieelvolgnummer`: the car position. 1 is the car in front of the train, 2 the next one, etc.
#     - `tns3:GpsDatumTijd`: the datetime given by the GPS.
#     - `tns3:Latitude`, `tns3:Longitude`, `tns3:Elevation`: 3D coordinates given by the GPS.
#     - `tns3:Snelheid`: speed, most likely given by the GPS.
#     - `tns3:Richting`: heading, most likely given by the GPS.
#     - `tns3:AantalSatelieten`: number of GPS satellites in view.
#     - ...
#
# We also notice that when a train is composed of multiple cars, the position is given in an array, with the position of all individual cars.

# %% [markdown]
# ### a) Extract data - 9/30
#
# Write a function `extract_gps_data` which takes the message as input and extracts the train number, train car and GPS data from the source messages. Using this function, you should be able to obtain the example table, or something similar:
#
# |            timestamp | train_number | car_number | car_position |       longitude |        latitude | elevation | heading | speed |
# |---------------------:|-------------:|-----------:|-------------:|----------------:|----------------:|----------:|--------:|------:|
# | 2021-04-26T11:18:38Z | 4651         | 2414       | 1            | 4.4337813744686 | 52.126090732796 | 0.0       | 0.0     | 0     |
# | 2021-04-26T11:18:29Z | 646          | 4029       | 1            | 6.13383283333   | 52.788337       | 0.0       | 104.83  | 103.0 |
# | 2021-04-26T11:18:29Z | 5747         | 2628       | 1            | 4.8238861121011 | 52.338504198172 | 0.0       | 90.5    | 126.0 |
# | 2021-04-26T11:18:19Z | 5747         | 2430       | 2            | 4.8168466316014 | 52.338447739203 | 0.0       | 85.8    | 118.8 |
#
#
# __Note:__
# - The messages can be occasionally empty, for example, `tns3:ArrayOfTreinLocation` or `tns3:TreinLocation` can be empty.
# - Not every message shares exactly the same structure, for example, `tns3:TreinMaterieelDelen` may be a list but not always
# - You may find Python disctionary [get(key, default)](https://docs.python.org/3.7/library/stdtypes.html#dict.get) method helpful.

# %%
from datetime import datetime


def extract_gps_data(msg):
    
    train_list = msg.get('tns3:ArrayOfTreinLocation').get('tns3:TreinLocation')
    new_train_list = []
    for train in train_list:
        train_equipment = train.get('tns3:TreinMaterieelDelen')
        if not isinstance(train_equipment, list):
            train_equipment = [train_equipment]
            
        for wagon in train_equipment:
            train_dict = {
                'train_number': int(train.get('tns3:TreinNummer')),
                'timestamp': pd.to_datetime(wagon.get('tns3:GpsDatumTijd')), # Sometimes the timestamps include decimal minutes, and sometimes they don't
                'car_number': int(wagon.get('tns3:MaterieelDeelNummer')),
                'car_position': int(wagon.get('tns3:Materieelvolgnummer')), 
                'longitude': float(wagon.get('tns3:Longitude')),
                'latitude': float(wagon.get('tns3:Latitude')),
                'elevation': float(wagon.get('tns3:Elevation')),
                'heading': float(wagon.get('tns3:Richting')),
                'speed': float(wagon.get('tns3:Snelheid'))
            }
            
        new_train_list.append(train_dict)
    return new_train_list


# %%
# Example results from "extract_gps_data"
import numpy as np
import pandas as pd

df_example = pd.DataFrame(
    data = extract_gps_data(json.loads(example_gps.value)),
    columns = ['timestamp', 'train_number', 'car_number', 'car_position', 
               'longitude', 'latitude', 'elevation', 'heading', 'speed']
)
df_example.head(2)

# %% [markdown]
# ### b) Trains on the map - 9/30
#
# Each row of `df_example` represents one car of one train in the real world. 
#
# Use `plotly` to properly visualize trains in the `df_example` on a map. Set `title` as the median timestamp and `hovername` as the train number.
#
# **Note:**
# - We expect the train positions to fall on rail tracks on the map. Showing each train as a circle is good enough. Check [Scatter Plots on Mapbox](https://plotly.com/python/scattermapbox/).
# - One train may have many cars. You do not need to show every car on the map, please keep only cars with `car_position` equal to '1'.
# - Set an interactive label with the train number (we do not expect train type, as this needs to be recovered from other sources).

# %%
import plotly.express as px

 # %%
 df_example['timestamp'].median().strftime('%m/%d/%Y, %H:%M:%S')

# %%
import requests
res = requests.get(
    "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/the-netherlands.geojson"
)

fig = px.scatter_mapbox(df_example[df_example['car_position'] == 1],
                        lat="latitude",
                        lon="longitude",
                        title="Median timestamp: " + df_example[df_example['car_position'] == 1]['timestamp'].median().strftime('%d/%m/%Y, %H:%M:%S'),
                        hover_name='train_number',
                        hover_data={
                            'timestamp': False, 
                            'train_number': False, 
                            'car_number': False, 
                            'car_position': False, 
                            'longitude': False, 
                            'latitude': False, 
                            'elevation': False, 
                            'heading': False,
                            'speed': False
                            
                        }
                       )


fig.update_layout(
    mapbox={
                    "style": "carto-positron",
                    "zoom": 5.2,
                    "layers": [
                        {
                            "source": res.json(),
                            "type": "line",
                            "color": "green",
                            "line": {"width": 1},
                        }
                    ]
                }
            )

fig.show()

static_fig = fig

# %% [markdown]
# ### c) Trains on the move - 12/30
#
# From the static map above, use `plotly` to make a live plot of the train positions consuming the `ndovloketnl-gps` stream.
#
# Upon receving a new message, you need to:
#
# - Update train locations
# - Update hover information
# - Update title
#
# You can compare your plot to one of the live services: https://spoorkaart.mwnn.nl/, http://treinenradar.nl/

# %% [markdown]
# Create a simple consumer for `ndovloketnl-gps`, which consumes the earliest/latest information from the stream.

# %%
consumer = client.topics[b'ndovloketnl-gps'].get_simple_consumer(
    auto_offset_reset=OffsetType.EARLIEST, # OffsetType.LATEST
    reset_offset_on_start=True
)

# %%
import plotly.graph_objects as go

stream_fig = go.FigureWidget(static_fig)
stream_fig


# %% [markdown]
# Make the plot alive. You can refer to the exercise for an idea.

# %%
import time
try:
    for message in consumer:
        stream_df = pd.DataFrame(
        data = extract_gps_data(json.loads(message.value)),
        columns = ['timestamp', 'train_number', 'car_number', 'car_position', 
               'longitude', 'latitude', 'elevation', 'heading', 'speed']
        )
        with stream_fig.batch_update():
            stream_fig.layout.title.text = "Median timestamp: " + stream_df[stream_df['car_position'] == 1]['timestamp'].median().strftime('%d/%m/%Y, %H:%M:%S')
            stream_fig.data[0].lat = stream_df.latitude
            stream_fig.data[0].lon = stream_df.longitude
            stream_fig.data[0].hovertext = stream_df.train_number
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Plot interrupted.")


# %% [markdown]
# ---

# %% [markdown]
# ## PART II - Locate Message (20 points)
#
# After you finish this part, you will able to locate the message given a specific timestamp.
#
# You can find below a helper function to read a message at a specific offset from a Kafka topic.

# %%
def fetch_message_at(topic, offset):
    if isinstance(topic, str):
        topic = topic.encode('utf-8')
    t = client.topics[topic]
    consumer = t.get_simple_consumer()
    p = list(consumer.partitions.values())[0]
    consumer.reset_offsets([(p, OffsetType.EARLIEST if offset == 0 else offset - 1)])
    return consumer.consume()


# %%
msg = fetch_message_at(b'ndovloketnl-gps', 34567)

# %%
offsets = set()
for i in range(128232-100, 128232+5*83, 83):
    msg = fetch_message_at(b'ndovloketnl-gps', i)
    offsets.add(msg.offset)
offsets

# %%
msg.offset

# %%
# msg.value

# %% [markdown]
# ### a) Median timestamp - 10/20
#
# Write a function to extract the median timestamp from a message of the `ndovloketnl-gps` topic. You can reuse the `extract_gps_data` function from part I.

# %%
example_gps = client.topics[b'ndovloketnl-gps'].get_simple_consumer(
    auto_offset_reset=OffsetType.EARLIEST,
    reset_offset_on_start=True
).consume()

# %%
import pandas as pd
import numpy as np
def extract_gps_time_approx(msg):
    gps_data = extract_gps_data(msg)
    
    median = pd.DataFrame(
                        data = gps_data,
                        columns = ['timestamp']
                        ).timestamp.median().replace(tzinfo=None) 
    return np.datetime64(median)



# %%
assert extract_gps_time_approx(json.loads(example_gps.value)) == np.datetime64('2022-04-26T10:41:35.000000000')


# %% [markdown]
# ### b) Binary search - 10/20
#
# Using `fetch_message_at` and `extract_gps_time_approx`, write a function named `search_gps` to find the "first" offset for a given timestamp in the `ndovloketnl-gps` topic. You function should use [Binary Search Algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm).
#
# More preciseley, if we note `offset = search_gps(ts)` where `ts` is a timestamp, then we have:
# ```
# ts <= extract_gps_time_approx(fetch_message_at('ndovloketnl-gps', offset))
#
# extract_gps_time_approx(fetch_message_at('ndovloketnl-gps', offset - 1)) < ts
# ```

# %%
def search_gps(findTime):
    # TODO
    topic = b'ndovloketnl-gps'
    
    p = list(consumer.partitions.values())[0]
    
    
    left = client.topics[topic].earliest_available_offsets()[p.id].offset[0]
    right = client.topics[topic].latest_available_offsets()[p.id].offset[0]

  
    while left < right:
        m = int(np.floor((left + right) / 2))
        
        m_time = extract_gps_time_approx(json.loads(fetch_message_at(topic, m).value))
        if m_time > findTime:
            right = m
        else:
            left = m + 1
    return right 


# %%
def test_search_gps(tsStr):
    ts = np.datetime64(tsStr)
    offset = search_gps(ts)
    ts_after_offset = extract_gps_time_approx(json.loads(fetch_message_at(b'ndovloketnl-gps', offset).value))
    ts_before_offset = extract_gps_time_approx(json.loads(fetch_message_at(b'ndovloketnl-gps', offset - 1).value))
    assert ts_before_offset < ts <= ts_after_offset



# %%
test_search_gps('2022-04-29 06:01:45')

# %%
test_search_gps('2022-04-28 08:00:00')

# %%
test_search_gps('2022-04-29 11:00:00')

# %%
