# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # DSLab Homework 1 - Data Science with CO2
#
# ## Hand-in Instructions
#
# - __Due: 22.03.2022 23h59 CET__
# - `git push` your final verion to the master branch of your group's Renku repository before the due
# - check if `Dockerfile`, `environment.yml` and `requirements.txt` are properly written
# - add necessary comments and discussion to make your codes readable

# %% [markdown]
# ## Carbosense
#
# The project Carbosense establishes a uniquely dense CO2 sensor network across Switzerland to provide near-real time information on man-made emissions and CO2 uptake by the biosphere. The main goal of the project is to improve the understanding of the small-scale CO2 fluxes in Switzerland and concurrently to contribute to a better top-down quantification of the Swiss CO2 emissions. The Carbosense network has a spatial focus on the City of Zurich where more than 50 sensors are deployed. Network operations started in July 2017.
#
# <img src="http://carbosense.wdfiles.com/local--files/main:project/CarboSense_MAP_20191113_LowRes.jpg" width="500">
#
# <img src="http://carbosense.wdfiles.com/local--files/main:sensors/LP8_ZLMT_3.JPG" width="156">  <img src="http://carbosense.wdfiles.com/local--files/main:sensors/LP8_sensor_SMALL.jpg" width="300">

# %% [markdown]
# ## Description of the homework
#
# In this homework, we will curate a set of **CO2 measurements**, measured from cheap but inaccurate sensors, that have been deployed in the city of Zurich from the Carbosense project. The goal of the exercise is twofold: 
#
# 1. Learn how to deal with real world sensor timeseries data, and organize them efficiently using python dataframes.
#
# 2. Apply data science tools to model the measurements, and use the learned model to process them (e.g., detect drifts in the sensor measurements). 
#
# The sensor network consists of 46 sites, located in different parts of the city. Each site contains three different sensors measuring (a) **CO2 concentration**, (b) **temperature**, and (c) **humidity**. Beside these measurements, we have the following additional information that can be used to process the measurements: 
#
# 1. The **altitude** at which the CO2 sensor is located, and the GPS coordinates (latitude, longitude).
#
# 2. A clustering of the city of Zurich in 17 different city **zones** and the zone in which the sensor belongs to. Some characteristic zones are industrial area, residential area, forest, glacier, lake, etc.
#
# ## Prior knowledge
#
# The average value of the CO2 in a city is approximately 400 ppm. However, the exact measurement in each site depends on parameters such as the temperature, the humidity, the altitude, and the level of traffic around the site. For example, sensors positioned in high altitude (mountains, forests), are expected to have a much lower and uniform level of CO2 than sensors that are positioned in a business area with much higher traffic activity. Moreover, we know that there is a strong dependence of the CO2 measurements, on temperature and humidity.
#
# Given this knowledge, you are asked to define an algorithm that curates the data, by detecting and removing potential drifts. **The algorithm should be based on the fact that sensors in similar conditions are expected to have similar measurements.** 
#
# ## To start with
#
# The following csv files in the `../data/carbosense-raw/` folder will be needed: 
#
# 1. `CO2_sensor_measurements.csv`
#     
#    __Description__: It contains the CO2 measurements `CO2`, the name of the site `LocationName`, a unique sensor identifier `SensorUnit_ID`, and the time instance in which the measurement was taken `timestamp`.
#     
# 2. `temperature_humidity.csv`
#
#    __Description__: It contains the temperature and the humidity measurements for each sensor identifier, at each timestamp `Timestamp`. For each `SensorUnit_ID`, the temperature and the humidity can be found in the corresponding columns of the dataframe `{SensorUnit_ID}.temperature`, `{SensorUnit_ID}.humidity`.
#     
# 3. `sensor_metadata_updated.csv`
#
#    __Description__: It contains the name of the site `LocationName`, the zone index `zone`, the altitude in meters `altitude`, the longitude `LON`, and the latitude `LAT`. 
#
# Import the following python packages:

# %%
import pandas as pd
import numpy as np
import warnings
import sklearn
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
from sklearn import covariance
from sklearn.metrics import euclidean_distances, mean_absolute_error

from sklearn import covariance

# %%
pd.options.mode.chained_assignment = None
warnings.filterwarnings('ignore')

# %% [markdown]
# ## PART I: Handling time series with pandas (10 points)

