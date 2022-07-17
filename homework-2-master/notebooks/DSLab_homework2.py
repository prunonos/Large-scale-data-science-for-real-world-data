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
# # Homework 2 - Data Wrangling with Hadoop
#
# The goal of this assignment is to put into action the data wrangling techniques from the exercises of week-3 and week-4. We highly suggest you to finish these two exercises first and then start the homework. In this homework, we are going to reuse the same __   __ and __twitter__ datasets as seen before during these two weeks. 
#
# ## Hand-in Instructions
# - __Due: 03.04.2022 23:59 CET__
# - Fork this project as a private group project
# - Verify that all your team members are listed as group members of the project
# - `git push` your final verion to your group's Renku repository before the due date
# - Verify that `Dockerfile`, `environment.yml` and `requirements.txt` are properly written and notebook is functional
# - Add necessary comments and discussion to make your queries readable
#
# ## Hive Documentation
#
# Hive queries: <https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Select>
#
# Hive functions: <https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF>

# %% [markdown]
# <div style="font-size: 100%" class="alert alert-block alert-warning">
#     <b>Get yourself ready:</b> 
#     <br>
#     Before you jump into the questions, please first go through the notebook <a href='./prepare_env.ipynb'>prepare_env.ipynb</a> and make sure that your environment is properly set up.
#     <br><br>
#     <b>Cluster Usage:</b>
#     <br>
#     As there are many of you working with the cluster, we encourage you to prototype your queries on small data samples before running them on whole datasets.
#     <br><br>
#     <b>Try to use as much HiveQL as possible and avoid using pandas operations. Also, whenever possible, try to apply the methods you learned in class to optimize your queries to minimize the use of computing resources.</b>
# </div>

# %% [markdown]
# ## Part I: SBB/CFF/FFS Data (40 Points)
#
# Data source: <https://opentransportdata.swiss/en/dataset/istdaten>
#
# In this part, you will leverage Hive to perform exploratory analysis of data published by the [Open Data Platform Swiss Public Transport](https://opentransportdata.swiss).
#
# Format: the dataset is originally presented as a collection of textfiles with fields separated by ';' (semi-colon). For efficiency, the textfiles have been converted into Optimized Row Columnar ([_ORC_](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ORC)) file format. 
#
# Location: you can find the data in ORC format on HDFS at the path `/data/sbb/part_orc/istdaten`.
#
# The full description from opentransportdata.swiss can be found in <https://opentransportdata.swiss/de/cookbook/ist-daten/> in four languages. There may be inconsistencies or missing information between the translations.. In that case we suggest you rely on the German version and use an automated translator when necessary. We will clarify if there is still anything unclear in class and Slack. Here we remind you the relevant column descriptions:
#
# - `BETRIEBSTAG`: date of the trip
# - `FAHRT_BEZEICHNER`: identifies the trip
# - `BETREIBER_ABK`, `BETREIBER_NAME`: operator (name will contain the full name, e.g. Schweizerische Bundesbahnen for SBB)
# - `PRODUKT_ID`: type of transport, e.g. train, bus
# - `LINIEN_ID`: for trains, this is the train number
# - `LINIEN_TEXT`,`VERKEHRSMITTEL_TEXT`: for trains, the service type (IC, IR, RE, etc.)
# - `ZUSATZFAHRT_TF`: boolean, true if this is an additional trip (not part of the regular schedule)
# - `FAELLT_AUS_TF`: boolean, true if this trip failed (cancelled or not completed)
# - `HALTESTELLEN_NAME`: name of the stop
# - `ANKUNFTSZEIT`: arrival time at the stop according to schedule
# - `AN_PROGNOSE`: actual arrival time
# - `AN_PROGNOSE_STATUS`: show how the actual arrival time is calcluated
# - `ABFAHRTSZEIT`: departure time at the stop according to schedule
# - `AB_PROGNOSE`: actual departure time
# - `AB_PROGNOSE_STATUS`: show how the actual departure time is calcluated
# - `DURCHFAHRT_TF`: boolean, true if the transport does not stop there
#
# Each line of the file represents a stop and contains arrival and departure times. When the stop is the start or end of a journey, the corresponding columns will be empty (`ANKUNFTSZEIT`/`ABFAHRTSZEIT`).
#
# In some cases, the actual times were not measured so the `AN_PROGNOSE_STATUS`/`AB_PROGNOSE_STATUS` will be empty or set to `PROGNOSE` and `AN_PROGNOSE`/`AB_PROGNOSE` will be empty.

