

import pandas as pd 
import matplotlib.pyplot as plt 
import descartes
import geopandas as gpd 
from shapely.geometry import Point, Polygon

# Import map of India
map_india=gpd.read_file('/Users/vivekparashar/Documents/Code/Challenges-and-Competitions/30DayMapChallenge/Shapefiles/India-states/Indian_States.shp')
map_india=map_india.to_crs(crs='epsg:4326')
map_india.head()

# Import map of Rivers
map=gpd.read_file('/Users/vivekparashar/Documents/Code/Challenges-and-Competitions/30DayMapChallenge/Shapefiles/India-water/IND_water_lines_dcw.shp')
map=map.to_crs(crs='epsg:4326')
map.crs
map.head()

# Get unique river names
map.NAM.unique()
# Remove maps with unknown names
map[map.NAM!='UNK'].head()

# Function for annotating the chart
def vp_annotate(x, y, text, loc):
    if loc=='tl':
        ax.annotate(text, (x, y), xytext=(x-2, y+2), 
            arrowprops=dict(facecolor='grey', shrink=0.05, lw=0.0005),
            fontsize=20,
            horizontalalignment='right', verticalalignment='top')
    if loc=='tr':
        ax.annotate(text, (x, y), xytext=(x+3, y+2), 
            arrowprops=dict(facecolor='grey', shrink=0.05, lw=0.0005),
            fontsize=20,
            horizontalalignment='left', verticalalignment='top')
    if loc=='bl':
        ax.annotate(text, (x, y), xytext=(x-2, y-2), 
            arrowprops=dict(facecolor='grey', shrink=0.05, lw=0.0005),
            fontsize=20,
            horizontalalignment='right', verticalalignment='bottom')
    if loc=='br':
        ax.annotate(text, (x, y), xytext=(x+2, y-2), 
            arrowprops=dict(facecolor='grey', shrink=0.05, lw=0.0005),
            fontsize=20,
            horizontalalignment='left', verticalalignment='bottom')

# Plot India map and River map on the same axis
fig, ax = plt.subplots(figsize=(17,20))
# ax.set_facecolor('xkcd:azure')
ax.grid(color='steelblue', linestyle='-.', linewidth=0.50)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
map_india.plot(ax=ax, alpha=0.4, color='gainsboro')
map[map.NAM!='UNK'].plot(ax=ax, alpha=0.4, color='blue',)
plt.title(label='Major Rivers of India', 
fontdict={'fontsize': 33, 'fontweight': 'bold', 'color': 'cornflowerblue', 'verticalalignment': 'baseline',})
vp_annotate(82,26.5,'Ganges (2,525 Km)', 'tr')
vp_annotate(74.5,19.5,'Godavari \n(1,465 Km)', 'bl')
vp_annotate(74.5,16.5,'Krishna \n(1,400 Km)', 'bl')
vp_annotate(74,21.5,'Narmada \n(1,313 Km)', 'bl')
vp_annotate(78,28.5,'Yamuna (1,211 Km)', 'tr')
vp_annotate(78,33.5,'Indus (1,114 Km)', 'tr')
vp_annotate(94,27.5,'Brahmaputra (916 Km)', 'tl')
vp_annotate(86,20.5,'Mahanadi (851 Km)', 'br')
vp_annotate(78.5,9.5,'Kaveri (800 Km)', 'tr')
vp_annotate(77,21,'Tapi (724 Km)', 'tr')
plt.text(85, 6, '#30DayMapChallenge - Day 2 - Lines \nhttps://twitter.com/vivekparasharr/ \nData from DIVA-GIS', fontsize=20)
# fig.savefig('/Users/vivekparashar/Documents/GitHub/30DayMapChallenge/day2-major-rivers.png')

# Plot India map and River map on the same axis
fig, ax = plt.subplots(figsize=(17,20))
ax.grid(color='steelblue', linestyle='-.', linewidth=0.50)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
map_india.plot(ax=ax, alpha=0.4, color='gainsboro')
map.plot(ax=ax, alpha=0.4, color='blue',)
plt.title(label='All Rivers of India\nPerennial and Non-Perennial', 
fontdict={'fontsize': 33, 'fontweight': 'bold', 'color': 'cornflowerblue', 'verticalalignment': 'baseline',})
vp_annotate(82,26.5,'Ganges (2,525 Km)', 'tr')
vp_annotate(74.5,19.5,'Godavari \n(1,465 Km)', 'bl')
vp_annotate(74.5,16.5,'Krishna \n(1,400 Km)', 'bl')
vp_annotate(74,21.5,'Narmada \n(1,313 Km)', 'bl')
vp_annotate(78,28.5,'Yamuna (1,211 Km)', 'tr')
vp_annotate(78,33.5,'Indus (1,114 Km)', 'tr')
vp_annotate(94,27.5,'Brahmaputra (916 Km)', 'tl')
vp_annotate(86,20.5,'Mahanadi (851 Km)', 'br')
vp_annotate(78.5,9.5,'Kaveri (800 Km)', 'tr')
vp_annotate(77,21,'Tapi (724 Km)', 'tr')
plt.text(85, 6, '#30DayMapChallenge - Day 2 - Lines \nhttps://twitter.com/vivekparasharr/ \nData from DIVA-GIS', fontsize=20)

