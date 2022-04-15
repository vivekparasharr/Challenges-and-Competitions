
import numpy as np
import pandas as pd

forest = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-06/forest.csv')
forest_area = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-06/forest_area.csv')
df = forest

# add continent
from countryinfo import CountryInfo
def foo(ctry_nm):
    try:
        return CountryInfo(ctry_nm).region()
    except:
        return 'NA'
df['continent'] = [foo(x) for x in df['entity']]
df2 = df.groupby(['continent','year']).sum()[['net_forest_conversion']].reset_index()


import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[0, 2, 3, 5])) # fill down to xaxis
fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[3, 5, 1, 7], fill='tonexty')) # fill to trace0 y

fig.show()



# Plot
import plotly.graph_objects as go
fig = go.Figure()
for c in list(df.continent.unique()):
    fig.add_trace(go.Scatter(
        x=list(df2[df2.continent==c].year), 
        y=list(df2[df2.continent==c].net_forest_conversion),
        mode='lines+markers',
        #fill='tozeroy',
        name=c
    ))
#fig.update_layout(showlegend=False)
fig.update_layout(template="plotly_dark")
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.22,xanchor='center',yanchor='top', 
font=dict(family='Arial',size=22,color='grey'),showarrow=False, 
text='Net forest conversion in hectares'))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.085,xanchor='center',yanchor='top',
font=dict(family='Arial',size=14,color='grey'),showarrow=False,
text='Forest conversion is the clearing of natural forests (deforestation) to use the land for another purpose'))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.10,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='#30DayChartChallenge - space - 2021/04/19'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='Dataset from OurWorldInData.org'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.21,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
fig.show()