# %% [markdown]
# __Initialization__

# %%
import os
import pandas as pd
pd.set_option("display.max_columns", 50)
import matplotlib.pyplot as plt
# %matplotlib inline
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

username = os.environ['RENKU_USERNAME']
hiveaddr = os.environ['HIVE_SERVER2']
(hivehost,hiveport) = hiveaddr.split(':')
print("Operating as: {0}".format(username))

# %%
from pyhive import hive

# create connection
conn = hive.connect(host=hivehost, 
                    port=int(hiveport),
                    username=username) 
# create cursor
cur = conn.cursor()

# %% [markdown]
# ### a) Prepare the table - 5/40
#
# Complete the code in the cell below, replace all `TODO` in order to create a Hive Table of SBB Istadaten.
#
# The table has the following properties:
#
# * The table is in your database, which must have the same name as your gaspar ID
# * The table name is `sbb_orc`
# * The table must be external
# * The table content consist of ORC files in the HDFS folder `/data/sbb/part_orc/istdaten`
# * The table is _partitioned_, and the number of partitions should not exceed 50
#

# %%
### Create your database if it does not exist
query = """
CREATE DATABASE IF NOT EXISTS {0} LOCATION '/user/{0}/hive'
""".format(username)
cur.execute(query)
x = cur.fetch_logs()
print(x)

# %%
### Make your database the default
query = """
USE {0}
""".format(username)
cur.execute(query)

# %%
query = """
DROP TABLE IF EXISTS {0}.sbb_orc
""".format(username)
cur.execute(query)

# %%
query = """
CREATE EXTERNAL TABLE {0}.sbb_orc(
        BETRIEBSTAG string,
        FAHRT_BEZEICHNER string,
        BETREIBER_ID string,
        BETREIBER_ABK string,
        BETREIBER_NAME string,
        PRODUKT_ID string,
        LINIEN_ID string,
        LINIEN_TEXT string,
        UMLAUF_ID string,
        VERKEHRSMITTEL_TEXT string,
        ZUSATZFAHRT_TF string,
        FAELLT_AUS_TF string,
        BPUIC string,
        HALTESTELLEN_NAME string,
        ANKUNFTSZEIT string,
        AN_PROGNOSE string,
        AN_PROGNOSE_STATUS string,
        ABFAHRTSZEIT string,
        AB_PROGNOSE string,
        AB_PROGNOSE_STATUS string,
        DURCHFAHRT_TF string
    ) PARTITIONED BY (year string, month string)
    row format delimited fields terminated by ';'
    stored as orc
    location '/data/sbb/part_orc/istdaten'
    tblproperties ("skip.header.line.count"="1")
""".format(username)
cur.execute(query)



# %%

query = """MSCK REPAIR TABLE {0}.sbb_orc""".format(username)
cur.execute(query)
print(cur.fetch_logs())

# %%

query = """SHOW PARTITIONS {0}.sbb_orc""".format(username)
cur.execute(query)
pd.read_sql(query, conn)


# %%
query = """SELECT * FROM {0}.sbb_orc WHERE year=2019 LIMIT 5""".format(username)
pd.read_sql(query, conn)


# %% [markdown]
# **Checkpoint**
#
# Run the cells below and verify that your table satisfies all the required properties

# %%
query = """
DESCRIBE {0}.sbb_orc
""".format(username)
cur.execute(query)
cur.fetchall()

