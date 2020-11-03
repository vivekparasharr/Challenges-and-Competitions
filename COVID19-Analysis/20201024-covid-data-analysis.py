
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
df.columns


# Mean, median and min sales by country
df.pivot_table(index=['Country'], values=['Sales'], aggfunc={'median','mean','min'})
df.pivot_table(index=['Country'], values=['Sales'], aggfunc={'median','mean','min'}).plot()

# Groupby has some of similar funcitonality
df.groupby(['Country']).mean()['Sales'].plot() # can specify a specific column to find mean of. Here we do mean(sales)


df.pivot_table(index=['location'], values=[''])

df.groupby(['location']).count()

# Top 10 countries with Diabetes prevalence
df[['location','diabetes_prevalence']].drop_duplicates().sort_values(by='diabetes_prevalence').head(10).plot(x='location', y='diabetes_prevalence', kind='bar')

# Unique list of countries
location = df[['location']].drop_duplicates()

# Focus on 1 country - India
temp=df.loc[df.location=='India']
temp.plot(x='date', y='new_cases', rot=45, kind='bar')
plt.title('India case evolution')
plt.xlabel('Time')
plt.ylabel('New cases')

temp2=df[['date','new_cases']] # select cols of interest
temp2.set_index("date", inplace=True)
temp2.index = pd.to_datetime(temp2.index)

temp3=temp2.resample(rule='W').mean()
temp3.plot( rot=45, kind='bar')


# Lets get total cases by country and diabetes prevalance and other factors to see corelation
# Lets identify 20 countries with most cases
df.date.max() # '2020-10-24'
df2=df.loc[df.date=='2020-10-24']

df[['total_deaths','diabetes_prevalence']].plot(y='total_deaths',x='diabetes_prevalence', kind='scatter')
df[['total_deaths','population']].plot(y='total_deaths',x='population', kind='scatter')

temp=df.groupby(['location']).sum()['new_cases'].sort_values(ascending=False).head(21)

temp=df.groupby(['location']).mean()['diabetes_prevalence']

df.columns






