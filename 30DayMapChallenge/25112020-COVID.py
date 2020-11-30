
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon
import adjustText as aT


df_full=pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
df_full.columns
df_full.head(5)

# exclude rows with owid grouping of countries, eg. owid world
df2=df_full[['iso_code', 'date', 'total_cases']]
df2[df2.iso_code != 'OWID_WRL'][df2.iso_code != 'OWID_KOS'].iso_code.unique()
df3=df2[df2.iso_code != 'OWID_WRL'][df2.iso_code != 'OWID_KOS'][df2.iso_code.notna()]

# select specific dates (bi-weekly snapshots)
snapshot_dates=['2019-12-31',
                '2020-01-15','2020-01-31',
                '2020-02-15','2020-02-29',
                '2020-03-15','2020-03-31',
                '2020-04-15','2020-04-30',
                '2020-05-15','2020-05-31',
                '2020-06-15','2020-06-30',
                '2020-07-15','2020-07-31',
                '2020-08-15','2020-08-31',
                '2020-09-15','2020-09-30',
                '2020-10-15','2020-10-31',
                '2020-11-15']
df4=df3[df3.date.isin(snapshot_dates)]
df4.reset_index(drop=True) # drop=True removes previous index, otherwise the previous index would become a column

df=df4.pivot(index='iso_code', columns='date')
df.columns = df.columns.droplevel()
df=df.reset_index()
df=df.fillna(0)
df[df['iso_code']=='CHN'].values
'''
np.array([['CHN', 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 
10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 
10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 
10000000 ]])
'''
map_df=gpd.read_file('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/30DayMapChallenge/Shapefiles/natural_earth_vector/110m_cultural/ne_110m_admin_0_countries.shp')
map_df=map_df.to_crs(crs='epsg:4326')
map_df.head()
map_df.plot()


merged = map_df.set_index('ADM0_A3').join(df.set_index('iso_code'))
merged.head()

# alternative way of joining
# merged = map_df.merge(df, left_on='ADM0_A3', right_on='iso_code', how='left')

# save all the maps in the charts folder
output_path = '/Users/vivekparashar/Downloads/all_charts'

vmin, vmax = 100.0, 1000000.0
# counter for the for loop
i = 0
# start the for loop to create one map per year
for date in snapshot_dates:
    #fig, ax = plt.subplots(figsize=(25,10))
    #map_df.plot(ax=ax, alpha=0.4, color='grey',  edgecolor = "lightgrey",)
    # create map, UDPATE: added plt.Normalize to keep the legend range the same for all maps
    fig = merged.plot( column=date, figsize=(25,10), cmap='Reds', linewidth=0.8, 
                       edgecolor='0.8', vmin=vmin, vmax=vmax,
                       #facecolor='w',
                       legend=True, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    # remove axis of chart
    fig.axis('off')
    #ax.xaxis.set_ticks([])
    #ax.yaxis.set_ticks([])
    #ax.xaxis.set_visible(False)
    #ax.yaxis.set_visible(False)
    
    # add a title
    fig.set_title('Total Cases of Coronavirus (Dec 2019-Nov 2020)', fontdict={'fontsize': '40', 'fontweight' : '3'})

    # create an annotation for the year by grabbing the first 4 digits
    fig.annotate(date,
            xy=(0.1, .225), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=25)
    
    fig.annotate('#30DayMapChallenge - Day 25 - COVID19 \nhttps://twitter.com/vivekparasharr/ \nData from ourworldindata.org \nMax capped at 1M cases per country',
            xy=(0.1, .15), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=20)
    
    # this will save the figure as a high-res png in the output path. you can also save as svg if you prefer.
    filepath = os.path.join(output_path, date+'_covid19.png')
    fig.get_figure().savefig(filepath, dpi=100, facecolor='w')

