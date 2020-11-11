

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


mobile=pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-11-10/mobile.csv')
landline=pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-11-10/landline.csv')

mobile.columns
mobile.head()
mobile.entity.unique()

m1=mobile.groupby(['continent', 'entity', 'code', 'year']).agg({
    'mobile_subs':'mean'
})
m1.reset_index(level=0, inplace=True) # Convert Index to Column

m1[m1.entity=='India'].plot(x='year', y='mobile_subs', kind='bar')

mobile[mobile.entity=='India']


bar = alt.Chart(m1[m1.entity=='India']).mark_bar().encode(
    x='year',
    y='mobile_subs'
).properties(
    width=alt.Step(40),  # controls width of bar.
    title='#Items vs Price Per Category (Bars represent #Items, Ticks represent Avg. Price)'
)

mobile['geography']=

c1=countries[['ADM0_A3','geometry']]

m1.concat(c1,axis=0,join='left',join_axes=None,ignore_index=False)

m1.join(c1, on=['code','ADM0_A3'],
         lsuffix="_df1", rsuffix="_df2")


m1['geometry']=np.NaN

for idx in m1.index:
   m1.loc[idx,'geometry'] = c1.loc[idx, '']*df_lookup.at[idx.hour]


countries.plot()
countries.shape

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



#######################################################



import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
from h3 import h3

countries=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/natural_earth_vector/110m_cultural/ne_110m_admin_0_countries.shp')
countries=countries.to_crs(crs='epsg:4326')

oceans=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/natural_earth_vector/110m_physical/ne_110m_ocean.shp')
oceans=oceans.to_crs(crs='epsg:4326')

glaciated_areas=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/natural_earth_vector/110m_physical/ne_110m_glaciated_areas.shp')
glaciated_areas=glaciated_areas.to_crs(crs='epsg:4326')

countries_lakes=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/natural_earth_vector/110m_cultural/ne_110m_admin_0_countries_lakes.shp')
countries_lakes=countries_lakes.to_crs(crs='epsg:4326')

rivers_lakes=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/natural_earth_vector/110m_physical/ne_110m_rivers_lake_centerlines.shp')
rivers_lakes=rivers_lakes.to_crs(crs='epsg:4326')

# Plotting
fig, ax = plt.subplots(figsize=(17,20))
#ax.grid(True)
ax.grid(color='steelblue', linestyle='-.', linewidth=0.50)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
#fig.suptitle('Indian Cities: Population', fontsize=50)
plt.title(label='So much of Earth is covered in Water',
fontdict={'fontsize': 33, #rcParams['axes.titlesize'],
 'fontweight': 'bold',
 'color': 'cornflowerblue', #rcParams['axes.titlecolor'],
 'verticalalignment': 'baseline',})
 #'horizontalalignment': 'left'})
#ax.set(title='Indian Cities with Population > 100k')

#ax.xaxis.set_ticks([])
#ax.yaxis.set_ticks([])
#ax.xaxis.set_visible(False)
#ax.yaxis.set_visible(False)

countries.plot(ax=ax, alpha=0.4, color='burlywood')
oceans.plot(ax=ax, alpha=0.4, color='dodgerblue')
glaciated_areas.plot(ax=ax, alpha=0.4, color='cornflowerblue')
#rivers_lakes.plot(ax=ax, alpha=0.4, color='black')
plt.text(80, -85, '#30DayMapChallenge - Day 5 - Something Blue \nhttps://twitter.com/vivekparasharr/ \nData from https://www.naturalearthdata.com/', fontsize=10)

ax.annotate('Asia', (80, 40), fontsize=20, color='forestgreen')
ax.annotate('Africa', (15, -5), fontsize=20, color='forestgreen')
ax.annotate('Europe', (20, 45), fontsize=20, color='forestgreen')
ax.annotate('Oceania', (120, -27), fontsize=20, color='forestgreen')
ax.annotate('North \nAmerica', (-110, 40), fontsize=20, color='forestgreen')
ax.annotate('South \nAmerica', (-70, -15), fontsize=20, color='forestgreen')
ax.annotate('Antarctica', (-12, -84), fontsize=20, color='forestgreen')

ax.annotate('Pacific \nOcean', (-150, 0), fontsize=20, color='maroon')
ax.annotate('Atlantic \nOcean', (-50, 25), fontsize=20, color='maroon')
ax.annotate('Indian \nOcean', (72, -15), fontsize=20, color='maroon')
ax.annotate('Southern \nOcean', (-9, -60), fontsize=20, color='maroon')
ax.annotate('Arctic \nOcean', (-9, 72), fontsize=20, color='maroon')


