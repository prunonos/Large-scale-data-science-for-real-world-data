# -*- coding: utf-8 -*-
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
# # Widgets with Voila interface
#
# This environment comes with the Voilà framework.
#
# Voilà can be used to run, convert, and serve a Jupyter notebook as a standalone webapp.
#
# This simple notebook illustrate how it can be used to serve results via a web interface to an audience who is not familiar with jupyter notebooks.

# %% [markdown]
# ----
# We will use data from the COVID updates in Switzerland.

# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    'https://raw.githubusercontent.com/openZH/covid_19/master/COVID19_Fallzahlen_CH_total_v2.csv',
    usecols=['abbreviation_canton_and_fl',
              'date',      
              'ncumul_conf',
              'current_hosp',
              'current_icu',
              'ncumul_deceased',
             ],
    parse_dates=['date'],
    index_col=['date']
).sort_index(ascending=True).dropna()
df.rename(columns={"abbreviation_canton_and_fl":"canton"},inplace=True)

# %%
df[:5]

# %% [markdown]
# This data shows daily COVID statistics for each canton in Switzerland
# * Create a list _cantons_ of all the Swiss cantons that have at least one value in this data. The list must be sorted and contain no duplicates

# %%
#TODO
import numpy as np

df_covid = df[df.ncumul_conf > 0]
cantons = np.unique((df_covid.sort_values('ncumul_conf',ascending=False)).canton)

# %% [markdown]
# Create an interactive plot using ipywidgets as seen in the previous set of exercises.
#
# * The interface must allow you to choose a canton, the value to measure and averaging windows of 1 day, 7 days or 14 days
#
# Method:
# * Pivot dataframe _df_ around the cantons columns
# * Use the dataframe resample method (daily)
# * Compute the mean of each sample
# * Select the canton specified by the user
#
# Once you have a plot, open a new tab in your browser, replacing `/lab` in the URL by `/voila/render/notebooks/DSLab_week2-4.ipynb`

# %%
from ipywidgets import interact

@interact(Canton=cantons,Values=df.columns.to_list()[1:],J=[1,7,14])
def plot(Canton='VD',Values='current_hosp',J=7):
    # TODO
    print(df.pivot(columns='canton',values=Values).resample(str(J)+'D').mean().columns)
    df.pivot(columns='canton',values=Values).resample(str(J)+'D').mean()[Canton].plot(figsize=(10,10),legend=False)


# %%
df.pivot(columns='canton',values=df.columns.to_list()).resample('14D').mean().ncumul_conf.AG