# %% [markdown]
# We have partitioned the database into 49 distinct partions.
# %%
query = """
SHOW PARTITIONS {0}.sbb_orc
""".format(username)
cur.execute(query)
partitions = cur.fetchall()
print(len(partitions))

# %% [markdown]
# ### b) Type of transport - 5/40
#
# In the exercise of week-3, you have already explored the stop distribution of different types of transport on a small data set. Now, let's do the same for a full two years worth of data.
#
# - Query `sbb_orc` to get the total number of stops for different types of transport in each month of 2019 and 2020, and order it by time and type of transport.
# |month_year|ttype|stops|
# |---|---|---|
# |...|...|...|
# - Use `plotly` to create a facet bar chart partitioned by the type of transportation. 
# - Document any patterns or abnormalities you can find.
#
# __Note__: 
# - In general, one entry in the `sbb_orc` table means one stop.
# - You might need to filter out the rows where:
#     - `BETRIEBSTAG` is not in the format of `__.__.____`
#     - `PRODUKT_ID` is NULL or empty
# - Facet plot with plotly: https://plotly.com/python/facet-plots/

# %%

query = """

    SELECT count(*) as count_stops, year, month, lower(produkt_id) as produkt_id
    FROM {0}.sbb_orc 
    WHERE 
    (year = 2019 
    or year = 2020) 
    and BETRIEBSTAG like '__.__.____'
    and PRODUKT_ID is not null
    and PRODUKT_ID <> ''
    GROUP BY month, year, lower(PRODUKT_ID)
    ORDER BY cast(year as int), cast(month as int), produkt_id ASC
    
""".format(username)
df_ttype = pd.read_sql(query, conn)

# %%
print(df_ttype[0:30])

# %%
len(df_ttype)

# %%
prod_id_list = list(set(df_ttype.produkt_id))
prod_id_list

# %%

fig = px.bar(
    df_ttype,
    x="month",y="count_stops",color="year",facet_row="produkt_id",text="year",
    facet_row_spacing=0.01, height=2000, title='Distribution of Transports'
)

fig.update_yaxes(matches=None)
# TODO: make your figure more readable

fig.show()

# %% [markdown]
# Firstly both for metro and zahnradbahn, data is missing from 2019. 
# One pattern that can be observered is a change of travel patterns during the summer. Use of metro
# train, tram and bus are significantly less than other months, while Zahnradbahn and Schliff have increased traffic.
# This can most likely be explained by many professionals taking holiday. 
#   
# One other notable change year over year is fewer stops in April of 2020 comapred to Mars of 2020. This is probably
# because of covid-19 and which casued fewer people to travel and the number of stops being reduced. This is especially apparent for Schliff,
# where during April and May 2020, no stops were made. 
#
# A third interesting pattern that can be observed using the visualization
# is that the number of bus stops have beens gradually increasing over time. 

# %% [markdown]
# ### c) Schedule - 10/40
#
# - Select a any day on a typical week day (not Saturday, not Sunday, not a bank holiday) from `sbb_orc`. Query the table for that one-day and get the set of IC (`VERKEHRSMITTEL_TEXT`) trains you can take to go (without connections) from Genève to Lausanne on that day. 
# - Display the train number (`LINIEN_ID`) as well as the schedule (arrival and departure time) of the trains.
#
# |train_number|departure|arrival|
# |---|---|---|
# |...|...|...|
#
# __Note:__ 
# - The schedule of IC from Genève to Lausanne has not changed for the past few years. You can use the advanced search of SBB's website to check your answer.
# - Do not hesitate to create intermediary tables or views (see [_CTAS_](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-CreateTableAsSelect(CTAS)))
# - You might need to add filters on these flags: `ZUSATZFAHRT_TF`, `FAELLT_AUS_TF`, `DURCHFAHRT_TF` 
# - Functions that could be useful: `unix_timestamp`, `to_utc_timestamp`, `date_format`.

