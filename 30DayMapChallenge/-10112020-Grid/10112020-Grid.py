

import pandas as pd 
import matplotlib.pyplot as plt 
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
from h3 import h3


map=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/India-states/Indian_States.shp')
map=map.to_crs(crs='epsg:4326')
map.plot()

# import population data
df=pd.read_csv('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Data/India-cities-population.csv')
# convert lat, lon to geography (point)
points=df.apply(lambda row: Point(row.lng, row.lat), axis=1)
# create a new gpd.df from existing pd.df and geography
cities=gpd.GeoDataFrame(df, crs={'init':'epsg:4326'}, geometry=points)
cities.plot()

####################################################

# H3 library has 15 levels of resolution
# Level 3 results in a grid size of approximately 100km
h3_level = 3

# lat_lng_to_h3 converts a location’s coordinates into an H3 id of the chosen level 
def lat_lng_to_h3(row):
    return h3.geo_to_h3(
      row.geometry.y, row.geometry.x, h3_level)

# add a column called h3 with the H3 grid id for the point at level 3 
cities['h3'] = cities.apply(lat_lng_to_h3, axis=1)

# Find number of piracy incidents for each grid cell
# since all points that fall in a grid cell will have the same id
# use groupby function on the h3 column and add a new column count to the output with the number of rows for each H3 id
counts = cities.groupby(['h3']).h3.agg('count').to_frame('count').reset_index()

# To visualize the results or export it to a GIS, we need to convert the H3 cell ids to a geometry
# h3_to_geo_boundary function takes a H3 key and returns a list of coordinates that form the hexagonal cell
from shapely.geometry import Polygon
 
def add_geometry(row):
    points = h3.h3_to_geo_boundary(
      row['h3'], True)
    return Polygon(points)
 
counts['geometry'] = counts.apply(add_geometry, axis=1)

# We turn the dataframe to a GeoDataframe with the CRS EPSG:4326 (WGS84 Latitude/Longitude) and write it to a geopackage
gdf = gpd.GeoDataFrame(counts, crs='EPSG:4326')
#gdf.plot()

cities_hex=gdf

####################################################



# funciton for annotating
def city_info(id):
    top_cities=cities[cities.population>=5000000]
    top_cities_sel_col=top_cities[['city','population','lat','lng']]
    return top_cities_sel_col.iloc[id]
def coord(id):
    return (city_info(i).lng - 0.25, city_info(i).lat - 0.25)
def coord_txt(id):
    if i in [0, 4]:
        return (city_info(i).lng - 1, city_info(i).lat - 1.5)
    if i in [1]:
        return (city_info(i).lng - 3, city_info(i).lat + 3)
    if i in [2, 5, 3, 6]:
        return (city_info(i).lng + 9, city_info(i).lat - 1.5)


# Indian cities with population more than a 100k
fig, ax = plt.subplots(figsize=(17,20))
#ax.grid(True)
ax.grid(color='steelblue', linestyle='-.', linewidth=0.50)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
#fig.suptitle('Indian Cities: Population', fontsize=50)
plt.title(label='Indian Cities with Population > 100,000 people',
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

map.plot(ax=ax, alpha=0.4, color='gainsboro')
cities_hex.plot(ax=ax, alpha=0.4, color='cornflowerblue')
plt.text(83, 6, '#30DayMapChallenge - Day 4 - Hexagons \nhttps://twitter.com/vivekparasharr/ \nData from https://diva-gis.org/gdata', fontsize=20)


for i in range(7):
    ax.annotate('['+str(i)+'] '+city_info(i).city, coord(i), #(city_info(i).lng - 0.25, city_info(i).lat - 0.25),
                xytext=coord_txt(i), # (city_info(i).lng - 1.5, city_info(i).lat - 1.5),
                #textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=25,
                horizontalalignment='right', verticalalignment='top')


#########################################

import numpy as np
from scipy.interpolate import griddata
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#Define mapframe
lllon = -11
lllat = 49
urlon = 2
urlat = 61

# Make some toy data, random points + corners
n = 10 # no of stations
lat = np.random.uniform(low=lllat+2, high=urlat-2, size=n)
lat = np.append(lat, [lllat, urlat, urlat, lllat]) 
lon = np.random.uniform(low=lllon+2, high=urlon-2, size=n)
lon = np.append(lon, [lllon, urlon, lllon, urlon])
temp = np.random.randn(n+4) + 8 # British summer?

# set up basemap chose projection!
m = Basemap(projection = 'merc', resolution='i', 
    llcrnrlon = lllon, llcrnrlat = lllat, urcrnrlon = urlon, urcrnrlat = urlat) 

# transform coordinates to map projection m
m_lon, m_lat = m(*(lon, lat))

# generate grid data
numcols, numrows = 240, 240
xi = np.linspace(m_lon.min(), m_lon.max(), numcols)
yi = np.linspace(m_lat.min(), m_lat.max(), numrows)
xi, yi = np.meshgrid(xi, yi)

# interpolate, there are better methods, especially if you have many datapoints
zi = griddata((m_lon,m_lat),temp,(xi,yi),method='cubic')

fig, ax = plt.subplots(figsize=(12, 12))

# draw map details
m.drawmapboundary(fill_color = 'skyblue', zorder = 1)

# Plot interpolated temperatures
m.contourf(xi, yi, zi, 500, cmap='magma', zorder = 2)

m.drawlsmask(ocean_color='skyblue', land_color=(0, 0, 0, 0), lakes=True, zorder = 3)

cbar = plt.colorbar()
plt.title('Temperature')

plt.show()

####################################

import matplotlib.pyplot as plt
import numpy as np
 
# Create a array of marks in different subjects scored by different students 
z=np.random(20)
z = np.array([[0, 0, 0, 0,0, 0],
                    [72, 85, 64, 33, 47, 87],
                    [52, 97, 44, 73, 17, 56],
                    [69, 45, 89, 79,70, 48],
                    [87, 65, 56, 86, 72, 68],
                    [90, 29, 78, 66, 50, 32]])
# name of students
x=range(50)
# name of subjects
y=range(50) 
# Setting the labels of x axis.
# set the xticks as student-names
# rotate the labels by 90 degree to fit the names
plt.xticks(ticks=np.arange(len(x)),labels=x,rotation=90)
# Setting the labels of y axis.
# set the xticks as subject-names
plt.yticks(ticks=np.arange(len(y)),labels=y)
# use the imshow function to generate a heatmap
# cmap parameter gives color to the graph
# setting the interpolation will lead to different types of graphs
plt.imshow(z, cmap='cool',interpolation="nearest")
