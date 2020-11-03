

import pandas as pd 
import matplotlib.pyplot as plt 
import descartes
import geopandas as gpd 
from shapely.geometry import Point, Polygon

# Import map of Canada
greatlakes_subbasins=gpd.read_file('/Users/vivekparashar/Documents/GitHub/30DayMapChallenge/Maps/Great-lakes/greatlakes_subbasins/greatlakes_subbasins.shp')
greatlakes_subbasins=greatlakes_subbasins.to_crs(crs='epsg:4326')
# sub_basins.plot()
# map_can.head()

hydro_p_LakeSuperior=gpd.read_file('/Users/vivekparashar/Documents/GitHub/30DayMapChallenge/Maps/Great-lakes/hydro_p_LakeSuperior/hydro_p_LakeSuperior.shp')
hydro_p_LakeSuperior=hydro_p_LakeSuperior.to_crs(crs='epsg:4326')

hydro_p_LakeStClair=gpd.read_file('/Users/vivekparashar/Documents/GitHub/30DayMapChallenge/Maps/Great-lakes/hydro_p_LakeStClair/hydro_p_LakeStClair.shp')
hydro_p_LakeStClair=hydro_p_LakeStClair.to_crs(crs='epsg:4326')

hydro_p_LakeOntario=gpd.read_file('/Users/vivekparashar/Documents/GitHub/30DayMapChallenge/Maps/Great-lakes/hydro_p_LakeOntario/hydro_p_LakeOntario.shp')
hydro_p_LakeOntario=hydro_p_LakeOntario.to_crs(crs='epsg:4326')

hydro_p_LakeMichigan=gpd.read_file('/Users/vivekparashar/Documents/GitHub/30DayMapChallenge/Maps/Great-lakes/hydro_p_LakeMichigan/hydro_p_LakeMichigan.shp')
hydro_p_LakeMichigan=hydro_p_LakeMichigan.to_crs(crs='epsg:4326')

hydro_p_LakeHuron=gpd.read_file('/Users/vivekparashar/Documents/GitHub/30DayMapChallenge/Maps/Great-lakes/hydro_p_LakeHuron/hydro_p_LakeHuron.shp')
hydro_p_LakeHuron=hydro_p_LakeHuron.to_crs(crs='epsg:4326')

hydro_p_LakeErie=gpd.read_file('/Users/vivekparashar/Documents/GitHub/30DayMapChallenge/Maps/Great-lakes/hydro_p_LakeErie/hydro_p_LakeErie.shp')
hydro_p_LakeErie=hydro_p_LakeErie.to_crs(crs='epsg:4326')

# Function for annotating the chart
def vp_annotate(x, y, text, loc):
    if loc=='tl':
        ax.annotate(text, (x, y), xytext=(x-1, y+1), 
            arrowprops=dict(facecolor='grey', shrink=0.05, lw=0.0005),
            fontsize=20,
            horizontalalignment='right', verticalalignment='top')
    if loc=='tr':
        ax.annotate(text, (x, y), xytext=(x+1, y+1), 
            arrowprops=dict(facecolor='grey', shrink=0.05, lw=0.0005),
            fontsize=20,
            horizontalalignment='left', verticalalignment='top')
    if loc=='bl':
        ax.annotate(text, (x, y), xytext=(x-1, y-1), 
            arrowprops=dict(facecolor='grey', shrink=0.05, lw=0.0005),
            fontsize=20,
            horizontalalignment='right', verticalalignment='bottom')
    if loc=='br':
        ax.annotate(text, (x, y), xytext=(x+1, y-1), 
            arrowprops=dict(facecolor='grey', shrink=0.05, lw=0.0005),
            fontsize=20,
            horizontalalignment='left', verticalalignment='bottom')

# Plot India map and River map on the same axis
fig, ax = plt.subplots(figsize=(20,17))
# ax.set_facecolor('xkcd:azure')
#ax.grid(color='steelblue', linestyle='-.', linewidth=0.50)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
greatlakes_subbasins.plot(ax=ax, alpha=0.4, color='lightgrey')
hydro_p_LakeSuperior.plot(ax=ax, alpha=0.4, color='dodgerblue')
#hydro_p_LakeStClair.plot(ax=ax, alpha=0.4, color='royalblue')
hydro_p_LakeOntario.plot(ax=ax, alpha=0.4, color='turquoise')
hydro_p_LakeMichigan.plot(ax=ax, alpha=0.4, color='steelblue')
hydro_p_LakeErie.plot(ax=ax, alpha=0.4, color='slateblue')
hydro_p_LakeHuron.plot(ax=ax, alpha=0.4, color='teal')
plt.title(label='The North American Great Lakes', 
fontdict={'fontsize': 33, 'fontweight': 'bold', 'color': 'cornflowerblue', 'verticalalignment': 'baseline',})
vp_annotate(-88,48,'Lake Superior\n(82,100 Sq Km,\nWorld Rank: 2nd)', 'tl')
vp_annotate(-82.5,46,'Lake Huron\n(59,600 Sq Km,\nWorld Rank: 4th)', 'tr')
vp_annotate(-87.5,42.5,'Lake Michigan\n(57,800 Sq Km,\nWorld Rank: 5th)', 'bl')
vp_annotate(-78,44,'Lake Ontario\n(19,010 Sq Km,\nWorld Rank: 14th)', 'tr')
#vp_annotate(-83,42.5,'Lake StClair (1,210 Sq Km)', 'bl')
vp_annotate(-80,42,'Lake Erie\n(25,670 Sq Km,\nWorld Rank: 11th)', 'br')
plt.text(-94, 40, '#30DayMapChallenge - Day 3 - Polygons \nhttps://twitter.com/vivekparasharr/ \nData from USGS-ScienceBase-Catalog, Britannica', fontsize=20)
#fig.savefig('/Users/vivekparashar/Documents/GitHub/30DayMapChallenge/day2-major-rivers.png')

