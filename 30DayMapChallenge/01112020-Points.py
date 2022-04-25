
import pandas as pd 
import matplotlib.pyplot as plt 
import descartes
import geopandas as gpd 
from shapely.geometry import Point, Polygon


map_india=gpd.read_file(r'C:\Users\vivek\Documents\Code\local-items\30daymapchallenge-data\india\states\Indian_States.shp')
fig, ax = plt.subplots(figsize=(15,15))
#map.plot(ax=ax)
map=map.to_crs(crs='epsg:4326')
map.crs

# import data
df=pd.read_csv(r'C:\Users\vivek\Documents\Code\local-items\30daymapchallenge-data\india\India-cities-population.csv')
# convert lat, lon to geography (point)
points=df.apply(lambda row: Point(row.lng, row.lat), axis=1)
# create a new gpd.df from existing pd.df and geography
cities=gpd.GeoDataFrame(df, crs={'init':'epsg:4326'}, geometry=points)
# check current crs
cities.crs 
# plot the data
# cities.plot()


# funciton for annotating
def city_info(id):
    top_cities=cities[cities.population>=5000000]
    top_cities_sel_col=top_cities[['city','population','lat','lng']]
    return top_cities_sel_col.iloc[id]
def coord(id):
    return (city_info(i).lng - 0.25, city_info(i).lat - 0.25)
def coord_txt(id):
    if i in [6, 0, 4]:
        return (city_info(i).lng - 1.5, city_info(i).lat - 1.5)
    if i in [1]:
        return (city_info(i).lng - 3, city_info(i).lat + 3)
    if i in [2, 5, 3]:
        return (city_info(i).lng + 9, city_info(i).lat - 1.5)


# Indian cities with population more than a 100k
fig, ax = plt.subplots(figsize=(17,20))
#ax.grid(True)
ax.grid(color='steelblue', linestyle='-.', linewidth=0.50)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
#fig.suptitle('Indian Cities: Population', fontsize=50)
plt.title(label='Indian Cities with Population > 100k\nCities with Population > 5M (highlighted in Red)',
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
cities[cities.population<5000000].plot(ax=ax, markersize=150, c=df.population, cmap='Blues' , marker='o')
cities[cities.population>=5000000].plot(ax=ax, markersize=250, color='Crimson') #c=df.population, cmap='Reds' , marker='o')

for i in range(7):
    ax.annotate('['+str(i)+'] '+city_info(i).city, coord(i), #(city_info(i).lng - 0.25, city_info(i).lat - 0.25),
                xytext=coord_txt(i), # (city_info(i).lng - 1.5, city_info(i).lat - 1.5),
                #textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=25,
                horizontalalignment='right', verticalalignment='top')