# %% [markdown]
# Create two intermediary tables for the same day (06/05/2019) and for trains (`VERKEHRSMITTEL_TEXT` == 'IC') that stop in Lausanne and Genève respectively.
#
# Also filtering that the type of transport of the stop is IC and, and in the last condition that the train did actually stopped there.
#
# We have also filtered for the corresponding partition of the date in order to optimize the access to the data.

# %%
query = """
DROP TABLE IF EXISTS {0}.sbb_06_05_19_lau
""".format(username)
cur.execute(query)

query = """
DROP TABLE IF EXISTS {0}.sbb_06_05_19_gen
""".format(username)
cur.execute(query)

# You may need more than one query, do not hesitate to create more

query_lau = """

    CREATE TABLE {0}.sbb_06_05_19_lau
        STORED AS orc
        AS
    SELECT *
    FROM {0}.sbb_orc
    WHERE (year = 2019 and month = 5)
    and VERKEHRSMITTEL_TEXT like 'IC'
    and HALTESTELLEN_NAME like 'Lausanne'
    and BETRIEBSTAG = '06.05.2019'
    and FAELLT_AUS_TF is FALSE and DURCHFAHRT_TF is FALSE

""".format(username)
cur.execute(query_lau)

query_gen = """

    CREATE TABLE {0}.sbb_06_05_19_gen
        STORED AS orc
        AS
    SELECT *
    FROM {0}.sbb_orc
    WHERE (year = 2019 and month = 5)
    and VERKEHRSMITTEL_TEXT like 'IC'
    and HALTESTELLEN_NAME like 'Gen_ve'
    and BETRIEBSTAG = '06.05.2019'
    and FAELLT_AUS_TF is FALSE and DURCHFAHRT_TF is FALSE

""".format(username)
cur.execute(query_gen)

# %% [markdown]
# Here we use the two intermediary tables we have just created filtering that the time of departure from Genève has happened before the arrival time in Lausanne. In order to do it, we have had to cast from String format dates to UNIX Timestamp format.
#
# And of course, we have checked that it is the same train (train id = `FAHRT_BEZEICHNER`) in both stops.

# %%
query = """

    SELECT DISTINCT lau.LINIEN_ID as train_number, 
        gen.ABFAHRTSZEIT as departure, 
        lau.ANKUNFTSZEIT as arrival
    FROM {0}.sbb_06_05_19_gen as gen, {0}.sbb_06_05_19_lau as lau
    WHERE gen.FAHRT_BEZEICHNER = lau.FAHRT_BEZEICHNER
    and gen.ABFAHRTSZEIT <> '' and lau.ANKUNFTSZEIT <> ''
    and unix_timestamp(gen.ABFAHRTSZEIT, 'dd.MM.yyyy HH:mm') < unix_timestamp(lau.ANKUNFTSZEIT, 'dd.MM.yyyy HH:mm')
    order by departure
    
""".format(username)
df_genlau = pd.read_sql(query,conn)

# %%
df_genlau

# %% [markdown]
# As we can check in the SBB webpage, our results match with the regular schedule.

# %% [markdown]
# ### d) Delay percentiles - 10/40
#
# - Query `sbb_orc` to compute the 50th and 75th percentiles of __arrival__ delays for IC 702, 704, ..., 728, 730 (15 trains total) at Genève main station. 
# - Use `plotly` to plot your results in a proper way. 
# - Which trains are the most disrupted? Can you find the tendency and interpret?
#
# __Note:__
# - Do not hesitate to create intermediary tables. 
# - When the train is ahead of schedule, count this as a delay of 0.
# - Use only stops with `AN_PROGNOSE_STATUS` equal to __REAL__ or __GESCHAETZT__.
# - Functions that may be useful: `unix_timestamp`, `percentile_approx`, `if`

# %%
import plotly.graph_objects as go
import plotly.express as px

# %%
# You may need more than one query, do not hesitate to create more



