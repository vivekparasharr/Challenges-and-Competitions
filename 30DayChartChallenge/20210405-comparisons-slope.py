
import numpy as np
import pandas as pd
import plotly.express as px

energy = pd.read_csv('Data/per-capita-energy-use.csv')

# prepare data
energy = energy[energy.Entity.isin(['United Kingdom', 'United States', \
    'Australia', 'Chile', 'India'])]
energy = energy[energy.Year.isin(['1965', '2019'])]
energy.columns = ['country', 'code', 'year', 'value']
energy.value = energy.value.round()

# calculate variables for plot
df = energy
year1=1965
year2=2019
vp_offset = (year2 - year1)/2
year1val = df[df.year==1965].value.to_list()
year2val = df[df.year==2019].value.to_list()
cat1val = df[df.year==1965].country.to_list()
vp_min = -min(year1val+year2val)*0.95
vp_max = max(year1val+year2val)*1.05

# Making the SLOPEGRAPH using plotly
import plotly.graph_objects as go
fig = go.Figure()
for x_val, y_val, cat_val in zip(year1val, year2val, cat1val):
    fig.add_trace(go.Scatter(x=[year1, year2], y=[x_val, y_val], mode='lines+markers+text', text=[cat_val, cat_val], textposition=['middle left', 'middle right'] ))
fig.update_layout(showlegend=False) 
fig.add_shape(type="line", x0=year1, y0=vp_min, x1=year1, y1=vp_max,line=dict(color="Grey",width=2))
fig.add_shape(type="line", x0=year2, y0=vp_min, x1=year2, y1=vp_max,line=dict(color="Grey",width=2))
fig.update_yaxes(range=[vp_min, vp_max] ) #, showticklabels=False)
fig.update_xaxes(range=[year1-vp_offset, year2+vp_offset] ) # showticklabels=False
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.22,xanchor='center',yanchor='top', 
font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
text='Energy Use Per Person'))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.085,xanchor='center',yanchor='top',
font=dict(family='Arial',size=14,color='grey'),showarrow=False,
text='1965 vs 2019'))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.07,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='#30DayChartChallenge - slope - 2021/04/05'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.13,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='https://ourworldindata.org/grapher/per-capita-energy-use'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.21,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
fig.show()
