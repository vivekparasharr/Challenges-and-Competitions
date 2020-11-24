
# Let’s make a map! Using Geopandas, Pandas and Matplotlib to make a Choropleth map
# https://towardsdatascience.com/lets-make-a-map-using-geopandas-pandas-and-matplotlib-to-make-a-chloropleth-map-dddc31c1983d

import pandas as pd 
import matplotlib.pyplot as plt 
import geopandas as gpd
from shapely.geometry import Point, Polygon
import adjustText as aT

map_df=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/statistical-gis-boundaries-london/ESRI/London_Borough_Excluding_MHW.shp')
map_df=map_df.to_crs(crs='epsg:4326')
map_df.head()
map_df.plot()

df = pd.read_csv('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Data/london-borough-profiles.csv', encoding='unicode_escape', header=0)
df = df[['Area_name',
         'Happiness_score_2011-14_(out_of_10)',
         'Anxiety_score_2011-14_(out_of_10)',
         'Population_density_(per_hectare)_2017',
         'Mortality_rate_from_causes_considered_preventable_2012/14'
         ]]
df.columns=['borough', 'happiness', 'anxiety', 'pop_density_per_hectare', 'mortality']

# join the geodataframe with the cleaned up csv dataframe
merged = map_df.set_index('NAME').join(df.set_index('borough'))
merged.head()

# Map time!
# set a variable that will call whatever column we want to visualise on the map
variable = 'pop_density_per_hectare'

# set the range for the choropleth
vmin, vmax = 120, 220

# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(10, 6))
merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')
ax.axis('off')

# add a title
ax.set_title('Preventable death rate in London', fontdict={'fontsize': '25', 'fontweight' : '3'})

# create an annotation for the data source
ax.annotate('Source: London Datastore, 2014',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')

# Create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
# empty array for the data range
sm._A = []
# add the colorbar to the figure
cbar = fig.colorbar(sm)


fig.savefig('map_export.png', dpi=300)



#########################

import os

# How to make a gif map using Python, Geopandas and Matplotlib
# https://towardsdatascience.com/how-to-make-a-gif-map-using-python-geopandas-and-matplotlib-cd8827cefbc8
'''
    load in shapefile
    load csv of data to visualise
    join the two dataframes
    plot the map and start to style it.
'''

map_df=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/statistical-gis-boundaries-london/ESRI/London_Borough_Excluding_MHW.shp')
map_df=map_df.to_crs(crs='epsg:4326')

df = pd.read_csv('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Data/MPS_Borough_Level_Crime_Historic.csv')

# join the geodataframe with the cleaned up csv dataframe
merged1 = map_df.set_index('NAME').join(df.set_index('borough'))


# save all the maps in the charts folder
output_path = '/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/22112020-Movement/maps'

# counter for the for loop
i = 0

# list of years (which are the column names at the moment)
list_of_years = ['200807','200907','201007','201107','201207','201307','201407','201507','201607']

# set the min and max range for the choropleth map
#vmin, vmax = 200, 1200
vmin, vmax = 10, 150

# start the for loop to create one map per year
for year in list_of_years:
    # create map, UDPATE: added plt.Normalize to keep the legend range the same for all maps
    fig = merged1.plot(column=year, cmap='Reds', figsize=(10,10), linewidth=0.8, 
                       edgecolor='0.8', vmin=vmin, vmax=vmax,
                       legend=True, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    # remove axis of chart
    fig.axis('off')
    
    # add a title
    fig.set_title('Violent crimes in London', fontdict={'fontsize': '25', 'fontweight' : '3'})

    # create an annotation for the year by grabbing the first 4 digits
    only_year = year[:4]    # position the annotation to the bottom left
    fig.annotate(only_year,
            xy=(0.1, .225), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=35)
    
    # this will save the figure as a high-res png in the output path. you can also save as svg if you prefer.
    filepath = os.path.join(output_path, year+'_violence.png')
    fig.get_figure().savefig(filepath, dpi=300)

    
##########
##########

import os

# How to make a gif map using Python, Geopandas and Matplotlib
# https://towardsdatascience.com/how-to-make-a-gif-map-using-python-geopandas-and-matplotlib-cd8827cefbc8
'''
    load in shapefile
    load csv of data to visualise
    join the two dataframes
    plot the map and start to style it.
'''

map_df=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/statistical-gis-boundaries-london/ESRI/London_Borough_Excluding_MHW.shp')
map_df=map_df.to_crs(crs='epsg:4326')

df = pd.read_csv('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Data/census-historic-population-borough.csv')

# join the geodataframe with the cleaned up csv dataframe
merged1 = map_df.set_index('NAME').join(df.set_index('Area Name'))


# save all the maps in the charts folder
output_path = '/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/22112020-Movement/maps'

# counter for the for loop
i = 0

# list of years (which are the column names at the moment)
'''
'Persons-1821','Persons-1831','Persons-1841','Persons-1851',
                 'Persons-1861','Persons-1871','Persons-1881','Persons-1891',
                 'Persons-1901',
'''
list_of_years = ['Persons-1911','Persons-1921','Persons-1931',
                 'Persons-1939','Persons-1951','Persons-1961','Persons-1971',
                 'Persons-1981','Persons-1991','Persons-2001','Persons-2011']

# set the min and max range for the choropleth map
vmin, vmax = 2000, 600000
#vmin, vmax = 10, 150

# start the for loop to create one map per year
for year in list_of_years:
    # create map, UDPATE: added plt.Normalize to keep the legend range the same for all maps
    fig = merged1.plot(column=year, cmap='Reds', figsize=(10,10), linewidth=0.8, 
                       edgecolor='0.8', vmin=vmin, vmax=vmax,
                       legend=True, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    # remove axis of chart
    fig.axis('off')
    
    # add a title
    fig.set_title('Population of London (1911-2011)', fontdict={'fontsize': '20', 'fontweight' : '3'})

    # create an annotation for the year by grabbing the first 4 digits
    only_year = year[-4:]    # position the annotation to the bottom left
    fig.annotate(only_year,
            xy=(0.1, .225), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=25)
    
    fig.annotate('#30DayMapChallenge - Day 22 - Movement \nhttps://twitter.com/vivekparasharr/ \nData from https://data.london.gov.uk/',
            xy=(0.1, .125), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=15)
    
    # this will save the figure as a high-res png in the output path. you can also save as svg if you prefer.
    filepath = os.path.join(output_path, year+'_violence.png')
    fig.get_figure().savefig(filepath, dpi=300)


##########
##########

###############

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