# %%
query="""
CREATE TABLE IF NOT EXISTS {0}.sbb_delay
    STORED AS ORC
    AS (
        SELECT linien_id AS train_number,
               IF (unix_timestamp(an_prognose, 'dd.MM.yyy HH:mm:ss') > unix_timestamp(ankunftszeit, 'dd.MM.yyy HH:mm'),
               unix_timestamp(an_prognose, 'dd.MM.yyy HH:mm:ss')- unix_timestamp(ankunftszeit, 'dd.MM.yyy HH:mm'), 0) AS DELAY
        FROM {0}.sbb_orc
        WHERE haltestellen_name like 'Gen_ve'
        AND upper(an_prognose_status) IN ('REAL', 'GESCHAETZT')
        AND upper(verkehrsmittel_text) = 'IC'
        AND linien_id IN (702, 704, 706, 708, 710, 712, 714, 716, 718, 720, 722, 724, 726, 728, 730)
    )
""".format(username)
cur.execute(query)

# %%
query = """
    SELECT train_number,
           percentile_approx(DELAY, 0.5)  AS 50th_percentile,
           percentile_approx(DELAY, 0.75) AS 75th_percentile
    FROM {0}.sbb_delay
    GROUP BY train_number
    ORDER BY train_number
""".format(username)
df_delays_ic_gen = pd.read_sql(query, conn)

#%%
plot_df = df_delays_ic_gen
plot_df

# %%

fig = px.bar(
    plot_df, x="train_number", y=['50th_percentile', '75th_percentile'],
    title="Percentiles of arrival delays for IC trains in Geneva",
    barmode="group"
)

# Which trains are the most distruped? Can you find the tendency and interpret?

fig.show()

# %% [markdown]
## Comment : We notice that the trains with the most delays are those of the morning and the evening, 
# as the IC codes follow the order of the day (train 704 arrives in Geneva around 8:30 for example and train 726 arrives in Geneva around 19:20).
# This can be explained by the morning and evening commuting that fills the trains. 
# People go to work early in the morning and arrive back at the end of the day.
# However with this in mind the actual cause of the delays, whether it is a higher account of accidents due to overcrowding or something else remains unclear.


# %% [markdown]
# ### e) Delay heatmap 10/40
#
# - For each week (1 to 52) of each year from 2019 to 2021, query `sbb_orc` to compute the median of delays of all trains __departing__ from any train stations in Zürich area during that week. 
# - Use `plotly` to draw a heatmap year x week (year columns x week rows) of the median delays. 
# - In which weeks were the trains delayed the most/least? Can you explain the results?
#
# __Note:__
# - Do not hesitate to create intermediary tables. 
# - When the train is ahead of schedule, count this as a delay of 0 (no negative delays).
# - Use only stops with `AB_PROGNOSE_STATUS` equal to __REAL__ or __GESCHAETZT__.
# - For simplicty, a train station in Zürich area <=> it's a train station & its `HALTESTELLEN_NAME` starts with __Zürich__.
# - Heatmap with `plotly`: https://plotly.com/python/heatmaps/
# - Functions that may be useful: `unix_timestamp`, `from_unixtime`, `weekofyear`, `percentile_approx`, `if`


# %%

query = """

    WITH delays AS (SELECT 
        FAHRT_BEZEICHNER as id,
        haltestellen_name as stop,
        weekofyear(from_unixtime(unix_timestamp(BETRIEBSTAG, "dd.MM.yyyy"))) as weekofyear,
        greatest((unix_timestamp(AB_PROGNOSE, "dd.MM.yyyy HH:mm:ss") - unix_timestamp(ABFAHRTSZEIT, "dd.MM.yyyy HH:mm")),0) as delay_seconds,
        year
    FROM {0}.sbb_orc
    WHERE (year = 2018 or year = 2019 or year = 2020 or year = 2021) AND
    produkt_id = 'Zug' AND
    haltestellen_name like "Zürich%" AND
    (ab_prognose_status = 'REAL' OR ab_prognose_status = 'GESCHAETZT')
    )


    SELECT max(weekofyear) as week, max(year) as year, percentile(cast(delay_seconds as int), 0.5) as median_delay, count(*) as n_journeys
    FROM delays
    GROUP BY year, weekofyear
    ORDER BY year, cast(week as int)


""".format(username)
df_delays_zurich = pd.read_sql(query, conn)

    # SELECT max(weekofyear)
    # FROM delays
    # GROUP BY weekofyear

