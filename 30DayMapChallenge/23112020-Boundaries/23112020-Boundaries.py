
# Letâ€™s make a map! Using Geopandas, Pandas and Matplotlib to make a Choropleth map
# https://towardsdatascience.com/lets-make-a-map-using-geopandas-pandas-and-matplotlib-to-make-a-chloropleth-map-dddc31c1983d

import pandas as pd 
import matplotlib.pyplot as plt 
import geopandas as gpd
from shapely.geometry import Point, Polygon
import adjustText as aT
import pycountry as pc
import numpy as np

countries=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Maps/natural_earth_vector/110m_cultural/ne_110m_admin_0_countries.shp')
countries=countries.to_crs(crs='epsg:4326')
countries.head()
countries.plot(alpha=0.4, color='lightgrey',  edgecolor = "dimgrey",)

df = pd.read_csv('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Data/country_x_language.csv', header=0) # encoding='unicode_escape', 
# add country code
def do_fuzzy_search(country):
    try:
        result = pc.countries.search_fuzzy(country)
    except Exception:
        return np.nan
    else:
        return result[0].alpha_3
df["country_code"] = df["Country"].apply(lambda country: do_fuzzy_search(country))


# join the geodataframe with the cleaned up csv dataframe
merged = countries.set_index('SOV_A3').join(df.set_index('country_code'))
merged.head()
merged[merged.Language=='Spanish'].plot()


# Map time!
fig, ax = plt.subplots(figsize=(20.5,10))
#ax.grid(True)
ax.grid(color='darkgoldenrod', linestyle='-.', linewidth=0.50)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
#fig.suptitle('Indian Cities: Population', fontsize=50)
plt.title(label='Predominantly Spanish Speaking Countries!',
fontdict={'fontsize': 24, #rcParams['axes.titlesize'],
 'fontweight': 'bold',
 'color': 'firebrick', #rcParams['axes.titlecolor'],
 'verticalalignment': 'baseline',})
 #'horizontalalignment': 'left'})
#ax.set(title='Indian Cities with Population > 100k')

#ax.xaxis.set_ticks([])
#ax.yaxis.set_ticks([])
#ax.xaxis.set_visible(False)
#ax.yaxis.set_visible(False)

countries.plot(ax=ax, alpha=0.4, color='grey',  edgecolor = "dimgrey",)
merged[merged.Language=='Spanish'].plot(ax=ax, alpha=0.7, color='firebrick')
#merged[merged.Language=='Arabic'].plot(ax=ax, alpha=0.7, color='yellow')

plt.text(35, -85, '#30DayMapChallenge - Day 23 - Boundaries \nhttps://twitter.com/vivekparasharr/ \nData from http://geocountries.com', fontsize=18)    

#za=terrain[terrain.featurecla=='Desert'][terrain.scalerank<=3]
#za.name[za.name=='RUB AL KHALI']='RUB AL KHALI'
za=merged[merged.Language=='Spanish']
za["center"] = za["geometry"].representative_point()  # centroid
za_points = za.copy()
za_points.set_geometry("center", inplace = True)

texts = []

for x, y, label in zip(za_points.geometry.x, za_points.geometry.y, za_points["Country"].str.title()):
    texts.append(plt.text(x, y, label, fontsize = 18, )) #color='saddlebrown'))

aT.adjust_text(texts, force_points=0.3, force_text=0.8, expand_points=(1,1), expand_text=(1,1), 
               arrowprops=dict(arrowstyle="-", color='grey', lw=0.5))







