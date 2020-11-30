
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon
import adjustText as aT

map_df=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Shapefiles/natural_earth_vector/110m_cultural/ne_110m_admin_0_countries.shp')
map_df=map_df.to_crs(crs='epsg:4326')

df = pd.read_csv('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Data/map-of-genocide-and-politicide-deaths-around-the-world.csv')

# join the geodataframe with the cleaned up csv dataframe
merged = map_df.set_index('SOV_A3').join(df.set_index('Code'))
merged.to_csv('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Data/map-of-genocide-and-politicide-deaths-around-the-world-added-geo-data.csv')

