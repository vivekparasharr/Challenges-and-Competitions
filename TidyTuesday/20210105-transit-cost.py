
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=12,9 # make the chart wider
import pycountry

df=pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-01-05/transit_cost.csv')
df.head()
df.info()

df.dropna(inplace=True) # Drop Rows with NaN Values
df.reset_index(drop=True) # After dropping rows you can Reset the Index

# Lets add full country names using the pycountry package 
# pycountry.countries.lookup('in').name
def f(row):
    try:
        return pycountry.countries.lookup(row.country).name
    except:
        return 'Not found'
def ff(row):
    try:
        return pycountry.countries.lookup(row.country).alpha_3
    except:
        return 'Not found'
df.loc[(df.country=='UK'),'country']='GB' # replace country = UK to country = GB as UK is not recognized a country code by pycountry
df['country_full'] = df.apply(f, axis=1) # call the function to get country using pycountry
df['country_alpha_3'] = df.apply(ff, axis=1) # call the function to get country using pycountry

# now lets summarize the data
# view 0: number of train lines by country
df.groupby('country_full').count()[['line']].plot(kind='bar')
# view 1: number of train lines by country - excluding china
df[~df.country.isin(['CN'])].groupby('country').count()[['line']].plot(kind='bar')
# view 2: number of train lines by country, bar chart will be stacked with cities of the countries
df[~df.country.isin(['CN','IN'])].groupby(['country','city']).count()[['line']].unstack('city').plot(kind='bar',stacked=True)
# view 3: pivot by country x start year showing number of lines
# df[df.country.isin(['CN','IN'])]\
df\
    .groupby(['country','start_year']).count()[['line']]\
    .reset_index()\
    .pivot(index='start_year', columns='country', values='line')\
    .plot()

df2 = df[df.country=='IN']\
    [['city','line','start_year','end_year']]\
        .dropna()\
            .set_index(['city','line'])

def fff(row, yr):
    if ( yr >= int(row[0]) and yr <= int(row[1]) ):
        return 1
    else:
        return 0
# new = s.apply(lambda num : num + 5) 
#df2['2009'] = df2[['start_year','end_year']].apply(fff, axis=1)
for i in range( ( int(df2.start_year.min()) - 2 )  ,  ( int(df2.end_year.max()) + 2 ) ):
    df2[str(i)] = df2.apply(fff, yr=i, axis=1) # we can pass additional values to the function by specifying them after the function name

df2.drop(['start_year','end_year'], axis=1, inplace=True) # drop start and end year

df2.reset_index(inplace=True)

years = list(range(2004,2028))
years = list(map(str, years))
df2 = pd.melt(df2, id_vars=['city','line'], value_vars=years, var_name='year', value_name='track_exists')

def ffff(row):
    return row[0]+" - "+row[1]
df2['city_line'] = df2.apply(ffff, axis=1)
df2.drop(['city','line'],axis=1, inplace=True)

import altair as alt
# Table Bubble Plot (Github Punch Card)
c1=alt.Chart(df2).mark_circle().encode(
    y=alt.Y('city_line:O', axis=alt.Axis(title='India: City + Line (Project) Name')),
    x=alt.X('year:O', axis=alt.Axis(title='Project Duration (Start year to End year)')),
    size='track_exists:Q'
).properties(
    height=600,
    width=350
)

# chart for hcat
df3 = df[df.country=='IN']\
    [['city','line','cost_km_millions','stations','length']]\
        .dropna()
def ffff(row):
    return row[0]+" - "+row[1]
df3['city_line'] = df3.apply(ffff, axis=1)
df3.drop(['city','line'],axis=1, inplace=True)

chart2 = alt.Chart(df3).mark_bar().encode(
    y=alt.Y('city_line:O', axis=alt.Axis(labels=False)),
    x=alt.X('cost_km_millions:Q', axis=alt.Axis(format='$~s', title='Cost/Km (USD Mn)'))
#    y=alt.Y('petalWidth:Q', bin=alt.Bin(maxbins=30)),
#    color='species:N'
).properties(
    height=600,
    width=100
)

chart3 = alt.Chart(df3).mark_bar().encode(
    y=alt.Y('city_line:O', axis=alt.Axis(labels=False)),
    x=alt.X('stations:Q', axis=alt.Axis(format='~s', title='Number of Stations'))
#    y=alt.Y('petalWidth:Q', bin=alt.Bin(maxbins=30)),
#    color='species:N'
).properties(
    height=600,
    width=100
)

chart4 = alt.Chart(df3).mark_bar().encode(
    y=alt.Y('city_line:O', axis=alt.Axis(labels=False)),
    x=alt.X('length:Q', axis=alt.Axis(format='~s', title='Line Length (Km)'))
#    y=alt.Y('petalWidth:Q', bin=alt.Bin(maxbins=30)),
#    color='species:N'
).properties(
    height=600,
    width=100
)

c1 | chart2 | chart3 | chart4

# length - Length of proposed line in km
# tunnel_per - Percent of line length completed
# tunnel - Tunnel length of line completed in km 
# stations - Number of stations where passengers can board/leave
# cost_km_millions - Cost/km in millions of USD
def fffff(row):
    return row[2]+" - "+row[3]
df['city_line'] = df.apply(fffff, axis=1)
df[df.country=='IN'][['city_line','start_year','length', 'tunnel_per', 'tunnel', 'stations', 'cost_km_millions']]

# by year -> cost per km for india, china and rest of the world 
# segment the countries into india, china and rest-of-the-world
def in_cn_row(row):
    if row[1]=='IN' or row[1]=='CN':
        return row[1]
    else:
        return 'RoW'
df['in_cn_row']=df.apply(in_cn_row, axis=1)
# crate a flag which shows if the line has more than x% tunnel 
def tunnel_or_not(row):
    if float(row[8].strip('%')) > 0:
        return 'Yes'
    else:
        return 'No'
df['tunnel_or_not'] = df.apply(tunnel_or_not, axis=1)

source = df.groupby(['in_cn_row','start_year','tunnel_or_not']).mean()[['cost_km_millions']].reset_index()
c2=alt.Chart(source).mark_line().encode(
    x='start_year:O',
    y='cost_km_millions:Q',
    color='in_cn_row:O',
    strokeDash='tunnel_or_not',
)
# Seems like the cost of lines with tunnels is slightly higher in India and China but significantly higher for rest of the world. 

# by number of stations -> cost per km for india, china and rest of the world 
source = df.groupby(['in_cn_row','stations','tunnel_or_not']).mean()[['cost_km_millions']].reset_index()
c3=alt.Chart(source).mark_line().encode(
    x='stations:O',
    y='cost_km_millions:Q',
    color='in_cn_row:O',
    strokeDash='tunnel_or_not',
)

c1 & c2