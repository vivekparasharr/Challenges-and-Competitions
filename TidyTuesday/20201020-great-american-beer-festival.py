# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:31:55 2020

@author: vivek
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
d = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-10-20/beer_awards.csv')
# m = pd.read_csv('us-census-bureau-regions.csv')
d.save()
d.head()
d.columns
# Index(['medal', 'beer_name', 'brewery', 'city', 'state', 'category', 'year'], dtype='object')
# Index(['State', 'State Code', 'Region', 'Division'], dtype='object')
# d.columns=['medal', 'beer_name', 'brewery', 'city', 'StateCode', 'category', 'year']
# m.columns=['State', 'StateCode', 'Region', 'Division']

d.info()
d.describe()
d.category.unique()

d[d.category.str.contains('American')][d.year>=2014][d.year<=2017]


t=d.groupby('state').count()[['medal']].sort_values(by=['medal'],ascending=False)
t2=t[t.medal>200]

d2=d[['year','state','medal']]

d3=d2.groupby(['year','state']).count().reset_index()
d4=d3.pivot("state", "year", "medal")
d4=d4.fillna(0)
# Load the example flights dataset and convert to long-form
flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(d4, annot=True,  linewidths=.5, ax=ax)

import pandas as pd
import seaborn as sns
d=pd.read_csv('d2.csv')
d.columns=['States', 'Years', 'Number of Medals', 'Region']
sns.relplot(data=d, kind='line',
            x='Years', y='Number of Medals', col='States', col_wrap=4,)



sns.set_theme(style="ticks", palette="pastel")

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested boxplot to show bills by day and time

sns.boxplot(x="States", y="Number of Medals",
            # hue="smoker", palette=["m", "g"],
            data=d,)
sns.lineplot(data=d, palette="tab10", linewidth=2.5,
             x="Years", y="Number of Medals", hue="States")
sns.lineplot(data=d, palette="tab10", linewidth=2.5,
             x="Years", y="Number of Medals", hue="Region")


sns.despine(offset=10, trim=True)


d3=pd.read_csv('d4.csv')

