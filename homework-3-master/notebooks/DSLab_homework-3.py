# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # DSLab Homework3 - Uncovering World Events using Twitter Hashtags
#
# ## ... and learning about Spark `DataFrames` along the way
#
# In this notebook, we will use temporal information about Twitter hashtags to discover trending topics and potentially uncover world events as they occurred. 
#
# ## Hand-in Instructions:
#
# - __Due: 26.04.2022 23:59:59 CET__
# - your project must be private
# - `git push` your final verion to the master branch of your group's Renku repository before the due date
# - check if `Dockerfile`, `environment.yml` and `requirements.txt` are properly written
# - add necessary comments and discussion to make your codes readable

# %% [markdown]
# ## Hashtags
#
# The idea here is that when an event is happening and people are having a conversation about it on Twitter, a set of uniform hashtags that represent the event spontaneously evolves. Twitter users then use those hashtags to communicate with one another. Some hashtags, like `#RT` for "retweet" or just `#retweet` are used frequently and don't tell us much about what is going on. But a sudden appearance of a hashtag like `#oscars` probably indicates that the oscars are underway. For a particularly cool example of this type of analysis, check out [this blog post about earthquake detection using Twitter data](https://blog.twitter.com/official/en_us/a/2015/usgs-twitter-data-earthquake-detection.html) (although they search the text and not necessarily hashtags).

# %% [markdown]
# ## Initialize the environment

# %%
# %load_ext sparkmagic.magics

# %%
import os
from IPython import get_ipython
username = os.environ['RENKU_USERNAME']
server = "http://iccluster029.iccluster.epfl.ch:8998"

# set the application name as "<your_gaspar_id>-homework3"
get_ipython().run_cell_magic(
    'spark',
    line='config', 
    cell="""{{ "name": "{0}-homework3", "executorMemory": "4G", "executorCores": 4, "numExecutors": 10, "driverMemory": "4G"}}""".format(username)
)

# %% [markdown]
# Send `username` to Saprk kernel, which will frist start the Spark application if there is no active session.

# %%
get_ipython().run_line_magic(
    "spark", "add -s {0}-homework3 -l python -u {1} -k".format(username, server)
)

# %% language="spark"
# print('We are using Spark %s' % spark.version)

# %%
# %%spark?

# %% [markdown]
# ## PART I: Set up (5 points)
#
# The twitter stream data is downloaded from [Archive Team: The Twitter Stream Grab](https://archive.org/details/twitterstream), which is a collection of a random sample of all tweets. We have parsed the stream data and prepared the twitter hashtag data of __2020__, a very special and different year in many ways. Let's see if we can see any trends about all these events of 2020 in the Twitter data. 
#
# <div style="font-size: 100%" class="alert alert-block alert-danger">
# <b>Disclaimer</b>
# <br>
# This dataset contains unfiltered data from Twitter. As such, you may be exposed to tweets/hashtags containing vulgarities, references to sexual acts, drug usage, etc.
# </div>

# %% [markdown]
# ### a) Load data - 1/10
#
# Load the **orc** data from `/data/twitter/orc/hashtags/year=2020` into a Spark dataframe using the appropriate `SparkSession` method. 
#
# Look at the first few rows of the dataset - note the timestamp and its units!

# %% language="spark"
# df = spark.read.orc('/data/twitter/part_orc/hashtags/year=2020')
# df.printSchema()

# %% language="spark"
# df.show(n=5, truncate=False, vertical=False)

# %% [markdown]
# <div style="font-size: 100%" class="alert alert-block alert-info">
#     <b>Cluster Usage:</b> As there are many of you working with the cluster, we encourage you to
#     <ul>
#         <li>prototype your queries on small data samples before running them on whole datasets</li>
#         <li>save your intermediate results in your own directory at hdfs <b>"/user/&lt;your-gaspar-id&gt;/"</b></li>
#     </ul>
# </div>
#
# For example:
#
# ```python
#     # create a subset of original dataset
#     df_sample = df.sample(0.01)
#     
#     # save as orc
#     df_sample.write.orc('/user/%s/sample.orc' % username, mode='overwrite')
#
# ```

