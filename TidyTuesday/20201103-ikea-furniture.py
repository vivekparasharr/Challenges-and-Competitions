# -*- coding: utf-8 -*-
"""
Created on Tue Nov 03 17:04:37 2020

@author: vivek
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=6.4, 4.8

import numpy as np
import seaborn as sns
sns.set_theme(style="ticks", palette="pastel")
import altair as alt


df=pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-11-03/ikea.csv')

df.columns
'''
Index(['Unnamed: 0', 'item_id', 'name', 'category', 'price', 'old_price',
       'sellable_online', 'link', 'other_colors', 'short_description',
       'designer', 'depth', 'height', 'width'],
      dtype='object')
'''

df.head()
df.category.unique()

d1=df.groupby(['category']).agg({
    'price':'mean', 
    'item_id':'nunique'}) 
d1=pd.DataFrame(d1) # Convert Series to DataFrame
d1.reset_index(level=0, inplace=True) # Convert Index to Column
#d1.price=d1.price.apply(np.round)
d1.price=d1.price.astype(int)
#d1=d1.sort_values(by='item_id')
d1.columns=['Furniture Category', 'Average Price (SR)', 'Number of Items']

##

bar = alt.Chart(d1).mark_bar().encode(
    x='Furniture Category',
    y='Number of Items'
).properties(
    width=alt.Step(40),  # controls width of bar.
    title='#Items vs Price Per Category (Bars represent #Items, Ticks represent Avg. Price)'
)

text_bar = bar.mark_text(
    align='center',
    baseline='bottom',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='Number of Items'
)

tick = alt.Chart(d1).mark_tick(
    color='red',
    thickness=4,
    size=40 * 0.9,  # controls width of tick.
).encode(
    x='Furniture Category',
    y='Average Price (SR)',
    text='Average Price (SR)'
)

text_tick = tick.mark_text(
    align='left',
    baseline='bottom',
    angle=270,
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='Average Price (SR)'
)

bar + text_bar + tick + text_tick

