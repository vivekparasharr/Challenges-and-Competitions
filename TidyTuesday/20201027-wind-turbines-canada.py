# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:04:37 2020

@author: vivek
"""


import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=6.4, 4.8

import numpy as np
import seaborn as sns
sns.set_theme(style="ticks", palette="pastel")

df=pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-10-27/wind-turbine.csv')

df.columns
'''
['objectid', 'province_territory', 'project_name',
       'total_project_capacity_mw', 'turbine_identifier',
       'turbine_number_in_project', 'turbine_rated_capacity_k_w',
       'rotor_diameter_m', 'hub_height_m', 'manufacturer', 'model',
       'commissioning_date', 'latitude', 'longitude', 'notes']
'''

# obviously - 
# total_project_capacity_mw = sum (turbine_rated_capacity_k_w)

# handle overlapping years
df.commissioning_date.replace(
['2000/2001','2001/2003','2002/2006','2004/2005','2005/2006/2012','2006/2007',
 '2006/2008','2006/2008','2011/2012','2013/2014','2014/2015'],
['2000','2001','2002','2004','2005','2006',
 '2006','2006','2011','2013','2014'],
inplace=True)

# Alternate way to handle overlapping years
df['commissioning_date'] = df['commissioning_date'].map({'2000/2001': '2000', 
                                                       '2001/2003': '2001'})


# province level views
# total capacity by province
cap_by_prov=df.groupby(['province_territory']).sum()['turbine_rated_capacity_k_w']
ax=cap_by_prov.sort_values(ascending=False).plot(kind='bar')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Province')
ax.set_ylabel('Total Capacity (MW)')
ax.set_title('Total Wind Energy Cap by Province')
#ax.set_xticks(x)
#ax.set_xticklabels(labels)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
#ax.legend()


# number of projects by province
proj_by_prov=df.groupby(['province_territory']).nunique()['project_name']
proj_by_prov.sort_values(ascending=False).plot(kind='bar')

# pandas groupby - apply different functions on different columns
# MultiIndex / advanced indexing
# province level grouping
prov_grouping=df.groupby(['province_territory']).agg({
    'turbine_rated_capacity_k_w':['sum','mean'], # total and mean turbine capacity by province
    'project_name':'nunique', # number of projects in province 
    'objectid':'nunique', # number of turbines in province 
    'manufacturer':'nunique'}) # number of manufacturers in province

prov_grouping.columns
prov_grouping.turbine_rated_capacity_k_w.sum
prov_grouping.plot(subplots=True, layout=(1,2))
prov_grouping.iloc[:,1].sort_values(ascending=False).plot(kind='bar')

sns.relplot(data=prov_grouping, kind='boxplot',
            x='Years', y='Number of Medals', col='States', col_wrap=4,)

# PLOTTING PROVINCE DATA
# plotting multiple plots together
plt.rcParams['figure.figsize']=16,6   # default: 6.4, 4.8
fig, axs = plt.subplots(ncols=3) # nrows=2,

# Chart - avg turbine capacity by province
ax = sns.barplot(data=prov_grouping, 
                 x=prov_grouping.index, 
                 y=prov_grouping.iloc[:,1],ax=axs[2]) # ,ax=axs[0,0]
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
ax.set(xlabel='Province', ylabel='Avg Turbine Cap (kW)', title='Avg Turbine Cap by Province')

# Chart - total turbine capacity by province
ax = sns.barplot(data=prov_grouping, 
                 x=prov_grouping.index, 
                 y=prov_grouping.iloc[:,0],ax=axs[0])
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
ax.set(xlabel='Province', ylabel='Total Turbine Cap (MW)', title='Total Turbine Cap by Province')
'''
## figure out this error
# NotImplementedError: Index._join_level on non-unique index is not implemented
# Chart - number of projects by province
ax = sns.barplot(data=prov_grouping, 
                 x=prov_grouping.index, 
                 y=prov_grouping.iloc[:,2],ax=axs[1]) # prov_grouping['project_name']['nunique']
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
ax.set(xlabel='Province', ylabel='Number of Projects', title='Number of Projects by Province')
'''
# Chart - number of turbines by province
ax = sns.barplot(data=prov_grouping, 
                 x=prov_grouping.index, 
                 y=prov_grouping.iloc[:,3],ax=axs[1])
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
ax.set(xlabel='Province', ylabel='Number of Turbines', title='Number of Turbines by Province')
'''
# Num of turbines x Total capacity - scatter plot of provinces
ax=sns.scatterplot(data=prov_grouping, 
                 x=prov_grouping.iloc[:,0], 
                 y=prov_grouping.iloc[:,3],hue=prov_grouping.index, 
                 ax=axs[2])                   
ax.set(xlabel='Total Turbine Cap (MW)', ylabel='Number of Turbines', title='Number of Turbines x Total Cap')
'''



# manufacturer level views
# number of turbines by manufacturer
turb_by_manuf=df.groupby(['manufacturer']).count()['objectid'].sort_values(ascending=False)
turb_by_manuf[turb_by_manuf>500]
turb_by_manuf= pd.DataFrame({'manufacturer': ['Vestas', 'GE', 'Siemens', 'Enercon', 'Senvion', 'Others'],
                    'turbines': [1834,1725,1248,960,643,286]})

ax=turb_by_manuf.plot(kind='bar')
ax.set_xticklabels(turb_by_manuf.manufacturer, rotation=45, horizontalalignment='right')
ax.text(4.6, 400, 'Other has \n18 manuf-\nacturers', fontsize=10, style='italic',
        bbox={'facecolor': 'salmon', 'alpha': 0.5, 'pad': 4})
ax.set(xlabel='Manufacturer', ylabel='Number of Turbines', title='Number of Turbines by Manufacturer')
plt.xticks(rotation=45, horizontalalignment="right")


manuf_grouping=df.groupby(['manufacturer']).agg({
    'turbine_rated_capacity_k_w':['sum','mean'],  # total and avg capacity of turbines installed by manufacturer
    'project_name':'nunique', # number of projects by manufacturer
    'province_territory':'nunique'}) # number of provinces manufacturer operates in 



# commmission date level views
# projects started by commissioning_date
proj_by_comm_dt=df.groupby(['commissioning_date']).nunique()['project_name']
ax=proj_by_comm_dt.plot(kind='bar')
ax.text(9.6, 30, '2010-16 seems\nto be a period\nof boom', fontsize=10, style='italic',
        bbox={'facecolor': 'salmon', 'alpha': 0.5, 'pad': 4})
ax.set(xlabel='Year', ylabel='Number of Projects', title='Number of Projects by Year')


# turbines installed by commissioning_date
turb_by_comm_dt=df.groupby(['commissioning_date']).count()['objectid']
ax=turb_by_comm_dt.plot(kind='bar')
ax.text(9.6, 800, '2010-16 seems\nto be a period\nof boom', fontsize=10, style='italic',
        bbox={'facecolor': 'salmon', 'alpha': 0.5, 'pad': 4})
ax.set(xlabel='Year', ylabel='Number of Turbines', title='Number of Turbines by Year')



# turbine level views
# top 10 projects by number of turbines
top_proj_by_num_turb=df.groupby(['project_name']).count()['objectid']
top_proj_by_num_turb.sort_values(ascending=False).describe()
top_proj_by_num_turb.sort_values(ascending=False).median()

ax=top_proj_by_num_turb.plot(kind='box')
ax.text(1.1, 10, 'Avg 25 turbines per proj\n50% of proj <= 9 turbines\nLargest proj has 175 turbines', fontsize=10, style='italic',
        bbox={'facecolor': 'salmon', 'alpha': 0.5, 'pad': 4})
ax.set(xlabel='Boxplot', ylabel='Number of Turbines', title='Number of Turbines by Project')


ax=top_proj_by_num_turb.plot(kind='hist', bins=30)
ax.text(50, 45, 'Higher concentration of projects\nwith <= 20 turbines\nLets focus on them', fontsize=10, style='italic',
        bbox={'facecolor': 'salmon', 'alpha': 0.5, 'pad': 4})
ax.set(xlabel='Histogram', ylabel='Number of Turbines', title='Histogram of Number of Turbines by Project')


ax=top_proj_by_num_turb[top_proj_by_num_turb<=20].plot(kind='hist')
ax.text(10, 30, 'Still higher concentration of projects\nwith <= 10 turbines', fontsize=10, style='italic',
        bbox={'facecolor': 'salmon', 'alpha': 0.5, 'pad': 4})
ax.set(xlabel='Histogram', ylabel='Number of Turbines', title='Histogram of Number of Turbines by Project (<20 turbines)')


top_proj_by_num_turb.sort_values(ascending=False).head(10)

# top 10 projects by capacity
top_proj_by_cap=df.groupby(['project_name']).sum()['turbine_rated_capacity_k_w']
top_proj_by_cap.sort_values(ascending=False).head(10)

# correlation between turbine rated capacity and diameter/height of turbine


# geographical data
lat/lon to plot projects 
lat/lon to plot turbine volume


import geopandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings('ignore')

%matplotlib inline

geopandas.datasets.available

world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
print("Geometry Column Name : ", world.geometry.name)
print("Dataset Size : ", world.shape)
world.head()


nybb = geopandas.read_file(geopandas.datasets.get_path("nybb"))
nybb.head()

world.plot(figsize=(12,8));

with plt.style.context(("seaborn", "ggplot")):
    nybb.plot(figsize=(12,8), color="white", edgecolor="grey");


world_happiness = pd.read_csv("world_happiness_2019.csv")
print("Dataset Size : ",world_happiness.shape)
world_happiness.head()


##################################

Adding latitude and longitudes to a map in Python involves two processes:
- import data file containing latitude and longitude features
- import map image as .shp file


import numpy as np
import pandas as pd


# import libraries
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
# import street map
street_map = gpd.read_file('lpr_000b16a_e.shp')

# designate coordinate system
crs = {'init':'espc:4326'}
# zip x and y coordinates into single feature
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
# create GeoPandas dataframe
geo_df = gpd.GeoDataFrame(df, crs = crs, geometry = geometry)



###################################################


import altair as alt

# option 1
alt.data_transformers.disable_max_rows() # Disabling MaxRowsError
# option 2
alt.data_transformers.enable('json') # save data to a local filesystem and reference the data by file path
alt.data_transformers.enable('csv')
# option 3
# pip install altair_data_server
# serve your data from a local threaded server to avoid writing datasets to disk
alt.data_transformers.enable('data_server') # enable the data transformer

import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-10-27/wind-turbine.csv')
df.columns
df.head(2)

# bar chart
d1=df.groupby(['province_territory']).sum()['turbine_rated_capacity_k_w']
d1=pd.DataFrame(d1) # Convert Series to DataFrame
d1.reset_index(level=0, inplace=True) # Convert Index to Column
alt.Chart(d1).mark_bar().encode(
    x='province_territory',
    y='turbine_rated_capacity_k_w'
)

# stacked bar chart
d11=df.groupby(['manufacturer','province_territory']).sum()['turbine_rated_capacity_k_w']
d11=pd.DataFrame(d11) # Convert Series to DataFrame
d11.reset_index(level=0, inplace=True) # Convert Index to Column
d11.reset_index(level=0, inplace=True) # Reset twice because there were two indexes in the DataFrame
alt.Chart(d11).mark_bar().encode(
    y='province_territory',
    x='turbine_rated_capacity_k_w',
    color='manufacturer'
)

# heatmap
d2=df.groupby(['province_territory','manufacturer']).count()['objectid']
d2=pd.DataFrame(d2) # Convert Series to DataFrame
d2.reset_index(level=0, inplace=True) # Convert Index to Column
d2.reset_index(level=0, inplace=True) # Reset twice because there were two indexes in the DataFrame
alt.Chart(d2).mark_rect().encode(
    x='province_territory',
    y='manufacturer',
    color='objectid'
)

# histogram
d3=df.groupby(['project_name']).nunique()['objectid']
d3=pd.DataFrame(d3) # Convert Series to DataFrame
d3.reset_index(level=0, inplace=True) # Convert Index to Column
alt.Chart(d3).mark_bar().encode(
    alt.X('objectid', bin=True),
    y='count()',
)

# line plot
d4=df.groupby(['commissioning_date','province_territory']).nunique()['objectid']
d4=pd.DataFrame(d4) # Convert Series to DataFrame
d4.reset_index(level=0, inplace=True) # Convert Index to Column
d4.reset_index(level=0, inplace=True) # Reset twice because there were two indexes in the DataFrame
alt.Chart(d4).mark_line().encode(
    x='commissioning_date',
    y='objectid',
    color='province_territory'
)

# scatter plot
d5=df.groupby(['project_name','rotor_diameter_m','hub_height_m']).nunique()['objectid']
d5=pd.DataFrame(d5) # Convert Series to DataFrame
d5.reset_index(level=0, inplace=True) # Convert Index to Column
d5.reset_index(level=0, inplace=True) # Reset thrice because there were three indexes in the DataFrame
d5.reset_index(level=0, inplace=True) # Reset thrice because there were three indexes in the DataFrame
alt.Chart(d5).mark_circle(size=60).encode(
    x='rotor_diameter_m',
    y='hub_height_m',
    color='objectid',
    tooltip=['project_name', 'rotor_diameter_m', 'hub_height_m', 'objectid']
).interactive()

# stacked area chart - not sure if this is showing what i intended to show
d6=df.groupby(['commissioning_date','province_territory']).sum()['turbine_rated_capacity_k_w']
d6=pd.DataFrame(d6) # Convert Series to DataFrame
d6['turbine_rated_capacity_k_w_cumulative']=d6['turbine_rated_capacity_k_w'].cumsum()
d6.reset_index(level=0, inplace=True) # Convert Index to Column
d6.reset_index(level=0, inplace=True) # Reset twice because there were two indexes in the DataFrame
alt.Chart(d6).mark_area().encode(
    x="commissioning_date:T",
    y="turbine_rated_capacity_k_w_cumulative:Q",
    color="province_territory:N"
)

# strip plot
d7=df.groupby(['province_territory','hub_height_m']).nunique()['objectid']
d7=pd.DataFrame(d7) # Convert Series to DataFrame
d7.reset_index(level=0, inplace=True) # Convert Index to Column
d7.reset_index(level=0, inplace=True) # Reset twice because there were two indexes in the DataFrame
alt.Chart(d7).mark_tick().encode(
    x='province_territory:N',
    y='hub_height_m:Q',
    tooltip=['province_territory', 'hub_height_m', 'objectid']
).interactive()




