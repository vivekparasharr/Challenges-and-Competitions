
import os
os.chdir(r'C:\Users\vivek\Downloads\Chile')

import pandas as pd 
import matplotlib.pyplot as plt 
import descartes
import geopandas as gpd 
from shapely.geometry import Point, Polygon

# natural map of chile
chile_natural=gpd.read_file(r'natural\natural.shp')
chile_natural=chile_natural.to_crs(crs='epsg:4326')
chile_natural.plot()
chile_natural.head()

#places
chile_places=gpd.read_file(r'places\places.shp')
chile_places=chile_places.to_crs(crs='epsg:4326')
chile_places.plot()
chile_places.head()

# Import map of Canada
chile_landuse=gpd.read_file('landuse\landuse.shp')
chile_landuse=chile_landuse.to_crs(crs='epsg:4326')
# sub_basins.plot()
# map_can.head()
chile_landuse.plot()

# buildings
chile_buildings=gpd.read_file(r'buildings\buildings.shp')
chile_buildings=chile_buildings.to_crs(crs='epsg:4326')
chile_buildings.plot()
chile_buildings.head()

