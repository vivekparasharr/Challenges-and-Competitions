
import pandas as pd
capacity = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-05-03/capacity.csv')
df = capacity
df.head(5)
df.type.unique()

df.groupby(by=['year'], dropna=False)['total_gw'].sum().plot(kind='bar')

import plotly.express as px
fig = px.bar(df, x="year", y="total_gw", color="type", title="US Solar/Wind Capacity", width=650, height=450)
fig.add_annotation(dict(xref='paper',yref='paper',x=-0.105,y=1.155,xanchor='left',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Plant-level data from the U.S. fleet of ground-mounted photovoltaic (PV), PV+battery,'))
fig.add_annotation(dict(xref='paper',yref='paper',x=-0.105,y=1.095,xanchor='left',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='and concentrating solar-thermal power (CSP) plants with capacities exceeding 5 MWAC'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.2,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#30DayChartChallenge-2022-04-05 and #TidyTuesday-2022-05-03 @ parashar.ca'))
fig.show()
