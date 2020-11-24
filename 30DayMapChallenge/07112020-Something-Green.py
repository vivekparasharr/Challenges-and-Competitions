
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib as mpl 
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
from h3 import h3

# https://sites.google.com/site/georesweb/geographic-datasets

map=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/India-states/Indian_States.shp')
map=map.to_crs(crs='epsg:4326')

map_forest=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/India Districts with Forest Cover 2015/India Districts with Forest Cover 2015/India Districts with Forest Cover 2015.shp')
map_forest=map_forest.to_crs(crs='epsg:4326')

# Plotting
fig, ax = plt.subplots(figsize=(17,20))
#ax.grid(True)
#ax.grid(color='steelblue', linestyle='-.', linewidth=0.50)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
#fig.suptitle('Indian Cities: Population', fontsize=50)
plt.title(label='Forests of India',
fontdict={'fontsize': 33, #rcParams['axes.titlesize'],
 'fontweight': 'bold',
 'color': 'darkgreen', #rcParams['axes.titlecolor'],
 'verticalalignment': 'baseline',})
 #'horizontalalignment': 'left'})
#ax.set(title='Indian Cities with Population > 100k')

#ax.xaxis.set_ticks([])
#ax.yaxis.set_ticks([])
#ax.xaxis.set_visible(False)
#ax.yaxis.set_visible(False)

map.plot(ax=ax, alpha=0.4, color='gainsboro')
map_forest[map_forest.Very_Dense > 0].plot(ax=ax, alpha=0.7, color='darkgreen')
plt.text(89.5, 5.5, '#30DayMapChallenge - Day 7 - Something Green \nhttps://twitter.com/vivekparasharr/ \nData from Forest Survey of India (FSI)', fontsize=10)

vp_annotate(78.5,32,'1. Himachal Pradesh (329 forests)\n2. Uttarakhand (133 forests)\n3. Jammu and Kashmir (92 forests)\n4. Haryana (57 forests)\n5. Uttar Pradesh (32 forests)', 'tr', 'darkgreen', 17, 5, 0.2)
vp_annotate(93,27,'1. Manipur (166 forests)\n2. Arunachal Pradesh (159 forests)\n3. Tripura (105 forests)\n4. Assam (29 forests)\n5. Sikkim (16 forests)', 'tl', 'darkgreen', 17, 5, 0.2)
vp_annotate(70.4,28,'1. Rajasthan (560 forests)\n2. Gujarat (42 forests)', 'tr', 'darkgreen', 17, 1.5, 0.2)
vp_annotate(87,21.5,'1. West Bengal (562 forests)\n2. Orissa (188 forests)\n3. Bihar (43 trees)\n4. Jharkhand (29 trees)', 'br', 'darkgreen', 17, 6, 0.2)
vp_annotate(80,20,'1. Madya Pradesh (170 forests)\n2. Chhattisgarh (63 forests)', 'br', 'darkgreen', 17, 8, 0.2)
vp_annotate(80,12,'1. Tamil Nadu (1,275 forests)\n2. Andhra Pradesh (677 forests)\n3. Puducherry (108 forests)\n4. Telangana (57 forests)', 'br', 'darkgreen', 17, 6, 0.2)
vp_annotate(76.5,12,'1. Maharashtra (2,820 forests)\n2. Karnataka (1,476 forests)\n3. Kerala (644 forests)\n4. Goa (93 forests)', 'bl', 'darkgreen', 17, 3, 0.2)



############################

# Function for annotating the chart
# aspect - is 2 if x is twice the length of y
# aspect - is 1.5 if x is 1.5 times the length of y
def vp_annotate(x, y, text, loc, colorr, fs, dist, aspect):
    arrow_properties=dict(arrowstyle= '-|>', #  '<|-|>',
                             color='darkgreen',
                             lw=3.5,
                             ls='--')
    if loc=='tl':
        ax.annotate(text, xy=(x, y), xytext=(x-dist*aspect, y+dist), 
            arrowprops=arrow_properties,
            fontsize=fs, color=colorr,
            horizontalalignment='right', verticalalignment='top')
    if loc=='tr':
        ax.annotate(text, xy=(x, y), xytext=(x+dist*aspect, y+dist), 
            arrowprops=arrow_properties,
            fontsize=fs, color=colorr,
            horizontalalignment='left', verticalalignment='top')
    if loc=='bl':
        ax.annotate(text, xy=(x, y), xytext=(x-dist*aspect, y-dist), 
            arrowprops=arrow_properties,
            fontsize=fs, color=colorr,
            horizontalalignment='right', verticalalignment='bottom')
    if loc=='br':
        ax.annotate(text, xy=(x, y), xytext=(x+dist*aspect, y-dist), 
            arrowprops=arrow_properties,
            fontsize=fs, color=colorr,
            horizontalalignment='left', verticalalignment='bottom')