# %% [markdown]
# ### a) **8/10**
#
# Merge the `CO2_sensor_measurements.csv`, `temperature_humidity.csv`, and `sensors_metadata_updated.csv`, into a single dataframe. 
#
# * The merged dataframe contains:
#     - index: the time instance `timestamp` of the measurements
#     - columns: the location of the site `LocationName`, the sensor ID `SensorUnit_ID`, the CO2 measurement `CO2`, the `temperature`, the `humidity`, the `zone`, the `altitude`, the longitude `lon` and the latitude `lat`.
#
# | timestamp | LocationName | SensorUnit_ID | CO2 | temperature | humidity | zone | altitude | lon | lat |
# |:---------:|:------------:|:-------------:|:---:|:-----------:|:--------:|:----:|:--------:|:---:|:---:|
# |    ...    |      ...     |      ...      | ... |     ...     |    ...   |  ... |    ...   | ... | ... |
#
#
#
# * For each measurement (CO2, humidity, temperature), __take the average over an interval of 30 min__. 
#
# * If there are missing measurements, __interpolate them linearly__ from measurements that are close by in time.
#
# __Hints__: The following methods could be useful
#
# 1. ```python 
# pandas.DataFrame.resample()
# ``` 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html
#     
# 2. ```python
# pandas.DataFrame.interpolate()
# ```
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html
#     
# 3. ```python
# pandas.DataFrame.mean()
# ```
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html
#     
# 4. ```python
# pandas.DataFrame.append()
# ```
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html
# %% [markdown]
# Loading in the data from lfs and read the downloaded csv files
# %%
! git lfs pull

carbon_data = pd.read_csv("../data/carbosense-raw/CO2_sensor_measurements.csv", sep="\t")
sensors_metadata = pd.read_csv("../data/carbosense-raw/sensors_metadata_updated.csv", sep=",", index_col=0)
temperature_humidity = pd.read_csv("../data/carbosense-raw/temperature_humidity.csv",sep="\t")

# %% [markdown]
# Casting timestamp as datetime types
# %%
temperature_humidity["Timestamp"] = pd.to_datetime(temperature_humidity["Timestamp"], infer_datetime_format=True)
carbon_data["timestamp"] = pd.to_datetime(carbon_data["timestamp"], infer_datetime_format=True)

# %% [markdown]
# Setting the timestamp as index and interpolating temperature and humidity data
# %%
temperature_humidity_interpolated = temperature_humidity.set_index("Timestamp").interpolate(axis=0).reset_index()

# %% [markdown]
# Taking the average of the data every 30 minutes 
# %%
temperature_humidity_30 = temperature_humidity_interpolated.resample('30T', on="Timestamp").mean().reset_index()

# %% [markdown]
# Taking the average of the data every 30 minutes and interpolating the missing CO2 values.<br>
# Checking that we do not have any NaN values left in the Dataframe.<br>
# Some sensors lack data for some dates as for examples sensor 1174.<br>For these sensors, we have chosen to only include timestamps where sensor data exists.
# %%
carbon_data30 = carbon_data.groupby(["SensorUnit_ID", "LocationName"]).resample('30T', on="timestamp").agg(
    {"CO2": "mean"})
carbon_data30["CO2"] = carbon_data30["CO2"].interpolate(axis=0)
carbon_data30 = carbon_data30.reset_index()

assert not carbon_data30.isna().sum().any()

# %% [markdown]
# Joining the carbon data as well as the metadata.
# %%
carbon_and_metadata = carbon_data30.join(sensors_metadata.set_index("LocationName"), on='LocationName')