# %% [markdown]
# ### b) Functions - 2/10

# %% language="spark"
# import pyspark.sql.functions as F

# %% [markdown]
# __User-defined functions__
#
# A neat trick of spark dataframes is that you can essentially use something very much like an RDD `map` method but without switching to the RDD. If you are familiar with database languages, this works very much like e.g. a user-defined function in SQL. 
#
# So, for example, if we wanted to make a user-defined python function that returns the hashtags in lowercase, we could do something like this:

# %% language="spark"
# @F.udf
# def lowercase(text):
#     """Convert text to lowercase"""
#     return text.lower()

# %% [markdown]
# The `@F.udf` is a "decorator" -- this is really handy python syntactic sugar and in this case is equivalent to:
#
# ```python
# def lowercase(text):
#     return text.lower()
#     
# lowercase = F.udf(lowercase)
# ```
#
# It basically takes our function and adds to its functionality. In this case, it registers our function as a pyspark dataframe user-defined function (UDF).
#
# Using these UDFs is very straightforward and analogous to other Spark dataframe operations. For example:

# %% language="spark"
# df.select(lowercase(df.hashtag)).show(n=5)

# %% [markdown]
# __Built-in functions__
#
# Using a framework like Spark is all about understanding the ins and outs of how it functions and knowing what it offers. One of the cool things about the dataframe API is that many functions are already defined for you (turning strings into lowercase being one of them). Find the [Spark python API documentation](https://spark.apache.org/docs/2.3.2/api/python/index.html). Look for the `sql` section and find the listing of `sql.functions`. Repeat the above (turning hashtags into lowercase) but use the built-in function.

# %% language="spark"
# df.select(F.lower(df.hashtag)).show(n=5)

# %% [markdown]
# We'll work with a combination of these built-in functions and user-defined functions for the remainder of this homework. 
#
# Note that the functions can be combined. Consider the following dataframe and its transformation:

# %% language="spark"
# from pyspark.sql import Row
#
# # create a sample dataframe with one column "degrees" going from 0 to 180
# test_df = spark.createDataFrame(spark.sparkContext.range(180).map(lambda x: Row(degrees=x)), ['degrees'])
#
# # define a function "sin_rad" that first converts degrees to radians and then takes the sine using built-in functions
# sin_rad = F.sin(F.radians(test_df.degrees))
#
# # show the result
# test_df.select(sin_rad).show()

# %% [markdown]
# ### c) Tweets in english - 2/10
#
# - Create `english_df` with only english-language tweets. 
# - Turn hashtags into lowercase.
# - Convert the timestamp to a more readable format and name the new column as `date`.
# - Sort the table in chronological order. 
#
# Your `english_df` should look something like this:
#
# ```
# +-----------+----+-----------+-------------------+
# |timestamp_s|lang|    hashtag|               date|
# +-----------+----+-----------+-------------------+
# | 1577862000|  en| spurfamily|2020-01-01 08:00:00|
# | 1577862000|  en|newyear2020|2020-01-01 08:00:00|
# | 1577862000|  en|     master|2020-01-01 08:00:00|
# | 1577862000|  en|  spurrific|2020-01-01 08:00:00|
# | 1577862000|  en|     master|2020-01-01 08:00:00|
# +-----------+----+-----------+-------------------+
# ```
#
# __Note:__ 
# - The hashtags may not be in english.
# - [pyspark.sql.functions](https://spark.apache.org/docs/2.3.2/api/python/pyspark.sql.html#module-pyspark.sql.functions)

# %% [markdown]
# Filter the dataframe to get only the tweets in English.

# %% language="spark"
# filtered_english_df = df.filter(df.lang == 'en')

# %% [markdown]
# Select the timestime, language, the hashtag in lowercase and the date in a readable format.

