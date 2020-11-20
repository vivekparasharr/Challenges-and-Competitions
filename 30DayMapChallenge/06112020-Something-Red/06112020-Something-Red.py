
import pandas as pd 
import matplotlib.pyplot as plt 
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
from h3 import h3

cntry04=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/Volcanoes_of_the_World_93_from_Shapefiles/commondata/data0/cntry04.shp')
cntry04=cntry04.to_crs(crs='epsg:4326')
cntry04.plot()

volcanoes=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/Volcanoes_of_the_World_93_from_Shapefiles/commondata/data0/volcanoes.shp')
volcanoes=volcanoes.to_crs(crs='epsg:4326')
volcanoes.plot()

ridge=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/PLATES_PlateBoundary_ArcGIS/ridge.shp')
ridge=ridge.to_crs(crs='epsg:4326')
ridge.plot()

transform=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/PLATES_PlateBoundary_ArcGIS/transform.shp')
transform=transform.to_crs(crs='epsg:4326')
transform.plot()

trench=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/PLATES_PlateBoundary_ArcGIS/trench.shp')
trench=trench.to_crs(crs='epsg:4326')
trench.plot()

# Plotting
fig, ax = plt.subplots(figsize=(17,20))
#ax.grid(True)
ax.grid(color='lightsalmon', linestyle='-.', linewidth=0.50)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
#fig.suptitle('Indian Cities: Population', fontsize=50)
plt.title(label='So many volcanoes!',
fontdict={'fontsize': 33, #rcParams['axes.titlesize'],
 'fontweight': 'bold',
 'color': 'firebrick', #rcParams['axes.titlecolor'],
 'verticalalignment': 'baseline',})
 #'horizontalalignment': 'left'})
#ax.set(title='Indian Cities with Population > 100k')

#ax.xaxis.set_ticks([])
#ax.yaxis.set_ticks([])
#ax.xaxis.set_visible(False)
#ax.yaxis.set_visible(False)

cntry04.plot(ax=ax, alpha=0.4, color='burlywood')
volcanoes[volcanoes.TYPE=='Solfatara stage'].plot(ax=ax, alpha=0.4, color='coral')
volcanoes[volcanoes.TYPE=='Active'].plot(ax=ax, alpha=0.4, color='maroon')
volcanoes[volcanoes.TYPE=='Potentially active'].plot(ax=ax, alpha=0.4, color='firebrick')
ridge.plot(ax=ax, alpha=0.4, color='sienna')
transform.plot(ax=ax, alpha=0.4, color='peru')
trench.plot(ax=ax, alpha=0.4, color='saddlebrown')
plt.text(80, -85, '#30DayMapChallenge - Day 6 - Something Red \nhttps://twitter.com/vivekparasharr/ \nData from www.arcgis.com/, www-udc.ig.utexas.edu/', fontsize=10)


###########################

colorr='firebrick'
fs=20
#ax.annotate('Phillipine \nPlate', (130, 15), fontsize=fs, color=colorr)
vp_annotate(110,12.5,'Phillipine\nPlate', 'tl', 'firebrick', 20, 35, 0.5)
ax.annotate('Eurasian \nPlate', (40, 55), fontsize=fs, color=colorr)
ax.annotate('Indian \nPlate', (65, 5), fontsize=fs, color=colorr)
ax.annotate('Africa \nPlate', (5, -15), fontsize=fs, color=colorr)
ax.annotate('North \nAmerican \nPlate', (-105, 50), fontsize=fs, color=colorr)
ax.annotate('North \nAmerican \nPlate', (155, 65), fontsize=fs, color=colorr)
#ax.annotate('Carribean \nPlate', (-110, 10), fontsize=fs, color=colorr)
vp_annotate(-95,10,'Carribean\nPlate', 'bl', 'firebrick', 20, 30, 0.5)
ax.annotate('South \nAmerican \nPlate', (-60, -25), fontsize=fs, color=colorr)
ax.annotate('Nazca \nPlate', (-105, -25), fontsize=fs, color=colorr)
ax.annotate('Pacific \nPlate', (-180, 0), fontsize=fs, color=colorr)
ax.annotate('Pacific \nPlate', (160, 5), fontsize=fs, color=colorr)
ax.annotate('Australian \nPlate', (110, -35), fontsize=fs, color=colorr)
ax.annotate('Antarctic \nPlate', (-12, -85), fontsize=fs, color=colorr)



############################

# Function for annotating the chart
# aspect - is 2 if x is twice the length of y
# aspect - is 1.5 if x is 1.5 times the length of y
def vp_annotate(x, y, text, loc, colorr, fs, dist, aspect):
    arrow_properties=dict(arrowstyle= '-|>', #  '<|-|>',
                             color='firebrick',
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



