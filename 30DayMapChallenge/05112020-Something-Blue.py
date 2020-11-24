
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