# %% [markdown]
# Melting the temperature data to a long list and separating temperature and humidity data.
# %%
temperature_humidity_melted = temperature_humidity_30.melt(id_vars="Timestamp", var_name="id", value_name="value")
temperature_humidity_melted[["id", "type"]] = temperature_humidity_melted["id"].str.split(".", expand=True)
temperature_humidity_melted = temperature_humidity_melted.astype({"id": "int64"})
temperature_data_melted = temperature_humidity_melted[temperature_humidity_melted["type"] == "temperature"]
humidity_data_melted = temperature_humidity_melted[temperature_humidity_melted["type"] == "humidity"]
# %% [markdown]
# Mergeing carbon_and_metadata, temperature_data_melted and humidity_data_melted.
# %%
all_data = carbon_and_metadata.merge(temperature_data_melted, left_on=["SensorUnit_ID", "timestamp"], right_on=["id", "Timestamp"])
all_data = all_data.merge(humidity_data_melted, left_on=["id", "Timestamp"], right_on=["id", "Timestamp"])
all_data
# %% [markdown]
# Dropping and renaming columns to get a Dataframe with the correct format.
# %%
all_data = all_data.drop(columns=["type_x", "type_y", "X", "Y", "Timestamp"])
all_data = all_data.rename(columns={"LAT": "lat", "LON": "lon", "value_x": "temperature", "value_y": "humidity"})
all_data = all_data[
    ["timestamp", "LocationName", "SensorUnit_ID", "CO2", "temperature", "humidity", "zone", "altitude", "lon", "lat"]]
all_data = all_data.set_index("timestamp")
# %%
all_data.to_csv("../data/output/all_data.csv")
assert all_data.isna().sum().max() == 0 #Check no nan values
# Some sensors lack data for some dates
# For examples 1174. For these, we've currently chosen to only include timestamps where
# sensor data exists.


# %% [markdown]
# ### b) **2/10** 
#
# Export the curated and ready to use timeseries to a csv file, and properly push the merged csv to Git LFS.

# %% [markdown]
# Writing the final Dataframe as a csv file.
# Some sensors lack data for some dates as for examples sensor 1174. 
# For these sensors, we have chosen to only include timestamps where sensor data exists.
# %%
all_data.to_csv("../data/output/all_data.csv")
all_data
# %%
# ! git lfs track "/data/output/*csv"

# %%
# ! git lfs ls-files

# %% [markdown]
# ## PART II: Data visualization (15 points)

# %% [markdown]
# ### a) **5/15** 
# Group the sites based on their altitude, by performing K-means clustering. 
# - Find the optimal number of clusters using the [Elbow method](https://en.wikipedia.org/wiki/Elbow_method_(clustering)). 
# - Wite out the formula of metric you use for Elbow curve. 
# - Perform clustering with the optimal number of clusters and add an additional column `altitude_cluster` to the dataframe of the previous question indicating the altitude cluster index. 
# - Report your findings.
#
# __Note__: [Yellowbrick](http://www.scikit-yb.org/) is a very nice Machine Learning Visualization extension to scikit-learn, which might be useful to you. 

# %%
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

# %% [markdown]
# Averaging the altitude of the individual sensors
# %%
all_data_sites = all_data.groupby(['LocationName','SensorUnit_ID'])['altitude'].mean().reset_index()
# %% [markdown]
# Check that all_data_sites has the correct number of rows that includes all the individual sensors
# %%
assert len(set(all_data_sites.SensorUnit_ID)) == len(all_data_sites)
# %% [markdown]
# Plot the sensors depending on their location

# %%
fig = px.scatter(x=all_data_sites.SensorUnit_ID,y=all_data_sites.altitude)
fig.show()

# %% [markdown]
# Reshape the altitude data in order to apply K-Means to cluster the altitudes.
# We reshape to (-1,1) because the data consists of multiple samples with only a single feature, so we need to have the data in a multiple row (-1) and one column (1) shape.

# %%
all_data_resh = all_data_sites['altitude'].to_numpy().reshape(-1,1)

# %% [markdown]
# Fit and Plot KMeans with the KElbowVisualizer, function that helps us to find the optimal number of clusters *k* by fitting the model with a range of *k* values.

# %%
model = KMeans()
vis = KElbowVisualizer(model, k=(3,10), timings=False)

vis.fit(all_data_resh)
vis.show()

# %% [markdown]
# The "elbow", the point of inflection on the curve, indicates us the *k*-value in which the model fits best. In this case, the optimal value is *k*=5.

# %%
vis.elbow_value_

# %% [markdown]
# Train again our data but now only with the *elbow value*.

# %% tags=[]
model_elbow = KMeans(n_clusters=vis.elbow_value_,random_state=0)
model_elbow.fit(all_data_resh)
model_elbow.labels_

# %% [markdown]
# We cast our labels from int values to string values in order to discretize them and then we sort them by the altitude cluster value, and we plot them.

# %%
all_data_sites['altitud cluster'] = [str(l) for l in model_elbow.labels_]
all_data_sites.sort_values(by='altitud cluster',inplace=True)

