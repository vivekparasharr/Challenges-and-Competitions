

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

summ_data=pd.read_csv(r'C:\OneDrive\OneDrive-GitHub\Challenges-and-Competitions\TidyTuesday\Data\2020-11-10\summ_data.csv')
summ_data.columns=['Country', 'Landline connections', 'Mobile connections']
ax=summ_data.plot(x='Landline connections', y='Mobile connections', kind='scatter', title='2017: Connections per 100 people (each point represents a country)')
# Inference - there are a lot of countries with more connections than number of people


import geopandas as gpd
from shapely.geometry import Point, Polygon
import adjustText as aT

countries=gpd.read_file('ne_110m_admin_0_countries.shp')
countries=countries.to_crs(crs='epsg:4326')
countries.head()
countries.plot(alpha=0.4, color='lightgrey',  edgecolor = "dimgrey",)

# join the geodataframe with the cleaned up csv dataframe
merged = countries.set_index('SOV_A3').join(summ_data.set_index('Code'))

# Map time!
fig, ax = plt.subplots(figsize=(20.5,10))
#ax.grid(True)
ax.grid(color='darkgoldenrod', linestyle='-.', linewidth=0.50)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
plt.title(label='Counties with more mobile connections than number of people!',
fontdict={'fontsize': 24, #rcParams['axes.titlesize'],
 'fontweight': 'bold',
 'color': 'firebrick', #rcParams['axes.titlecolor'],
 'verticalalignment': 'baseline',})

countries.plot(ax=ax, alpha=0.4, color='grey',  edgecolor = "dimgrey",)
merged[merged['Mobile connections']>100].plot(ax=ax, alpha=0.7, color='firebrick')

plt.text(35, -85, '#TidyTuesday - 2020-11-10 - Historical Phone Usage \nhttps://twitter.com/vivekparasharr/ \nData from OurWorldInData.org', fontsize=14)    

za=merged[merged['Mobile connections']>100]
za["center"] = za["geometry"].representative_point()  # centroid
za_points = za.copy()
za_points.set_geometry("center", inplace = True)

texts = []

for x, y, label in zip(za_points.geometry.x, za_points.geometry.y, za_points["Country"].str.title()):
    texts.append(plt.text(x, y, label, fontsize = 18, )) #color='saddlebrown'))

aT.adjust_text(texts, force_points=0.3, force_text=0.8, expand_points=(1,1), expand_text=(1,1), 
               arrowprops=dict(arrowstyle="-", color='grey', lw=0.5))

