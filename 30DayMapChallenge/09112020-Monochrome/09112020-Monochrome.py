
import pandas as pd 
import matplotlib.pyplot as plt 
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
import adjustText as aT
from h3 import h3

countries=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/natural_earth_vector/110m_cultural/ne_110m_admin_0_countries.shp')
countries=countries.to_crs(crs='epsg:4326')

# Plotting
fig, ax = plt.subplots(figsize=(17,20))
#ax.grid(True)
#ax.grid(color='grey', linestyle='-.', linewidth=0.50)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
#fig.suptitle('Indian Cities: Population', fontsize=50)
plt.title(label='A Map of the World',
fontdict={'fontsize': 33, #rcParams['axes.titlesize'],
 'fontweight': 'bold',
 'color': 'black', #rcParams['axes.titlecolor'],
 'verticalalignment': 'baseline',})
 #'horizontalalignment': 'left'})
#ax.set(title='Indian Cities with Population > 100k')

#ax.xaxis.set_ticks([])
#ax.yaxis.set_ticks([])
#ax.xaxis.set_visible(False)
#ax.yaxis.set_visible(False)

countries.plot(ax=ax, alpha=0.2, color='white', edgecolor='black')
plt.text(80, -85, '#30DayMapChallenge - Day 9 - Monochrome \nhttps://twitter.com/vivekparasharr/ \nData from https://www.naturalearthdata.com/', fontsize=10)


za=countries[countries.LABELRANK<=2]
za["center"] = za["geometry"].centroid # representative_point() 
za_points = za.copy()
za_points.set_geometry("center", inplace = True)

texts = []

for x, y, label in zip(za_points.geometry.x, za_points.geometry.y, za_points["SOVEREIGNT"].str.title()):
    texts.append(plt.text(x, y, label, fontsize = 10, )) #color='saddlebrown'))

aT.adjust_text(texts, force_points=0.3, force_text=0.8, expand_points=(1,1), expand_text=(1,1), 
               arrowprops=dict(arrowstyle="-", color='black', lw=0.5))