# %% [markdown]
# Now, we plot the altitude clustering we have obtained with KMeans (*k*=5)

# %%
fig = px.scatter(all_data_sites, x='SensorUnit_ID',y='altitude',color= 'altitud cluster')
fig.show()


# %% [markdown]
# We can see that have obtained 5 clusters, and each cluster includes a range of altitude. The Y axis is the altitude, and the X axis is the ID of the sensor, that it is just a feature we have selected to plot the clusters but it does not affect the clustering of the sensors.
#
# Now, we are going to add to each sensor the cluster where it belongs. For that, we create a dictionary where the keys will be the IDs of the sensors and the values the cluster.

# %%
dict_alt = {k:v for k,v in zip(all_data_sites.SensorUnit_ID,model_elbow.labels_)}

# %% [markdown]
# Set the cluster value to its correspondent sample. We can check it and look how many times appears its altitude cluster in our dataset, with the numpy-function ```bincount```

# %%
all_data['altitude_cluster'] = all_data.SensorUnit_ID.map(dict_alt)
np.bincount(all_data.altitude_cluster)

# %% [markdown]
# ### b) **4/15** 
#
# Use `plotly` (or other similar graphing libraries) to create an interactive plot of the monthly median CO2 measurement for each site with respect to the altitude. 
#
# Add proper title and necessary hover information to each point, and give the same color to stations that belong to the same altitude cluster.


# %%
median_monthly_co2_altitude = all_data.groupby("SensorUnit_ID").resample('31D').agg({"CO2":"median", "altitude": "first", "LocationName": "first", "altitude_cluster": "first"})[["CO2", "altitude", "LocationName", "altitude_cluster"]]
median_monthly_co2_altitude

# %% [markdown]
# We discretize and sort by the cluster values again, and then we plot the data. This time, we plot to find a relation between CO2 and sensor altitude.

# %%
import plotly.express as px

median_monthly_co2_altitude.altitude_cluster = median_monthly_co2_altitude.altitude_cluster.astype(str)
median_monthly_co2_altitude.sort_values("altitude_cluster",inplace=True)

fig = px.scatter(median_monthly_co2_altitude, x="altitude", y="CO2", hover_data=["LocationName"], color="altitude_cluster")
fig.update_layout(title='Monthly median CO2 vs sensor altitude')
fig.show()

# %% [markdown]
# ### c) **6/15**
#
# Use `plotly` (or other similar graphing libraries) to plot an interactive time-varying density heatmap of the mean daily CO2 concentration for all the stations. Add proper title and necessary hover information.
#
# __Hints:__ Check following pages for more instructions:
# - [Animations](https://plotly.com/python/animations/)
# - [Density Heatmaps](https://plotly.com/python/mapbox-density-heatmaps/)

# %% [markdown]
# We compute the average of the diary values of CO2 and temperature in each sensor, and we also cast the timestamp values to string.

# %%
zone_sensors = all_data.reset_index().groupby(["SensorUnit_ID", "LocationName"]).resample('1D', on="timestamp").agg(
    {"CO2": "mean",
     "temperature": "mean",
     "lat": "first",
     "lon": "first"}).reset_index()
zone_sensors.timestamp = zone_sensors.timestamp.astype(str)

# TODO: add ppm to CO2 levels, format timestamp and chhange its name to day

fig = px.density_mapbox(zone_sensors, lat='lat', lon='lon', z='CO2',
                        animation_frame="timestamp",
                        hover_data=['SensorUnit_ID', 'temperature'],
                        title='Time-varying density heatmap of the mean daily CO2 concentration across stations around Zurich',
                        range_color=zone_sensors.CO2.quantile([0.01, 0.99]).to_list(),
                        zoom=9,
                        mapbox_style="stamen-terrain")
fig.show()

# %% [markdown]
# ## PART III: Model fitting for data curation (35 points)

# %% [markdown]
# ### a) **2/35**
#
# The domain experts in charge of these sensors report that one of the CO2 sensors `ZSBN` is exhibiting a drift on Oct. 24. Verify the drift by visualizing the CO2 concentration of the drifting sensor and compare it with some other sensors from the network. 

# %% [markdown]
# Choosing the sensors from the same zone as ZBSN.
#
# Visualizing the CO2 concretation of ZSBN sensors in red, while the others sensors in the same zone in grey. 

