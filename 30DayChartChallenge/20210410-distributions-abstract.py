
import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_beer_consumption_per_capita')[2]
df.columns=['Country', 'ConsumptionPerCapitaLitresPerYear',
       '2018changelitresperyear',
       'Totalnationalconsumptionmillionlitresperyear', 'Year',
       'Sources']

# add continent
from countryinfo import CountryInfo
def foo(ctry_nm):
    try:
        return CountryInfo(ctry_nm).region()
    except:
        return 'NA'
df['continent'] = [foo(x) for x in df['Country']]

# select data to plot
df = df[df.continent == 'Europe']
df = df[['Country','ConsumptionPerCapitaLitresPerYear']]

# Prepare data
df['x'] = 1
df['consumption_diff']=df.ConsumptionPerCapitaLitresPerYear.diff(periods=-1)
df.consumption_diff[df.Country=='Italy'] = df.ConsumptionPerCapitaLitresPerYear[df.Country=='Italy']

# Plot 1
import plotly.express as px
fig = px.bar(df, x='x', y="consumption_diff", color="Country", 
      title="Long-Form Input")
fig.show()

# Plot 2
import plotly.graph_objects as go
fig = go.Figure(data=[go.Bar(
            x=df.x.to_list()[::-1], y=df.consumption_diff.to_list()[::-1],
            text=df.Country.to_list()[::-1],
            textposition='auto',
        )])
fig.show()
