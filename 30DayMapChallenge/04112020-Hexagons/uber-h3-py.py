
'''
Distance from Nearest Cells:
A triangle has three kinds of distance (through the edge, vertex and across the 
center of the edge), a square has two (across the edge & the diagonal) and hexagon 
only has one — another reason why triangles are not really favored.
'''

import geopandas as gpd
from h3 import h3

incidents = gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/Anti-shipping-Activity-Messages/ASAM_events.shp')
incidents.plot()

# H3 library has 15 levels of resolution
# Level 3 results in a grid size of approximately 100km
h3_level = 3

# lat_lng_to_h3 converts a location’s coordinates into an H3 id of the chosen level 
def lat_lng_to_h3(row):
    return h3.geo_to_h3(
      row.geometry.y, row.geometry.x, h3_level)

# add a column called h3 with the H3 grid id for the point at level 3 
incidents['h3'] = incidents.apply(lat_lng_to_h3, axis=1)

# Find number of piracy incidents for each grid cell
# since all points that fall in a grid cell will have the same id
# use groupby function on the h3 column and add a new column count to the output with the number of rows for each H3 id
counts = incidents.groupby(['h3']).h3.agg('count').to_frame('count').reset_index()

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
gdf.plot()