# %%
ZSBN = all_data[all_data['LocationName'] == 'ZSBN']
zone_sensors = all_data[all_data['zone'] == ZSBN['zone'][0]]
fig = px.line(zone_sensors, y="CO2", color='LocationName')
fig.add_vline(x='2017-10-24', line_dash="dash", line_color="green")

# edit colors
for d in fig['data']:
    if d['name'] == 'ZSBN':
        d['line']['color'] = 'red'
    else:
        d['line']['color'] = 'lightgrey'

fig.show()

# %% [markdown]
# ### b) **8/35**
#
# The domain experts ask you if you could reconstruct the CO2 concentration of the drifting sensor had the drift not happened. You decide to:
# - Fit a linear regression model to the CO2 measurements of the site, by considering as features the covariates not affected by the malfunction (such as temperature and humidity)
# - Create an interactive plot with `plotly` (or other similar graphing libraries):
#     - the actual CO2 measurements
#     - the values obtained by the prediction of the linear model for the entire month of October
#     - the __confidence interval__ obtained from cross validation
# - What do you observe? Report your findings.
#
# __Note:__ Cross validation on time series is different from that on other kinds of datasets. The following diagram illustrates the series of training sets (in orange) and validation sets (in blue). For more on time series cross validation, there are a lot of interesting articles available online. scikit-learn provides a nice method [`sklearn.model_selection.TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html).
#
# ![ts_cv](https://player.slideplayer.com/86/14062041/slides/slide_28.jpg)


# %%
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit
import scipy.stats

# %% [markdown]
# Split the ZSBN data in two datasets, one data before the drift and the other, that we will predict, after the drift. We also select the covariates that were not affected by the malfunction of the sensor.

# %%
ZSBN = all_data[all_data['LocationName'] == 'ZSBN']

train = ZSBN[:"2017-10-23 23:30:00"]
pred =  ZSBN["2017-10-23 23:59:00":]

covariates = ["temperature", "humidity"]

X_train = train[covariates].to_numpy()
y_train = train["CO2"].to_numpy()

X_pred = pred[covariates].to_numpy()

# %% [markdown]
# We split the training data in 5 splits with the Time Series Cross-Validation (explained above), and we train and validate our LinearRegression model with each Time Series split. 
#
# Then, we use the different folder scores to compute the 95% Confidence Interval, calculating the mean and the percentile of the scores.

# %%
# TODO: Confidence interval unclear
def get_confidence_interval(X, y):
    tscv = TimeSeriesSplit(n_splits=5)
    model = LinearRegression()

    scores = []
    residuals = np.array([])
    for train_index, val_index in tscv.split(X):

        X_fold_train, X_fold_val = X[train_index], X[val_index]
        y_fold_train, y_fold_val = y[train_index], y[val_index]

        trained_model = model.fit(X_fold_train, y_fold_train)
        y_fold_pred = trained_model.predict(X_fold_val)
        scores.append(trained_model.score(X_fold_val, y_fold_val))

        residuals = np.append(residuals, y_fold_val - y_fold_pred)

    print("score mean:", np.mean(scores))
    term1, term2 = np.percentile(residuals, 2.5), np.percentile(residuals, 97.5)
    assert ((np.logical_and(term1 <= residuals, residuals <= term2))).sum() / residuals.size == 0.95
    return term1, term2

term1, term2 = get_confidence_interval(X_train, y_train)


# %% [markdown]
# After the validation of our model, we fit the model again, and we predict the CO2 values after the drift. <br>
# We mark the CO2 values depending if they were measured or predicted, in order to plot them with different styles later.

# %%
model = LinearRegression().fit(X_train, y_train)

# %%
train['CO2_values'] = 'measured'
pred['CO2_values'] = 'measured'

overwritten_pred = pred.copy()
overwritten_pred['CO2'] = model.predict(X_pred)
overwritten_pred['CO2_values'] = 'prediction on drift data'

overwritten_train = train.copy()
overwritten_train['CO2'] = model.predict(X_train)
overwritten_train['CO2_values'] = 'prediction on training data'

# %% [markdown]
# We plot our prediction after the 24th of October in red, and the prediction on the training data from before the 24th of October in green. <br>
# The predictied data seems to fit well the fluctuation of the measured data before the drift.

