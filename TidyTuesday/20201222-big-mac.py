
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

'Argentina', 'Brazil','Chile',

'Australia', 

'Azerbaijan', 'Bahrain', 

'Britain', 

'Canada',  'China', 'Colombia', 'Costa Rica',
       'Croatia', 'Czech Republic', 'Denmark', 'Egypt', 'Euro area',
       'Guatemala', 'Honduras', 'Hong Kong', 'Hungary', 'India',
       'Indonesia', 'Israel', 'Japan', 'Jordan', 'Kuwait', 'Lebanon',
       'Malaysia', 'Mexico', 'Moldova', 'New Zealand', 'Nicaragua',
       'Norway', 'Oman', 'Pakistan', 'Peru', 'Philippines', 'Poland',
       'Qatar', 'Romania', 'Russia', 'Saudi Arabia', 'Singapore',
       'South Africa', 'South Korea', 'Sri Lanka', 'Sweden',
       'Switzerland', 'Taiwan', 'Thailand', 'Turkey', 'UAE', 'Ukraine',
       'United Arab Emirates', 'United States', 'Uruguay', 'Vietnam'


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