# %% language="spark"
# english_df = filtered_english_df.select(['timestamp_s', 
#                                          'lang', 
#                                          F.lower(filtered_english_df.hashtag).alias('hashtag'), 
#                                          F.from_unixtime(filtered_english_df.timestamp_s).alias('date')
#                                          ])

# %% [markdown]
# Sort the tweets by the date.

# %% language="spark"
# english_df = english_df.sort("date")

# %% language="spark"
# english_df.show(n=5)

# %% [markdown]
# We saved a sample of the English data to be able to test our functions in the future parts, however the sample datagrame was only used when testing our queries not in the final version of the notebook.

# %% language="spark"
# english_sample_df = english_df.sample(0.01)
# english_sample_df.write.orc('/user/%s/english_sample_df.orc' % "prunonos", mode='overwrite')

# %% [markdown]
# ## PART II: Twitter hashtag trends (30 points)
#
# In this section we will try to do a slightly more complicated analysis of the tweets. Our goal is to get an idea of tweet frequency as a function of time for certain hashtags. 
#
# Have a look [here](http://spark.apache.org/docs/2.3.2/api/python/pyspark.sql.html#module-pyspark.sql.functions) to see the whole list of custom dataframe functions - you will need to use them to complete the next set of TODO items.

# %% language="spark"
# english_sample_df = spark.read.orc('/user/%s/english_sample_df.orc' % "prunonos")

# %% [markdown]
# ### a) Top hashtags - 1/30
#
# We used `groupBy` already in the previous notebooks, but here we will take more advantage of its features. 
#
# One important thing to note is that unlike other RDD or DataFrame transformations, the `groupBy` does not return another DataFrame, but a `GroupedData` object instead, with its own methods. These methods allow you to do various transformations and aggregations on the data of the grouped rows. 
#
# Conceptually the procedure is a lot like this:
#
# ![groupby](https://i.stack.imgur.com/sgCn1.jpg)
#
# The column that is used for the `groupBy` is the `key` - once we have the values of a particular key all together, we can use various aggregation functions on them to generate a transformed dataset. In this example, the aggregation function is a simple `sum`. In the simple procedure below, the `key` will be the hashtag.
#
#
# Use `groupBy`, calculate the top 5 most common hashtags in the whole english-language dataset.
#
# This should be your result:
#
# ```
# +-----------------+-------+
# |          hashtag|  count|
# +-----------------+-------+
# |              bts|1200196|
# |          endsars|1019280|
# |          covid19| 717238|
# |            방탄소년단| 488160|
# |sarkaruvaaripaata| 480124|
# +-----------------+-------+
# ```

# %% [markdown]
# Calculate the count of each hashtag, taking the top 5 counts and caching the results.
#
# We output the top 5 hashtags to the Python environment to be able to use as a Pandas dataframe.

# %% magic_args="-o top_hashtags" language="spark"
# top_hashtags = (english_df.groupBy("hashtag")
#                           .count()
#                           .orderBy('count', ascending=False)
#                           .limit(5)
#                           .cache())
# top_hashtags.show() 

# %% [markdown]
# We also saved it as a local pandas dataframe

# %%
type(top_hashtags)

# %%
top_hashtags.head()

# %% [markdown]
# ### b) Daily hashtags - 2/50
#
# Now, let's see how we can start to organize the tweets by their timestamps. Remember, our goal is to uncover trending topics on a timescale of a few days. A much needed column then is simply `day`. Spark provides us with some handy built-in dataframe functions that are made for transforming date and time fields.
#
# - Create a dataframe called `daily_hashtag` that includes the columns `month`, `week`, `day` and `hashtag`. 
# - Use the `english_df` you made above to start, and make sure you find the appropriate spark dataframe functions to make your life easier. For example, to convert the date string into day-of-year, you can use the built-in [dayofyear](http://spark.apache.org/docs/2.3.2/api/python/pyspark.sql.html#pyspark.sql.functions.dayofyear) function. 
# - For the simplicity of following analysis, filter only tweets of 2020.
# - Show the result.
#
# Try to match this view:
#
# ```
# +-----+----+---+-----------+
# |month|week|day|    hashtag|
# +-----+----+---+-----------+
# |    1|   1|  1| spurfamily|
# |    1|   1|  1|newyear2020|
# |    1|   1|  1|     master|
# |    1|   1|  1|  spurrific|
# |    1|   1|  1|     master|
# +-----+----+---+-----------+
# ```

