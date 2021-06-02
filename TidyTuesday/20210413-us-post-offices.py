
import numpy as np
import pandas as pd

# Prepare data
df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-13/post_offices.csv')

df[df.established.isna()] # 44 NA 
df[df.discontinued.isna()] # 29,089 NA 
df.shape # 166,140

df2 = df[['state','established','discontinued']]
df3 = df2[(df2.established>1800) & (df2.discontinued>1800) & (df2.discontinued<2020)]
e = df3.groupby('established').count()[['state']].reset_index()#.iloc[8:,:]
d = df3.groupby('discontinued').count()[['state']].reset_index()#.iloc[1:216,:]
d['state2']=d.state * (-1)

# Plotting
chosen_color='white'
from plotly.subplots import make_subplots
import plotly.graph_objects as go
fig = make_subplots(rows=2, cols=1,
    shared_xaxes=True, vertical_spacing=0.02,)
    #subplot_titles=("Plot 1", "Plot 2"))
fig.add_trace(
    go.Bar(x=list(e.established), y=list(e.state), name='Established', marker_color=chosen_color),
        #text=list(m['hex']),textposition='auto'),
    row=1, col=1
)
fig.add_trace(
    go.Bar(x=list(d.discontinued), y=list(d.state2), name='Discontinued', marker_color=chosen_color),
        #text=list(m['hex']),textposition='auto'),
    row=2, col=1
)
fig.update_xaxes(color=chosen_color)
fig.update_layout(showlegend=False)
# Set the visibility ON
# fig.update_yaxes(title='y', visible=True, showticklabels=False)
# Set the visibility OFF
fig.update_yaxes(title='y', visible=False, showticklabels=False)
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.25,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color=chosen_color),showarrow=False, 
  text="US Post Offices"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.13,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color=chosen_color),showarrow=False,
  text="Established vs Discontinued since 1800"))
# Notes
fig.add_annotation(dict(xref='paper',yref='paper',x=0.99,y=0.99,xanchor='right',yanchor='top',
  font=dict(family='Arial',size=16,color=chosen_color),showarrow=False,
  text="~166k post offices established"))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.99,y=0.1,xanchor='right',yanchor='top',
  font=dict(family='Arial',size=16,color=chosen_color),showarrow=False,
  text="~137k post offices discontinued"))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.09,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color=chosen_color),showarrow=False,
  text='#30DayChartChallenge - 2021/04/24 | timeseries | monochrome'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color=chosen_color),showarrow=False,
  text='#TidyTuesday - 2021/04/13 | Data: Cameron Blevins and Richard W. Helbock'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.21,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color=chosen_color),showarrow=False,
  text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
fig.update_layout(template="plotly_dark")
fig.show()