# %% Plot the predicted data of the training data as well
fig = px.line(pd.concat([train, pred , overwritten_pred, overwritten_train]),
              y="CO2", color ="CO2_values")
fig.add_vline(x='2017-10-24', line_dash="dash", line_color="green") #, annotation_text="drift date", annotation_position="bottom right")
fig.show()

# %% [markdown]
# Here we define a function to plot a given confidence interval.

# %% Plot with confidence interval
def plot_confidence_interval(measured, predicted, ci_term1, ci_term2):
    fig = go.Figure([
        go.Scatter(
            name='Measurement',
            x=measured.index,
            y=measured.CO2,
            mode='lines',
            line=dict(color='blue'),
        ),
        go.Scatter(
            name='Prediction',
            x=predicted.index,
            y=predicted.CO2,
            mode='lines',
            line=dict(color='red'),
        ),
        go.Scatter(
            name='Upper Bound',
            x=predicted.index,
            y=predicted.CO2 + ci_term2,
            mode='lines',
            marker=dict(color="#444"),
            line=dict(width=0),
            showlegend=False
        ),
        go.Scatter(
            name='Lower Bound',
            x=predicted.index,
            y=predicted.CO2 + ci_term1,
            marker=dict(color="#444"),
            line=dict(width=0),
            mode='lines',
            fillcolor='rgba(68, 68, 68, 0.3)',
            fill='tonexty',
            showlegend=False
        )
    ])
    fig.update_layout(
        yaxis_title='CO2',
        title='Predicted vs Measured CO2 during October',
        hovermode="x"
    )
    fig.add_vline(x='2017-10-24', line_dash="dash", line_color="green") #, annotation_text="drift date", annotation_position="bottom right")
    fig.update_xaxes(dtick=86400000)
    return fig

plot_confidence_interval(ZSBN, pd.concat([overwritten_train, overwritten_pred]), term1, term2).show()


# %% [markdown]
# Plotting the surface of the Linear Regresson to the humidity and temperature to make sure our model is reasonable.

# %%
space = [np.linspace(min_,max_,10) for min_, max_ in zip(np.min(X_train, axis=0), np.max(X_train, axis=0))]
xx, yy = np.meshgrid(*space)
pred_surface = model.predict(np.c_[xx.ravel(), yy.ravel()])
pred_surface = pred_surface.reshape(xx.shape)

fig = px.scatter_3d(train, x='temperature', y='humidity', z='CO2')
fig.update_traces(marker=dict(size=5))
fig.add_traces(go.Surface(x=space[0], y=space[1], z=pred_surface, name='pred_surface'))
fig.show()

# %%
fig = make_subplots(rows=1, cols=2)
for i, name in enumerate(["temperture", "humidity"]):
    fig.add_trace(go.Scatter(x=X_train[:, i], 
                             y=y_train, 
                             name=name,
                             mode="markers"),
                             row=1, 
                             col=i+1)
    fig.update_xaxes(title_text=name, row=1, col=i+1)
    fig.update_yaxes(title_text='CO2', row=1, col=i+1)
fig.show()

# %% [markdown]
#
# ### c) **10/35**
#
# In your next attempt to solve the problem, you decide to exploit the fact that the CO2 concentrations, as measured by the sensors __experiencing similar conditions__, are expected to be similar.
#
# - Find the sensors sharing similar conditions with `ZSBN`. Explain your definition of "similar condition".
# - Fit a linear regression model to the CO2 measurements of the site, by considering as features:
#     - the information of provided by similar sensors
#     - the covariates associated with the faulty sensors that were not affected by the malfunction (such as temperature and humidity).
# - Create an interactive plot with `plotly` (or other similar graphing libraries):
#     - the actual CO2 measurements
#     - the values obtained by the prediction of the linear model for the entire month of October
#     - the __confidence interval__ obtained from cross validation
# - What do you observe? Report your findings.

# %% [markdown]
# ### Similar sensors
#
# In this part we identify sensors which could be categorized as experiencing similar conditions as the drifting sensor.
#
# 3 main categories for similar sensors were identified.
# - Sensors that are in the same zone
# - Sensors that are geographically close to the drifting sensor
# - Sensors that are in the same altritude cluster ass the drifiting sensors
#
# The sensor values from these similar sensors were used as additional features in the training model to predict the CO2 value of the drifiting sensor.

