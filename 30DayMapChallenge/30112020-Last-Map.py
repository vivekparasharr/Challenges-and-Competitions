
# 1. Create the Interactive Globe
# 1.1 Download and import the topography data
import numpy as np
from netCDF4 import Dataset

def Etopo(lon_area, lat_area, resolution):
  ### Input
  # resolution: resolution of topography for both of longitude and latitude [deg]
  # (Original resolution is 0.0167 deg)
  # lon_area and lat_area: the region of the map which you want like [100, 130], [20, 25]
  ###
  ### Output
  # Mesh type longitude, latitude, and topography data
  ###
  
  # Read NetCDF data
  data = Dataset("/Users/vivekparashar/Downloads/ETOPO1_Ice_g_gdal.grd", "r")
  
  # Get data
  lon_range = data.variables['x_range'][:]
  lat_range = data.variables['y_range'][:]
  topo_range = data.variables['z_range'][:]
  spacing = data.variables['spacing'][:]
  dimension = data.variables['dimension'][:]
  z = data.variables['z'][:]
  lon_num = dimension[0]
  lat_num = dimension[1]
  
  # Prepare array
  lon_input = np.zeros(lon_num); lat_input = np.zeros(lat_num)
  for i in range(lon_num):
    lon_input[i] = lon_range[0] + i * spacing[0]
  for i in range(lat_num):
    lat_input[i] = lat_range[0] + i * spacing[1]

  # Create 2D array
  lon, lat = np.meshgrid(lon_input, lat_input)
  
  # Convert 2D array from 1D array for z value
  topo = np.reshape(z, (lat_num, lon_num))
  
  # Skip the data for resolution
  if ((resolution < spacing[0]) | (resolution < spacing[1])):
    print('Set the highest resolution')
  else:
    skip = int(resolution/spacing[0])
    lon = lon[::skip,::skip]
    lat = lat[::skip,::skip]
    topo = topo[::skip,::skip]
    
  topo = topo[::-1]
  
  # Select the range of map
  range1 = np.where((lon>=lon_area[0]) & (lon<=lon_area[1]))
  lon = lon[range1]; lat = lat[range1]; topo = topo[range1]
  range2 = np.where((lat>=lat_area[0]) & (lat<=lat_area[1]))
  lon = lon[range2]; lat = lat[range2]; topo = topo[range2]
  
  # Convert 2D again
  lon_num = len(np.unique(lon))
  lat_num = len(np.unique(lat))
  lon = np.reshape(lon, (lat_num, lon_num))
  lat = np.reshape(lat, (lat_num, lon_num))
  topo = np.reshape(topo, (lat_num, lon_num))
  
  return lon, lat, topo


# 1.2 Converting to the spherical coordinates
def degree2radians(degree):
  # convert degrees to radians
  return degree*np.pi/180
  
def mapping_map_to_sphere(lon, lat, radius=1):
  # this function maps the points of coords (lon, lat) to points onto the sphere of radius radius
  lon=np.array(lon, dtype=np.float64)
  lat=np.array(lat, dtype=np.float64)
  lon=degree2radians(lon)
  lat=degree2radians(lat)
  xs=radius*np.cos(lon)*np.cos(lat)
  ys=radius*np.sin(lon)*np.cos(lat)
  zs=radius*np.sin(lat)
  return xs, ys, zs


# 1.3 Plot the Interactive Globe using Plotly
# Import topography data
# Select the area you want
resolution = 0.8
lon_area = [-180., 180.]
lat_area = [-90., 90.]
# Get mesh-shape topography data
lon_topo, lat_topo, topo = Etopo(lon_area, lat_area, resolution)

# converting to the spherical coordinates using the created function of mapping_map_to_sphere
xs, ys, zs = mapping_map_to_sphere(lon_topo, lat_topo)

# define the color scale of the topography 
Ctopo = [[0, 'rgb(0, 0, 70)'],[0.2, 'rgb(0,90,150)'], 
          [0.4, 'rgb(150,180,230)'], [0.5, 'rgb(210,230,250)'],
          [0.50001, 'rgb(0,120,0)'], [0.57, 'rgb(220,180,130)'], 
          [0.65, 'rgb(120,100,0)'], [0.75, 'rgb(80,70,0)'], 
          [0.9, 'rgb(200,200,200)'], [1.0, 'rgb(255,255,255)']]
cmin = -8000
cmax = 8000

# We prepare the plot using Plotly as follows
topo_sphere=dict(type='surface',
  x=xs,
  y=ys,
  z=zs,
  colorscale=Ctopo,
  surfacecolor=topo,
  cmin=cmin,
  cmax=cmax)

# To make our plot more brilliant, the axes are removed as follows
noaxis=dict(showbackground=False,
  showgrid=False,
  showline=False,
  showticklabels=False,
  ticks='',
  title='',
  zeroline=False)

# Figure title (‘3D spherical topography map’), font (‘Courier New’), and its associated settings are described here
import plotly.graph_objs as go

titlecolor = 'white'
bgcolor = 'black'

layout = go.Layout(
  autosize=False, width=1200, height=800,
  title = '3D spherical topography map',
  titlefont = dict(family='Courier New', color=titlecolor),
  showlegend = False,
  scene = dict(
    xaxis = noaxis,
    yaxis = noaxis,
    zaxis = noaxis,
    aspectmode='manual',
    aspectratio=go.layout.scene.Aspectratio(
      x=1, y=1, z=1)),
  paper_bgcolor = bgcolor,
  plot_bgcolor = bgcolor)


# Finally, we create the plot and export as an HTML file.
# Once you create the HTML file, you can check your plot using the Web browser (Google Chrome, Safari, …) in the local environment.
from plotly.offline import plot

plot_data=[topo_sphere]
fig = go.Figure(data=plot_data, layout=layout)
plot(fig, validate = False, filename='SphericalTopography.html',
   auto_open=True)


# In the above plot, the topography data was displayed as the color without any three-dimensional shapes. Here we create those shapes by converting xs, ys, and zs. The following code describes how to create and make the figure just like what we did in the previous plot
ratio_topo = 1.0 + topo*1e-5
xs_3d = xs*ratio_topo
ys_3d = ys*ratio_topo
zs_3d = zs*ratio_topo

topo_sphere_3d=dict(type='surface',
    x=xs_3d,
    y=ys_3d,
    z=zs_3d,
    colorscale=Ctopo,
    surfacecolor=topo,
    opacity=1.,
    cmin=cmin,
    cmax=cmax,
    showscale=False,
    hoverinfo='skip'
    )

plot_data_3DST=[topo_sphere_3d]
fig = go.Figure(data=plot_data_3DST, layout=layout)

fig.update_layout(title_text = '3D Map of Earth with Elevation')

os.chdir('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps')
plot(fig, validate = False, filename='30112020-3DSphericalTopography.html',
    auto_open=True)

plot(fig)

# 2 Plot the Global Earthquake Distribution on the Interactive Globe
# https://towardsdatascience.com/create-interactive-globe-earthquake-plot-in-python-b0b52b646f27