# %% [markdown]
# Filter to take only tweets of 2020 and we get the month, week of the year and day of the year numbers.

# %% language="spark"
# daily_hashtag = (english_df.filter(F.year('date') == 2020)
#                            .select([F.month('date').alias('month'),
#                                     F.weekofyear('date').alias('week'),
#                                     F.dayofyear('date').alias('day'),
#                                     'hashtag'
#                                     ]))

# %% language="spark"
# daily_hashtag.show(n=5)

# %% [markdown]
# Once again, we save a sample of the df to test future parts.

# %% language="spark"
# daily_hashtag_sample = daily_hashtag.sample(0.01)
# daily_hashtag_sample.write.orc('/user/%s/daily_hashtag_sample.orc' % "prunonos", mode='overwrite')

# %% language="spark"
# daily_hashtag_sample = spark.read.orc('/user/%s/daily_hashtag_sample.orc' % "prunonos")

# %% [markdown]
# ### c) Daily counts - 2/50
#
# Now we want to calculate the number of times a hashtag is used per day based on the dataframe `daily_hashtag`. Sort in descending order of daily counts and show the result. Call the resulting dataframe `day_counts`.
#
# Your output should look like this:
#
# ```
# +---+----------------------+----+------+
# |day|hashtag               |week|count |
# +---+----------------------+----+------+
# |229|pawankalyanbirthdaycdp|33  |202241|
# |222|hbdmaheshbabu         |32  |195718|
# |228|pawankalyanbirthdaycdp|33  |152037|
# |357|100freeiphone12       |52  |122068|
# |221|hbdmaheshbabu         |32  |120401|
# +---+----------------------+----+------+
# ```
#
# <div class="alert alert-info">
# <p>Make sure you use <b>cache()</b> when you create <b>day_counts</b> because we will need it in the steps that follow!</p>
# </div>

# %% [markdown]
# Here we count the numer of times a hashtag is used per day using the results from the previous question.

# %% language="spark"
# day_counts = (daily_hashtag.groupBy(['day', 'hashtag'])
#                            .agg(F.first('week').alias('week'), 
#                                 F.count('hashtag').alias('count'))
#                            .orderBy('count', ascending=False)
#                            .cache())

# %% language="spark"
# day_counts.show(n=5, truncate=False)

# %% [markdown]
# ### d) Weekly average - 2/50
#
# To get an idea of which hashtags stay popular for several days, calculate the average number of daily occurences for each week. Sort in descending order and show the top 20.
#
# __Note:__
# - Use the `week` column we created above.
# - Calculate the weekly average using `F.mean(...)`.

# %% language="spark"
# (day_counts.groupBy(['week', 'hashtag'])
#            .agg(F.mean('count').alias('weekly_mean'))
#            .orderBy('weekly_mean', ascending=False)
#            .show(n=20))

# %% [markdown]
# ### e) Ranking - 3/20
#
# Window functions are another awesome feature of dataframes. They allow users to accomplish complex tasks using very concise and simple code. 
#
# Above we computed just the hashtag that had the most occurrences on *any* day. Now lets say we want to know the top tweets for *each* day.  
#
# This is a non-trivial thing to compute and requires "windowing" our data. I recommend reading this [window functions article](https://databricks.com/blog/2015/07/15/introducing-window-functions-in-spark-sql.html) to get acquainted with the idea. You can think of a window function as a fine-grained and more flexible `groupBy`. 
#
# There are two things we need to define to use window functions:
#
# 1. the "window" to use, based on which columns (partitioning) and how the rows should be ordered 
# 2. the computation to carry out for each windowed group, e.g. a max, an average etc.
#
# Lets see how this works by example. We will define a window function, `daily_window` that will partition data based on the `day` column. Within each window, the rows will be ordered by the daily hashtag count that we computed above. Finally, we will use the rank function **over** this window to give us the ranking of top tweets. 
#
# In the end, this is a fairly complicated operation achieved in just a few lines of code! (can you think of how to do this with an RDD??)

