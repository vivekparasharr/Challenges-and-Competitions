

import pandas as pd 
import matplotlib.pyplot as plt 
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
from h3 import h3


map=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/India-states/Indian_States.shp')
fig, ax = plt.subplots(figsize=(15,15))
#map.plot(ax=ax)
map=map.to_crs(crs='epsg:4326')
map.crs

# import data
df=pd.read_csv('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Data/India-cities-population.csv')
# convert lat, lon to geography (point)
points=df.apply(lambda row: Point(row.lng, row.lat), axis=1)
# create a new gpd.df from existing pd.df and geography
cities=gpd.GeoDataFrame(df, crs={'init':'epsg:4326'}, geometry=points)
# check current crs
cities.crs 
# plot the data
# cities.plot()
#cities.plot()

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



