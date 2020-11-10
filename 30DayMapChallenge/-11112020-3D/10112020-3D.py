
import pandas as pd 
import matplotlib.pyplot as plt 
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
import adjustText as at
from h3 import h3

buildings=gpd.read_file('/Users/vivekparashar/Downloads/Bos3d_Bldg_BPDA_MP_Current/Bos3d_Bldg_BPDA_MP_Current.shp')
buildings=buildings.to_crs(crs='epsg:4326')

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

buildings.plot(ax=ax, alpha=0.4, color='burlywood')
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

#############################################

import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


# setup the figure and axes
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# fake data
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax1.set_title('Shaded')

ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
ax2.set_title('Not Shaded')

plt.show()


