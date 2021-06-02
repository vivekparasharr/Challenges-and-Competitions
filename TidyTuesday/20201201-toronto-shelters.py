
'''
.plot() has several optional parameters. Most notably, the kind parameter accepts eleven different string values and determines which kind of plot you’ll create:
    "area" is for area plots.
    "bar" is for vertical bar charts.
    "barh" is for horizontal bar charts.
    "box" is for box plots.
    "hexbin" is for hexbin plots.
    "hist" is for histograms.
    "kde" is for kernel density estimate charts.
    "density" is an alias for "kde".
    "line" is for line graphs.
    "pie" is for pie charts.
    "scatter" is for scatter plots.
'''

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
#import altair as alt

# import data
shelters = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-12-01/shelters.csv')

# see summary of data
shelters.info()

# convert datetime column
shelters['occupancy_date'] = pd.to_datetime(shelters['occupancy_date'])
shelters['occupancy_year'] = shelters.occupancy_date.dt.year
shelters['occupancy_month'] = shelters.occupancy_date.dt.month

# line plot showing occupancy/capacity over time
shelters.groupby('occupancy_date').mean()[['occupancy','capacity']].plot() # ,xlim=(0,20),ylim=(0,100)

# mean occupancy/capacity by by sector
shelters[shelters.occupancy_date=='2017-01-01'].groupby('sector').mean()[['occupancy','capacity']].plot(kind='bar')
shelters[shelters.occupancy_date=='2019-12-31'].groupby('sector').mean()[['occupancy','capacity']].plot(kind='bar')

# how num of org, shelters, facility, program have changed over time
shelters.groupby('occupancy_date').nunique()[['organization_name','shelter_name','facility_name','program_name']].plot() # ,xlim=(0,20),ylim=(0,100)

# seasonal - summer - j,j,a; fall - s,o,n; winter - d,j,f; spring - m,a,m
season_dict={6 : "summer", 7 :"summer", 8 : "summer",
            9 : "fall", 10 :"fall", 11 : "fall",
            12 : "winter", 1 :"winter", 2 : "winter",
            3 : "spring", 4 :"spring", 5 : "spring",} 
shelters['season'] = shelters['occupancy_month'].map(season_dict) 
shelters.groupby('season').mean()[['occupancy','capacity']].plot()

# Immigrant, Refugee and Extreme weather shelters
shelters['Immigrant']=shelters.organization_name.str.contains('Immigrant')
shelters['Refugee']=shelters.organization_name.str.contains('Refugee')
shelters['Extreme']=shelters.program_name.str.contains('Extreme')
# create new column using .apply and a function
def f(row):
    if row['Immigrant'] == True:
        val = 'Immigrant'
    elif row['Refugee'] == True:
        val = 'Refugee'
    elif row['Extreme'] == True:
        val = 'Extreme'
    else:
        val = 'Normal'
    return val
shelters['type'] = shelters.apply(f, axis=1)

shelters[shelters.occupancy_date=='2019-12-31'].groupby(['type'])\
    .sum()[['occupancy','capacity']]\
        .plot(y='occupancy', kind='pie',figsize=(12,7))
        #.plot(kind='pie', subplots=True)
        #df.set_index('x').plot()

# putting it all together using matplotlib
#plt.figure(figsize = (10,6))
fig, ax = plt.subplots(2,3)
fig.subplots_adjust(hspace=0.5)
fig.suptitle('Analysis of Toronto Shelters Data', fontsize=26, color='blue')
fig.text(0.75, 0.01, 'https://twitter.com/vivekparasharr', style = 'italic', fontsize = 10, color = "blue") 
shelters.groupby('occupancy_date').mean()[['occupancy','capacity']].plot(title='Capacity and Occupany over Time', ax=ax[0,0],figsize=(12,7)) # ,xlim=(0,20),ylim=(0,100)
shelters.groupby('occupancy_date').nunique()[['organization_name','shelter_name','facility_name','program_name']].plot(title='# of Orgs, Shelters, Facilities, Programs', ax=ax[0,1],figsize=(12,7)) # ,xlim=(0,20),ylim=(0,100)
shelters.groupby('season').mean()[['occupancy','capacity']].plot(title='Capacity and Occupancy over Time', ax=ax[0,2],figsize=(12,7))
shelters[shelters.occupancy_date=='2017-01-01'].groupby('sector').mean()[['occupancy','capacity']].plot(title='2017: Cap/Ocp by Sector', kind='bar', ax=ax[1,0],figsize=(12,7))
shelters[shelters.occupancy_date=='2019-12-31'].groupby('sector').mean()[['occupancy','capacity']].plot(title='2019: Cap/Ocp by Sector', kind='bar', ax=ax[1,1],figsize=(12,7))
shelters[shelters.occupancy_date=='2019-12-31'].groupby(['type']).sum()[['occupancy','capacity']].plot(title='2019: Occupancy by Type', y='occupancy', kind='pie', ax=ax[1,2],figsize=(12,7))
plt.savefig('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/TidyTuesday/Data/2020-12-01/20201201-Toronto-Shelters.png', dpi=300, facecolor='w')
plt.show()

'''
fig.subplots_adjust(..)
left  = 0.125  # the left side of the subplots of the figure
right = 0.9    # the right side of the subplots of the figure
bottom = 0.1   # the bottom of the subplots of the figure
top = 0.9      # the top of the subplots of the figure
wspace = 0.2   # the amount of width reserved for blank space between subplots
hspace = 0.2   # the amount of height reserved for white space between subplots
'''