# %%
df_delays_zurich

# %%
delays_pivoted = df_delays_zurich.pivot(index="week", columns="year", values="median_delay")
fig = px.imshow(delays_pivoted,
                labels=dict(x="Year", y="Week", color="Median delay"),
                width=600,
                height=600
               )
fig.update_xaxes(side="top")
fig.show()
# %% [markdown]
# In which weeks were the trains delayed the most/least? Can you explain the results?
# -----
# The trains were significantly less delayed during the period between week 12 and 70 during 2020 as well as the 
# during the period between week 50 and 52 during 2021. This can probably be explained by covid-19 lockdowns which
# reduced the number of travellers which as a second order effect reduced delays.
# 
# Conversely, the median delay was the highest during the second half of 2019. While we cannot identify any direct
# causes, this could potentially be a consequence of gradually raising number of travellers, constructions of railways,
# and weather that promotes travelling by train. However, this would have to be supported by additional data.
# This part of the year is also a busy work season when people travel between the major cities of Switzerland including Zurich. 


# %% [markdown]
# ## Part II: Twitter Data (20 Points)
#
# Data source: https://archive.org/details/twitterstream?sort=-publicdate 
#
# In this part, you will leverage Hive to extract the hashtags from the source data, and then perform light exploration of the prepared data. 
#
# ### Dataset Description 
#
# Format: the dataset is presented as a collection of textfiles containing one JSON document per line. The data is organized in a hierarchy of folders, with one file per minute. The textfiles have been compressed using bzip2. In this part, we will mainly focus on __2016 twitter data__.
#
# Location: you can find the data on HDFS at the path `/data/twitter/json/year={year}/month={month}/day={day}/{hour}/{minute}.json.bz2`. 
#
# Relevant fields: 
# - `created_at`, `timestamp_ms`: The first is a human-readable string representation of when the tweet was posted. The latter represents the same instant as a timestamp since UNIX epoch.
# - `lang`: the language of the tweet content 
# - `entities`: parsed entities from the tweet, e.g. hashtags, user mentions, URLs.
# - In this repository, you can find [a tweet example](../data/tweet-example.json).
#
# Note:  Pay attention to the time units! and check the Date-Time functions in the Hive [_UDF_](https://cwiki.apache.org/confluence/display/hive/Languagemanual+udf#LanguageManualUDF-DateFunctions) documentation.

# %% [markdown]
# <div style="font-size: 100%" class="alert alert-block alert-danger">
#     <b>Disclaimer</b>
#     <br>
#     This dataset contains unfiltered data from Twitter. As such, you may be exposed to tweets/hashtags containing vulgarities, references to sexual acts, drug usage, etc.
#     </div>

# %% [markdown]
# ### a) JsonSerDe - 4/20
#
# In the exercise of week 4, you have already seen how to use the [SerDe framework](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-RowFormats&SerDe) to extract JSON fields from raw text format. 
#
# In this question, please use SerDe to create an <font color="red" size="3px">EXTERNAL</font> table with __one day__ (e.g. 01.07.2016) of twitter data. You only need to extract three columns: `timestamp_ms`, `lang` and `entities`(with the field `hashtags` only) with following schema (you need to figure out what to fill in `TODO`):
# ```
# timestamp_ms string,
# lang         string,
# entities     struct<hashtags:array<...<text:..., indices:...>>>
# ```
#
# The table you create should be similar to:
#
# | timestamp_ms | lang | entities |
# |---|---|---|
# | 1234567890001 | en | {"hashtags":[]} |
# | 1234567890002 | fr | {"hashtags":[{"text":"hashtag1","indices":[10]}]} |
# | 1234567890002 | jp | {"hashtags":[{"text":"hashtag1","indices":[14,23]}, {"text":"hashtag2","indices":[45]}]} |
#
# __Note:__
#    - JsonSerDe: https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-RowFormats&SerDe
#    - Hive data types: https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Types#LanguageManualTypes
#    - Hive complex types: https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Types#LanguageManualTypes-ComplexTypes

