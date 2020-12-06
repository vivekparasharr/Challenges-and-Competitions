
import pandas as pd 
import altair as alt

# import data
shelters = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-12-01/shelters.csv')

# see summary of data
shelters.info()

# convert datetime column
shelters['occupancy_date'] = pd.to_datetime(shelters['occupancy_date'])

# line plot showing occupancy/capacity over time
shelters.groupby('occupancy_date').mean()[['occupancy','capacity']].plot() # ,xlim=(0,20),ylim=(0,100)

# mean occupancy/capacity by by sector
shelters[shelters.occupancy_date=='2017-01-01'].groupby('sector').mean()[['occupancy','capacity']].plot(kind='bar')
shelters[shelters.occupancy_date=='2019-12-31'].groupby('sector').mean()[['occupancy','capacity']].plot(kind='bar')


shelters[shelters.program_name.str.contains('Extreme')]



shelters.groupby('organization_name')

shelters.groupby('sector').mean()[['occupancy', 'capacity']]
shelters.groupby('shelter_postal_code').mean()['capacity'].plot(kind='bar')

shelters.groupby('sector').get_group('Men')


shelters[shelters.facility_name=='Scott Mission - 502 Spadina Ave'].iloc[:10].plot(x='occupancy_date', y='occupancy', color='program_name', kind='line', rot=60)

source=shelters[shelters.facility_name=='Scott Mission - 502 Spadina Ave'].iloc[:40]
alt.Chart(source).mark_line().encode(
    x=alt.X('occupancy_date', axis=alt.Axis(title='Occupancy Date')),
    y=alt.Y('occupancy', axis=alt.Axis(title='Occupancy'), scale=alt.Scale(domain=(15, 55))),
    color=alt.Color('program_name', legend=alt.Legend(orient="bottom")),
    strokeDash='program_name',
)

shelters.nunique()

# org run multiple shelter > facility > program
shelters.groupby('organization_name').nunique()[['shelter_name', 'facility_name', 'program_name']].sort_values(by=['shelter_name'], ascending=False)