# %%

from sklearn.metrics.pairwise import haversine_distances

ZSBN_timeseries = all_data[all_data['LocationName'] == 'ZSBN']

all_sensors = all_data.groupby(["LocationName"]).agg({"SensorUnit_ID": "first", "zone": "first", "altitude": "first", "lon": "first", "lat": "first", "altitude_cluster": "first"})
ZSBN_sensor = all_sensors.loc['ZSBN']
all_data
# %%
## Sensors in the same zone
same_zone_sensors = all_sensors[all_sensors['zone'] == all_sensors.loc['ZSBN']["zone"]].filter([""])
same_zone_sensors # 6 Sensors, including ZSBN

# %%
## Sensors that are close to ZSBN
sensor_coords = all_sensors[["lon", "lat"]].apply(np.radians)
sensor_coords["distance_km"] = haversine_distances(sensor_coords, [[sensor_coords.loc['ZSBN']["lon"], sensor_coords.loc['ZSBN']["lat"]]]) * (6371000/1000)

closest_10_sensors = sensor_coords.sort_values("distance_km")[1:11].filter([""])
closest_10_sensors

# %%
## Sensors in the same altitude cluster
same_altitude_cluster = all_sensors[all_sensors['altitude_cluster'] == all_sensors.loc['ZSBN']['altitude_cluster']].filter([""])
same_altitude_cluster

# %%
similar_sensors = pd.DataFrame(same_altitude_cluster).join([closest_10_sensors, same_zone_sensors], how="outer").reset_index()
similar_sensors

# %%
# The time series data from the selected similar sensors are combined and transformed into the training data format. 

similar_sensors_series = all_data[all_data["LocationName"].isin(similar_sensors["LocationName"])]
similar_train = similar_sensors_series[:"2017-10-23 23:30:00"]
similar_pred =  similar_sensors_series["2017-10-23 23:59:00":]

covariates = ["humidity", "temperature"]
grouped = all_data.groupby(["LocationName"])

combined = grouped.get_group(similar_sensors["LocationName"][0])[covariates]


for sensor in similar_sensors["LocationName"][1:]:
  combined = combined.merge(grouped.get_group(sensor)[covariates], right_on="timestamp", left_on="timestamp", how="left" )

# We drop columns from two sensor containing only sensor data for a subset of the period.
combined = combined.dropna(axis=1)
assert combined.isna().sum().all() == 0


X_train = combined[:"2017-10-23 23:30:00"].to_numpy()
X_pred = combined["2017-10-23 23:59:00":].to_numpy()

y_train = train["CO2"].to_numpy()


# %%

term1, term2 = get_confidence_interval(X_train, y_train)

# %%

model = model.fit(X_train, y_train)
overwritten_pred = pred.copy()
overwritten_pred['CO2'] = model.predict(X_pred)
overwritten_pred['CO2_values'] = 'predicted'

plot_confidence_interval(ZSBN, pd.concat([overwritten_train, overwritten_pred]), term1, term2)


# %% [markdown]
# ### Observed results
#
# By using the combination of the sensor data from the identified similar sensors, a r2 score mean
# after cross validation of 0.53 is achived. Significalty higher than the original predictionsmade only
# using the drifiting sensor covariates. 

# %% [markdown]
# ### d) **10/35**
#
# Now, instead of feeding the model with all features, you want to do something smarter by using linear regression with fewer features.
#
# - Start with the same sensors and features as in question c)
# - Leverage at least two different feature selection methods
# - Create similar interactive plot as in question c)
# - Describe the methods you choose and report your findings

# %%
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold, SelectKBest, SelectFromModel, f_regression

# %% [markdown]
# We start by using PCA, where the number of components was chosen so all the singular values are larger than 150.
# %%
pca = PCA(n_components=5)
pca.fit(np.append(X_train, X_pred, axis=0))
print(pca.singular_values_)

X_train_select = pca.transform(X_train)
X_pred_select = pca.transform(X_pred)

ci = get_confidence_interval(X_train_select, y_train)

model = model.fit(X_train_select, y_train)
overwritten_pred = pred.copy()
overwritten_pred['CO2'] = model.predict(X_pred_select)
overwritten_pred['CO2_values'] = 'predicted'

plot_confidence_interval(ZSBN, overwritten_pred, *ci)