# %% language="spark"
# from pyspark.sql import Window

# %% [markdown]
# First, we specify the window function and the ordering:

# %% language="spark"
# daily_window = Window.partitionBy('day').orderBy(F.desc('count'))

# %% [markdown]
# The above window function says that we should window the data on the `day` column and order it by count. 
#
# Now we need to define what we want to compute on the windowed data. We will start by just calculating the daily ranking of hashtags, so we can use the helpful built-in `F.rank()` and sort:

# %% language="spark"
# daily_rank = (F.rank()
#                .over(daily_window)
#                .alias('rank'))

# %% [markdown]
# Now compute the top five hashtags for each day in our data:

# %% language="spark"
# (day_counts.withColumn("daily_rank", daily_rank)
#            .filter(F.col('daily_rank') <= 5)
#            .show())

# %% [markdown]
# ### f) Rolling sum - 5/30
#
# With window functions, you can also calculate the statistics of a rolling window. 
#
# In this question, construct a 7-day rolling window (including the day and 6 days before) to calculate the rolling sum of the daily occurences for each hashtag.
#
# Your results should be like:
# - For the hashtag `covid19`:
#
# ```
# +---+----+-----+-------+-----------+
# |day|week|count|hashtag|rolling_sum|
# +---+----+-----+-------+-----------+
# | 42|   7|   85|covid19|         85|
# | 43|   7|   94|covid19|        179|
# | 45|   7|  192|covid19|        371|
# | 46|   7|   97|covid19|        468|
# | 47|   7|  168|covid19|        636|
# | 48|   8|  317|covid19|        953|
# | 49|   8|  116|covid19|        984|
# | 51|   8|  234|covid19|       1124|
# | 52|   8|  197|covid19|       1129|
# | 53|   8|  369|covid19|       1401|
# +---+----+-----+-------+-----------+
# ```
#
# - For the hashtag `bts`:
#
# ```
# +---+----+-----+-------+-----------+
# |day|week|count|hashtag|rolling_sum|
# +---+----+-----+-------+-----------+
# |  1|   1| 2522|    bts|       2522|
# |  2|   1| 1341|    bts|       3863|
# |  3|   1|  471|    bts|       4334|
# |  4|   1|  763|    bts|       5097|
# |  5|   1| 2144|    bts|       7241|
# |  6|   2| 1394|    bts|       8635|
# |  7|   2| 1673|    bts|      10308|
# |  8|   2| 5694|    bts|      13480|
# |  9|   2| 5942|    bts|      18081|
# | 10|   2| 5392|    bts|      23002|
# +---+----+-----+-------+-----------+
# ```

# %% [markdown]
# Create a window previous of calculating the rolling sum, by partitioning by hashtag and taking the 6 previous days with the function `rangeBetween`.
#
# Then we calculate the rolling sum, by adding up the counts over the window. We also had to cache the resulting dataframe.

# %% language="spark"
# week_window = (Window.partitionBy('hashtag')
#                      .orderBy('day')
#                      .rangeBetween(-6, Window.currentRow))
# rs_counts = day_counts.withColumn('rolling_sum', F.sum('count').over(week_window)).cache()

# %% [markdown]
# Now we check the results for the rolling sum.

# %% language="spark"
# rs_counts.filter(F.col('hashtag') == 'covid19').show(n=10)

# %% language="spark"
# rs_counts.filter(F.col('hashtag') == 'bts').show(n=10)

