

### big mac geo analysis

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
plt.rcParams['figure.figsize']=12,9 # make the chart wider
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
import adjustText as aT
from h3 import h3

# load the base map
countries=gpd.read_file('/Users/vivekparashar/OneDrive/GitHub-OneDrive/Challenges-and-Competitions/30DayMapChallenge/Shapefiles/natural_earth_vector/110m_cultural/ne_110m_admin_0_countries.shp')
countries=countries.to_crs(crs='epsg:4326')

# load the data
df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-12-22/big-mac.csv')
df.date = pd.to_datetime(df.date, format = '%Y-%m-%d') # convert date to datetime
df2 = df[df.date=='2020-07-01'][['iso_a3','dollar_price']].set_index('iso_a3') # and take the most recent burger price (as of July 2020)
#df2=df.groupby("iso_a3").mean()[["dollar_price"]] # pivot data by country and take mean burger price

# join the geodataframe with the cleaned up csv dataframe
merged = countries.set_index('ADM0_A3').join(df2)
merged = merged.dropna(subset=['dollar_price'])

# Plotting
fig, ax = plt.subplots(figsize=(20.5,10))
ax.grid(color='darkgoldenrod', linestyle='-.', linewidth=0.50)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
plt.title(label='Price of a Big Mac (as of July 2020)!',
fontdict={'fontsize': 24, 
 'fontweight': 'bold',
 'color': 'firebrick',
 'verticalalignment': 'baseline',})
countries.plot(ax=ax, alpha=0.4, color='grey',  edgecolor = "dimgrey",)
merged.plot(ax=ax, column='dollar_price', cmap='Reds', vmin=1.8, vmax=6.4 )
plt.text(10, -95, '#TidyTuesday - 2020-12-22 - Big Mac Index 2020-07-01 \nhttps://twitter.com/vivekparasharr/ \nData from http://geocountries.com', fontsize=18)    

# prepare column for labels
merged['dollar_price_rounded'] = round(merged.dollar_price, 2)
merged['merged_label'] = merged.NAME + ", $" + merged.dollar_price_rounded.apply(str)

# add labels
za=merged
za["center"] = za["geometry"].representative_point()  # centroid
za_points = za.copy()
za_points.set_geometry("center", inplace = True)
texts = []
for x, y, label in zip(za_points.geometry.x, za_points.geometry.y, za_points["merged_label"].str.title()):
    texts.append(plt.text(x, y, label, fontsize = 10, )) 
aT.adjust_text(texts, force_points=0.3, force_text=0.8, expand_points=(1,1), expand_text=(1,1), 
               arrowprops=dict(arrowstyle="-", color='grey', lw=0.5))

#########################################################################

### big mac analysis 

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=11,7 # make the chart wider

df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-12-22/big-mac.csv')
# convert date to datetime
df.date = pd.to_datetime(df.date, format = '%Y-%m-%d')

df.head()
df.info()

df2 = df.groupby(['name', 'date'])\
    .mean()[['local_price', 'dollar_price']]\
    .reset_index()

df2.name.unique()

df2[df2.name.isin(['Chile', 'India', 'Canada', 'China', 'Australia', \
    'United States', 'Britain', 'Brazil', 'Japan'])]\
    .pivot(index='date', columns='name', values='dollar_price')\
    .plot(legend='best')

df2[df2.name.isin(['Chile', 'India', 'Canada', 'United States'])]\
    .pivot(index='date', columns='name', values='dollar_price')\
    .plot(legend='best')

df2[df2.name.isin(['Chile', 'Brazil', 'Peru', 'Argentina', 'Mexico', 'Uruguay'])]\
    .pivot(index='date', columns='name', values='dollar_price')\
    .plot(legend='best')

df2[df2.name.isin(['Canada'])]\
    .pivot(index='date', columns='name', values=['local_price','dollar_price'])\
    .plot(legend='best', subplots=True)

# New approach

def cagr(first, last, periods):
    return (last/first)**(1/periods)-1

df3 = df.groupby(['name', 'date']).mean()[['dollar_price']].reset_index()
df3_pivoted = df3.pivot(index='date', columns='name', values='dollar_price')
df3_pivoted.dropna(axis=1)
df3_pivoted.fillna()

# Taking care of missing data
# https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
# dff.fillna(dff.mean()["B":"C"])
# df3_pivoted.fillna(df3_pivoted.mean()["Azerbaijan":"Bahrain"])
df3_pivoted = df3_pivoted.where(pd.notna(df3_pivoted), df3_pivoted.min(), axis="columns")

df3_pivoted[['India','Chile','Canada','United States']].plot()