# %% [markdown]
# We then use VarianceThreshold, with a theshold of 100. <br>
# The resulting data has 15 features chosen.
# %%
vth = VarianceThreshold(threshold=100)
vth.fit(np.append(X_train, X_pred, axis=0))

X_train_select = vth.transform(X_train)
X_pred_select = vth.transform(X_pred)
ci = get_confidence_interval(X_train_select, y_train)
print(X_train_select.shape, X_pred_select.shape)

model = model.fit(X_train_select, y_train)
overwritten_pred = pred.copy()
overwritten_pred['CO2'] = model.predict(X_pred_select)
overwritten_pred['CO2_values'] = 'predicted'

plot_confidence_interval(ZSBN, overwritten_pred, *ci)

# %% [markdown]
# Now, we use *SelectKBest*, that gives us the best 20 features.

# %%
skb = SelectKBest(f_regression, k=20)
X_train_select = skb.fit_transform(X_train, y_train)
X_pred_select = skb.transform(X_pred)
ci = get_confidence_interval(X_train_select, y_train)
print(X_train_select.shape, X_pred_select.shape)

model = model.fit(X_train_select, y_train)
overwritten_pred = pred.copy()
overwritten_pred['CO2'] = model.predict(X_pred_select)
overwritten_pred['CO2_values'] = 'predicted'

plot_confidence_interval(ZSBN, overwritten_pred, *ci)

# %% [markdown]
# Finally, we use *SelectFromModel*, that uses our classifier to select the best features. In this case, it has chosen 12 features.

# %%
sfm = SelectFromModel(estimator=LinearRegression())
X_train_select = sfm.fit_transform(X_train, y_train)
X_pred_select = sfm.transform(X_pred)
ci = get_confidence_interval(X_train_select, y_train)
print(X_train_select.shape, X_pred_select.shape)

model = model.fit(X_train_select, y_train)
overwritten_pred = pred.copy()
overwritten_pred['CO2'] = model.predict(X_pred_select)
overwritten_pred['CO2_values'] = 'predicted'

plot_confidence_interval(ZSBN, overwritten_pred, *ci)

# %% [markdown]
# As conclusion, we can say that *PCA* has given us the best results by far, not only because of the score but because it uses just 5 features, while the others use at least 12 features.<br>
# While *VarianceThreshold* and *SelectFromModel* have provided us a decent performance, we have that SelectKBest has the worst performance by very far.

# %% [markdown]
# ### e) **5/35**
#
# Eventually, you'd like to try something new - __Bayesian Structural Time Series Modelling__ - to reconstruct counterfactual values, that is, what the CO2 measurements of the faulty sensor should have been, had the malfunction not happened on October 24. You will use:
# - the information of provided by similar sensors - the ones you identified in question c)
# - the covariates associated with the faulty sensors that were not affected by the malfunction (such as temperature and humidity).
#
# To answer this question, you can choose between a Python port of the CausalImpact package (such as https://github.com/jamalsenouci/causalimpact) or the original R version (https://google.github.io/CausalImpact/CausalImpact.html) that you can run in your notebook via an R kernel (https://github.com/IRkernel/IRkernel).
#
# Before you start, watch first the [presentation](https://www.youtube.com/watch?v=GTgZfCltMm8) given by Kay Brodersen (one of the creators of the causal impact implementation in R), and this introductory [ipython notebook](https://github.com/jamalsenouci/causalimpact/blob/HEAD/GettingStarted.ipynb) with examples of how to use the python package.
#
# - Report your findings:
#     - Is the counterfactual reconstruction of CO2 measurements significantly different from the observed measurements?
#     - Can you try to explain the results?

# %%
from causalimpact import CausalImpact

data_causal_impact = pd.DataFrame(ZSBN["CO2"]).join(combined)

pre_period = [pd.to_datetime(date) for date in ["2017-10-01", "2017-10-23"]]
post_period = [pd.to_datetime(date) for date in ["2017-10-24", "2017-10-31"]]
ci = CausalImpact(data_causal_impact, pre_period, post_period)
ci.run()
ci.plot()

#%%
ci.summary(output="report")

# %% [markdown]
# We observe a cumulative drift on the sensor with an relative effect of -12.2%, according to the package the negative effect observed during the intervention period is statistically significant
# The counterfactual reconstruction of CO2 measurements is significantly different from the observed measurements.