# %% [markdown]
# ### g) DIY - 15/20
#
# Use window functions (or other techniques!) to produce lists of top few trending tweets for each week. What's a __"trending"__ tweet? Something that seems to be __suddenly growing very rapidly in popularity__. 
#
# You should be able to identify, for example, Oscars-related hashtags in week 7 when [the 92nd Academy Awards ceremony took place](https://www.oscars.org/oscars/ceremonies/2020), COVID-related hashtags in week 11 when [WHO declared COVID-19 a pandemic](https://www.who.int/director-general/speeches/detail/who-director-general-s-opening-remarks-at-the-media-briefing-on-covid-19---11-march-2020), and other events like the movement of Black Life Matters in late May, the United States presidential elections, the 2020 American Music Awards, etc.
#
# The final listing should be clear and concise and the flow of your analysis should be easy to follow. If you make an implementation that is not immediately obvious, make sure you provide comments either in markdown cells or in comments in the code itself.

# %% [markdown]
# We group by hashtag and week and then we take the amount of tweets where every hashtag appears every week

# %% language="spark"
# rs_count_week = (rs_counts.groupBy(['hashtag', 'week'])
#                           .agg(F.sum('count').alias('week_sum')))

# %% [markdown]
# Now we calculate (within every hashtag and for every week) the increase in the popularity of a hashtag compared to the previous week

# %% language="spark"
# window = Window.partitionBy('hashtag').orderBy('week')
# rs_trend_week = rs_count_week.withColumn('dif_week', F.col('week_sum') - F.lag('week_sum').over(window))

# %% [markdown]
# Now we order by the popularity of a hashtag partitionating by week

# %% language="spark"
# week_window = Window.partitionBy('week').orderBy(F.desc('dif_week'))
# week_rank = (F.rank()
#               .over(week_window)
#               .alias('rank'))

# %% [markdown]
# Determine the n most popular hashtags in a week by taking the first `n_top_hashtags` in a week.
#

# %% language="spark"
# n_top_hashtags = 5
# trending_tweets_week = (rs_trend_week.withColumn("rank", week_rank)
#                                      .filter(F.col('rank') <= n_top_hashtags)
#                                      .orderBy('week')
#                                      .select(['week',
#                                               'rank',
#                                               'hashtag',
#                                               F.col('dif_week').alias('trending'),
#                                               F.col('week_sum').alias('count_week')
#                                               ])
#                                      .cache())

# %% [markdown]
# During week 7 we expect the top trending hashtags to include hashtags about the Oscars Awards celebration.

# %% language="spark"
# trending_tweets_week.filter('week == 7').show()

# %% [markdown]
# During week 11 we expect the top trending hashtags to include hashtags about the Coronsvirus pandemic.

# %% language="spark"
# trending_tweets_week.filter('week == 11').show()

# %% [markdown]
# During week 22 we expect the top trending hashtags to include hashtags about the black lives matter movement.

# %% language="spark"
# trending_tweets_week.filter('week == 22').show()

# %% [markdown]
# During week 44 we expect the top trending hashtags to include hashtags about the American Music Awards.

# %% language="spark"
# trending_tweets_week.filter('week == 44').show()

# %% [markdown]
# During week 45 we expect the top trending hashtags to include hashtags about the American presidential elections.

# %% language="spark"
# trending_tweets_week.filter('week == 45').show()

# %% [markdown]
# ## PART III: Hashtag clustering (25 points)

# %% [markdown]
# ### a) Feature vector - 3/25
#
# - Create a dataframe `daily_hashtag_matrix` that consists of hashtags as rows and daily counts as columns (hint: use `groupBy` and methods of `GroupedData`). Each row of the matrix represents the time series of daily counts of one hashtag. Cache the result.
#
# - Create the feature vector which consists of daily counts using the [`VectorAssembler`](https://spark.apache.org/docs/2.3.2/api/python/pyspark.ml.html#pyspark.ml.feature.VectorAssembler) from the Spark ML library. Cache the result.

# %% language="spark"
# day_counts

# %% language="spark"
# sampled_counts = day_counts#.sample(0.001)
# daily_hashtag_matrix = sampled_counts.groupBy("hashtag").pivot("day").sum("count").cache()