# %%
# Questions: What do do wiht nulls everywhere

# %%
# %%time
query="""
    DROP TABLE IF EXISTS {0}.twitter_hashtags
""".format(username)
cur.execute(query)

query="""
    CREATE EXTERNAL TABLE {0}.twitter_hashtags(
        timestamp_ms string,
        lang         string,
        entities     struct<hashtags:array<struct<text:string, indices:array<int>>>>
    )
    PARTITIONED BY (year STRING, month STRING, day STRING)
    ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
    STORED AS TEXTFILE
    location '/data/twitter/json'
    tblproperties ("skip.header.line.count"="1")
""".format(username)
cur.execute(query)

# %%
# %%time
query = """
    MSCK REPAIR TABLE {0}.twitter_hashtags
""".format(username)
cur.execute(query)
# pd.read_sql(query, conn)

# %%
# %%time

query="""
    SELECT * 
    
    FROM {0}.twitter_hashtags
    
    WHERE
        year=2016 AND month=07 AND day=01    
    LIMIT 15
""".format(username)
pd.read_sql(query, conn)

# %% [markdown]
# ### b) Explosion - 4/20
#
# In a), you created a table where each row could contain a list of multiple hashtags. Create another table **containing one day of data only** by normalizing the table obtained from the previous step. This means that each row should contain exactly one hashtag. Include `timestamp_ms` and `lang` in the resulting table, as shown below.
#
# | timestamp_ms | lang | hashtag |
# |---|---|---|
# | 1234567890001 | es | hashtag1 |
# | 1234567890001 | es | hashtag2 |
# | 1234567890002 | en | hashtag2 |
# | 1234567890003 | zh | hashtag3 |
#
# __Note:__
#    - `LateralView`: https://cwiki.apache.org/confluence/display/Hive/LanguageManual+LateralView
#    - `explode` function: <https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-explode>

# %%
# %%time
query="""
    DROP TABLE IF EXISTS {0}.twitter_hashtags_norm
""".format(username)
cur.execute(query)

query="""
    CREATE TABLE IF NOT EXISTS {0}.twitter_hashtags_norm
    STORED AS ORC
    AS  
        (
            SELECT timestamp_ms, lang, hashtag
            FROM {0}.twitter_hashtags
            LATERAL VIEW explode(entities.hashtags.text) exploded_hashtags as hashtag
            WHERE year=2016 AND month=07 AND day=01
        )
        
""".format(username)
cur.execute(query)

# %%
query="""
    DESCRIBE {0}.twitter_hashtags_norm
""".format(username)
pd.read_sql(query, conn)

# %%
query="""
    SELECT * FROM {0}.twitter_hashtags_norm LIMIT 10
""".format(username)
pd.read_sql(query, conn)

# %% [markdown]
# ### c) Hashtags - 8/20
#
# Query the normailized table you obtained in b). Create a table of the top 20 most mentioned hashtags with the contribution of each language. And, for each hashtag, order languages by their contributions. You should have a table similar to:
#
# |hashtag|lang|lang_count|total_count|
# |---|---|---|---|
# |hashtag_1|en|2000|3500|
# |hashtag_1|fr|1000|3500|
# |hashtag_1|jp|500|3500|
# |hashtag_2|te|500|500|
#
# Use `plotly` to create a stacked bar chart to show the results.
#
# __Note:__ to properly order the bars, you may need:
# ```python
# fig.update_layout(xaxis_categoryorder = 'total descending')
# ```

