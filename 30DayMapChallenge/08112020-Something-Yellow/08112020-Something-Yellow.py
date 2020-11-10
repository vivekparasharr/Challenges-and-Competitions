
import pandas as pd 
import matplotlib.pyplot as plt 
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
import adjustText as aT
from h3 import h3

countries=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/natural_earth_vector/110m_cultural/ne_110m_admin_0_countries.shp')
countries=countries.to_crs(crs='epsg:4326')

terrain=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/stanford-bh326sc0899-shapefile/bh326sc0899.shp')
terrain=terrain.to_crs(crs='epsg:4326')

# Plotting
fig, ax = plt.subplots(figsize=(17,20))
#ax.grid(True)
ax.grid(color='darkgoldenrod', linestyle='-.', linewidth=0.50)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
#fig.suptitle('Indian Cities: Population', fontsize=50)
plt.title(label='Deserts of our Planet!',
fontdict={'fontsize': 33, #rcParams['axes.titlesize'],
 'fontweight': 'bold',
 'color': 'darkgoldenrod', #rcParams['axes.titlecolor'],
 'verticalalignment': 'baseline',})
 #'horizontalalignment': 'left'})
#ax.set(title='Indian Cities with Population > 100k')

#ax.xaxis.set_ticks([])
#ax.yaxis.set_ticks([])
#ax.xaxis.set_visible(False)
#ax.yaxis.set_visible(False)

countries.plot(ax=ax, alpha=0.4, color='grey',  edgecolor = "dimgrey",)
terrain[terrain.featurecla=='Desert'].plot(ax=ax, alpha=0.7, color='yellow')
#rivers_lakes.plot(ax=ax, alpha=0.4, color='black')
plt.text(80, -85, '#30DayMapChallenge - Day 8 - Something Yellow \nhttps://twitter.com/vivekparasharr/ \nData from https://geo.nyu.edu/', fontsize=10)

za=terrain[terrain.featurecla=='Desert'][terrain.scalerank<=3]
za.name[za.name=='RUB AL KHALI']='RUB AL KHALI'
za["center"] = za["geometry"].representative_point()  # centroid
za_points = za.copy()
za_points.set_geometry("center", inplace = True)

texts = []

for x, y, label in zip(za_points.geometry.x, za_points.geometry.y, za_points["name"].str.title()):
    texts.append(plt.text(x, y, label, fontsize = 10, )) #color='saddlebrown'))

aT.adjust_text(texts, force_points=0.3, force_text=0.8, expand_points=(1,1), expand_text=(1,1), 
               arrowprops=dict(arrowstyle="-", color='grey', lw=0.5))