# %% language="spark"
# from pyspark.ml.feature import VectorAssembler
#
# vecAssembler = VectorAssembler(inputCols=daily_hashtag_matrix.columns[1:], outputCol="features")
# daily_vector = vecAssembler.transform(daily_hashtag_matrix.na.fill(0))

# %% [markdown]
# ### b) Visualization - 2/25
#
# Visualize the time sereis you just created. 
#
# - Select a few interesting hashtags you identified above. `isin` method of DataFrame columns might be useful.
# - Retrieve the subset DataFrame using sparkmagic
# - Plot the time series for the chosen hashtags with matplotlib.

# %% magic_args="-o df_plot" language="spark"
# hashtags = ["oscars", "covid19", u"ajithkumar"] #todo 
# df_plot = daily_vector.filter((daily_vector.hashtag.isin(hashtags)))

# %%
df_plot.head()

# %%
# %matplotlib inline
import matplotlib.pyplot as plt

x_values = df_plot.columns[1:-1]

plt.figure(figsize=(12,8))   

for index, row in df_plot.iterrows():
     plt.plot(x_values, row["features"]["values"], label=row["hashtag"])

        

plt.xticks(df_plot.columns[1:-1:61])
plt.legend()
plt.xlabel('Day')
plt.ylabel('Nb of hashtags mentions')
plt.suptitle("Distribution over time of specific hashtags")
plt.show()


# %% [markdown]
# ### c) KMeans clustering - 20/25
#
# Use KMeans to cluster hashtags based on the daily count timeseries you created above. Train the model and calculate the cluster membership for all hashtags. Again, be creative and see if you can get meaningful hashtag groupings. 
#
# Validate your results by showing certain clusters, for example, those including some interesting hashtags you identified above. Do they make sense?
#
# Make sure you document each step of your process well so that your final notebook is easy to understand even if the result is not optimal or complete. 
#
# __Note:__ 
# - Additional data cleaning, feature engineering, deminsion reduction, etc. might be necessary to get meaningful results from the model. 
# - For available methods, check [pyspark.sql.functions documentation](https://spark.apache.org/docs/2.3.2/api/python/pyspark.sql.html#module-pyspark.sql.functions), [Spark MLlib Guide](https://spark.apache.org/docs/2.3.2/ml-guide.html) and [pyspark.ml documentation](https://spark.apache.org/docs/2.3.2/api/python/pyspark.ml.html).

# %%
import pandas as pd
import numpy as np
import seaborn as sns

def plot_interesting_clusters(clustered_hashtags_series):

    
    # Take out hashtag and predictions columns before melting
    hashtag_predictions = clustered_hashtags_series[["hashtag", "prediction"]]
    
    # Melts frequencies from each daily colum to rows [hashtag, day1, day2, ...] to [hashtag, date, freq]
    hashtags_data_molten = clustered_hashtags_series.drop(columns=["prediction"]).melt(id_vars=['hashtag'], var_name="date", value_name="freq")
    
    # Converts from day of year to an actual date
    hashtags_data_molten.date = pd.to_datetime(str(2020) + hashtags_data_molten['date'], format='%Y%j')

    # Resample and group by hashtag
    hashtags_data_molten = hashtags_data_molten.set_index('date').groupby('hashtag').resample('W').mean().reset_index()

    # Adds the column 'prediction' back to the dataframe
    complete_df = hashtags_data_molten.merge(hashtag_predictions, on="hashtag")
    
    
    plt.figure(figsize=(24, 18))
    
    
    # Get the clusters that contain more than 1 hashtag and less than 30
    clusters = hashtag_predictions.groupby("prediction").count().query("hashtag > 1 and hashtag < 30").reset_index()["prediction"]
    
    skipped_clusters = 0
    for index, cluster in enumerate(clusters):
        cluster_data = complete_df[complete_df['prediction'] == cluster]
        
        plt.subplot(len(clusters) // 2 + 1, 2, index + 1).set_title(f'Cluster {cluster}')
        sns.lineplot(data=cluster_data, x="date", y="freq", hue="hashtag",
                     estimator=None, units="hashtag",
                     lw=1,
                     alpha=1)
    
    
    plt.xlabel('Date')
    plt.ylabel('Hashtag usage')
    plt.suptitle("Frequency distribution of hashtag usage")
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1.0)
    plt.show()