# %%
# %%time
query="""    
    SELECT a.hashtag as hashtag, lang, count(*) as lang_count, total_count
    FROM {0}.twitter_hashtags_norm as a
    join (
        SELECT hashtag, count(*) as total_count
        FROM {0}.twitter_hashtags_norm
        GROUP BY hashtag
        ORDER BY total_count DESC
    ) as b on a.hashtag = b.hashtag
    GROUP BY a.hashtag, lang, b.total_count
    ORDER BY total_count DESC
    
""".format(username)

df_hashtag = pd.read_sql(query, conn)
df_hashtag

# %%
fig = px.bar(
    df_hashtag,
    x = 'hashtag',
    y = 'lang_count',
    color= 'lang',
    hover_name = 'hashtag',
    hover_data = ['lang', 'lang_count'], #add percentage of total count
    title = 'Most used hashtags on 2016-07-01 broken down by language',
    labels={
             "hashtag": "Hashtag",
             "lang_count": "#Occurences",
             "lang": "Language"
        
            },

)

fig.update_layout(xaxis_categoryorder = 'total descending')

fig.show()

# %% [markdown]
# ### d) HBase - 4/20
#
# In the lecture and exercise of week-4, you have learnt what's HBase, how to create an Hbase table and how to create an external Hive table on top of the HBase table. Now, let's try to save the results of question c) into HBase, such that each entry looks like:
# ```
# (b'PIE', {b'cf1:total_count': b'31415926', b'cf2:langs': b'ja,en,ko,fr'})
# ``` 
# where the key is the hashtag, `total_count` is the total count of the hashtag, and `langs` is a string of  unique language abbreviations concatenated with commas. 
#
# __Note:__
# - To accomplish the task, you need to follow these steps:
#     - Create an Hbase table called `twitter_hbase`, in **your hbase namespace**, with two column families and fields (cf1, cf2)
#     - Create an external Hive table called `twitter_hive_on_hbase` on top of the Hbase table. 
#     - Populate the HBase table with the results of question c).
# - You may find function `concat_ws` and `collect_list` useful.

# %%
import happybase
hbaseaddr = os.environ['HBASE_SERVER']
hbase_connection = happybase.Connection(hbaseaddr, transport='framed',protocol='compact')

# %% tags=[]
try:
    hbase_connection.delete_table('{0}:twitter_hbase'.format(username),disable=True)
except Exception as e:
    print(e.message)
    pass

# %%
hbase_connection.create_table(
    '{0}:twitter_hbase'.format(username),
    {'cf1': dict(),
     'cf2': dict()
    }
)

# %%
query = """
DROP TABLE {0}.twitter_hive_on_hbase
""".format(username)
cur.execute(query)

# %%
query = """
CREATE EXTERNAL TABLE {0}.twitter_hive_on_hbase(
    RowKey STRING,
    total_count BIGINT,
    langs STRING

)
STORED BY 'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES (
    "hbase.columns.mapping"=":key,cf1:total_count,cf2:langs"
)
TBLPROPERTIES(
    "hbase.table.name"="{0}:twitter_hbase",
    "hbase.mapred.output.outputtable"="{0}:twitter_hbase"
)
""".format(username)
cur.execute(query)

# %%
# %%time
query="""
INSERT OVERWRITE TABLE {0}.twitter_hive_on_hbase
    select
         hashtag as RowKey,
         count(*) as total_count,
         concat_ws(',', collect_set(lang)) as langs
    FROM {0}.twitter_hashtags_norm
    GROUP BY hashtag
""".format(username)
#double check sort array works as expected
cur.execute(query)

# %%
from itertools import islice
for r in islice(hbase_connection.table('{0}:twitter_hbase'.format(username)).scan(),10):
    print(r)

# %% [markdown]
# # That's all, folks!
