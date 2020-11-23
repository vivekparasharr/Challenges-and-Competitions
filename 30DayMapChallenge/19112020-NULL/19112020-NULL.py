
# %%
import pandas as pd 
import matplotlib.pyplot as plt 
#import descartes
import geopandas as gpd 
from shapely.geometry import Point, Polygon

map_india=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/India-states/Indian_States.shp')
map_india=map_india.to_crs(crs='epsg:4326')
map_lines=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/India-water/IND_water_lines_dcw.shp')
map_lines=map_lines.to_crs(crs='epsg:4326')
map_areas=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/India-water/IND_water_areas_dcw.shp')
map_areas=map_areas.to_crs(crs='epsg:4326')

fig, ax = plt.subplots(figsize=(7,9))
ax.grid(color='steelblue', linestyle='-.', linewidth=0.25)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
map_india.plot(ax=ax, alpha=0.4, color='gainsboro')
map_lines[map_lines.NAM!='UNK'].plot(ax=ax, alpha=0.4, color='blue',)
map_areas[map_areas.NAME=='BRAHMAPUTRA'].plot(ax=ax, alpha=0.4, color='red',)
# map_areas[map_areas.NAME=='GANGA GANGES'].plot(ax=ax, alpha=0.4, color='red', )
plt.title(label='Major Rivers of India', fontdict={'fontsize': 33, 'fontweight': 'bold', 'color': 'cornflowerblue', 'verticalalignment': 'baseline',})
# Annotate
ax.annotate('Missing Brahmaputra River', (93, 27), xytext=(91, 29), 
            arrowprops=dict(facecolor='grey', shrink=0.05, lw=0.0005),
            fontsize=12,
            horizontalalignment='right', verticalalignment='top')
plt.show()

# %%