# %% magic_args="-o clustered_hashtags_series" language="spark"
# # Baseline with 20 clusters
# from pyspark.ml.clustering import KMeans
# from pyspark.ml.evaluation import ClusteringEvaluator
#
# kmeans = KMeans().setK(20).setSeed(1)
# model = kmeans.fit(daily_vector.select("features"))
#
# predictions = model.transform(daily_vector)
#
# print(model.summary.clusterSizes)
#
# preds = predictions.select("hashtag", "prediction").filter("prediction != 0")
# clustered_hashtags_series = daily_vector.join(preds, daily_vector.hashtag == preds.hashtag, "inner")

# %% [markdown]
# We observe that it is really unbalanced, with more than 4M hashtags in the first cluster. 

# %%
plot_interesting_clusters(clustered_hashtags_series.drop(columns=["features"]))
###
# Plots the clusters with more than 1 but less than 30 contained hashtags 
# This amounts to 3 out of 20 clusters.

# %% language="spark"
# # Create column for the total sum of all days as well as a column for the value of the day with peak usage
# daily_vector_sum = daily_vector.withColumn('total', sum(daily_vector[col] for col in daily_vector.columns[1:-1]))
# daily_vector_sum = daily_vector_sum.withColumn('max_day', F.greatest(*[F.coalesce(F.col(x), F.lit(0)) for x in daily_vector_sum.columns[1:-2]]))
#
# # Filter out hashtags that are have too few values to create distinct frequency distributions 
# daily_vector_ml = daily_vector_sum.filter("total > 5000")
#
# # Filter out hashtags that are likely to be outliers
# daily_vector_ml = daily_vector_ml.filter("max_day < 10*total/365")
#

# %% language="spark"
# # Kmeans with 35 clusters
# kmeans = KMeans().setK(35).setSeed(1)
# model = kmeans.fit(daily_vector_ml.select("features"))
# predictions = model.transform(daily_vector_ml)

# %% language="spark"
#
# model.summary.k, model.summary.clusterSizes

# %% [markdown]
# With 35 clusters, we observe that it is better balanced. 

# %% magic_args="-o clustered_hashtags_series_processed" language="spark"
# # Filter out cluster 0 that contains the majority of hashtags.
# preds = predictions.select("hashtag", "prediction").filter("prediction != 0")
#
# # Create a df that will be used for plotting the frequency distributions for the clusters
# clustered_hashtags_series_processed = daily_vector.join(preds, daily_vector.hashtag == preds.hashtag, "inner")

# %%
import warnings
warnings.filterwarnings('ignore')

plot_interesting_clusters(clustered_hashtags_series_processed.drop(columns=["features"]))

# %% [markdown]
# When we prune the hashtags by removing unfrequently used hashtags and potential outliers as well as increase the number of clusters, more interesting clusters are created. 
#
# Some interesting clusters with semantically similar hashtags include cluster 15, with 'china' and 'covid' or cluster 20 with 'lockdown' and 'stayhome'.
# Apart from the covid related clusters, there is also the semantically similar cluster 27 with 'qanon' and wwg1wga' (WHERE WE GO ONE, WE GO ALL) and cluster 21 with 'astro', 'nuest' and the south korean name for nuest. All referring to a south korean band. 
#
#  There are also some clusters that doesn't seem to be semantically similar, like cluster 13. Which contains mainly overall popular tweets with a more or less flat distribution
#  over 2020. It includes hashtags such as 'trump', 'win' and 'bitcoin'.
#
#  While the processing and testing of different number of clusters improved the result, there are still many clusters with 1 and clusters with seemingly coincidental frequency distributions. However, with the number of hashtags in the dataset, this is to be expected.

# %% [markdown] tags=[]
# # That's all, folks!
