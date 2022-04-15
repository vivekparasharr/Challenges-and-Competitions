
'''
Source: Wittgenstein Centre for Demography and Global Human Capital (2018). Wittgenstein Centre Data Explorer Version 2.0
Available at: www.wittgensteincentre.org/dataexplorer 

Population Size by Education (000's)
De facto population in a country or region, classified by sex and by five-year age groups. Available by level of educational attainment, in all scenarios, and at all geographical scales. Figures are presented in thousands. <br><br> Data for 1950 to 2015: Based on <a href="http://esa.un.org/wpp/documentation/WPP%202010%20publications.htm">UN Population Division, World Population Prospects 2017</a>
Multiple Scenarios
'''

import numpy as np
import pandas as pd
df = pd.read_csv('Data/wcde_data_education.csv')

df.Scenario.unique() 
Scenario_levels = ['SSP2', 'SSP1', 'SSP3'] # SSP1 - Rapid Development, SSP2 - Medium, SSP3 - Stalled Development

df.Education.unique() 
Education_levels = ['Total', 'Under 15', 'No Education', 'Incomplete Primary',
       'Primary', 'Lower Secondary', 'Upper Secondary', 'Post Secondary']

DEFAULT_PLOTLY_COLORS=['rgb(31, 119, 180)', 'rgb(255, 127, 14)',
                       'rgb(44, 160, 44)', 'rgb(214, 39, 40)',
                       'rgb(148, 103, 189)', 'rgb(140, 86, 75)',
                       'rgb(227, 119, 194)', 'rgb(127, 127, 127)',
                       'rgb(188, 189, 34)', 'rgb(23, 190, 207)']

# Plotting
from plotly.subplots import make_subplots
import plotly.graph_objects as go
fig = make_subplots(rows=3, cols=3, shared_xaxes=True,
     vertical_spacing=0.2, horizontal_spacing=0.1,
    specs=[[{"type": "xy"}, {"type": "xy"}, {"type": "xy"}],
           [{"type": "xy"}, {"type": "xy"}, {"type": "xy"}],
           [{"type": "xy"}, {"type": "xy"}, {"type": "xy"}]])

for e, gx, gy in zip(Education_levels, [1,1,2,2,2,3,3,3], [2,3,1,2,3,1,2,3]):
  x = list(df[df.Scenario=='SSP2'][df.Age=='All'][df.Education==e].Year.values)
  y = list(df[df.Scenario=='SSP2'][df.Age=='All'][df.Education==e].Population.values)
  y_upper = list(df[df.Scenario=='SSP1'][df.Age=='All'][df.Education==e].Population.values)
  y_lower = list(df[df.Scenario=='SSP3'][df.Age=='All'][df.Education==e].Population.values)
  # Plot
  fig.add_trace(
      go.Scatter(x=x, y=y, line=dict(color=DEFAULT_PLOTLY_COLORS[1]), mode='lines', showlegend=False) # rgb(0,100,80)
      ,row=gx, col=gy)
  fig.add_trace(
      go.Scatter(go.Scatter(x=x+x[::-1], y=y_upper+y_lower[::-1], fill='toself', fillcolor='rgba(255, 127, 14, 0.4)', 
          line=dict(color='rgba(255, 127, 14, 0)'), hoverinfo="skip", showlegend=False),)
      ,row=gx, col=gy)

# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.28,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color=DEFAULT_PLOTLY_COLORS[1]),showarrow=False, 
  text="Uncertainty in Global Education Projections"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.16,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="Past reconstructions and future projections of the global population by attained level of education"))

# Annotations
for t, offset, font_size in zip(['Plotted Scenarios', '1. Medium - the middle of the road', '    scenario that can also be seen as', '    the most likely path for each country', '2. Rapid Development', '3. Stalled Development'], [0.00, 0.07, 0.10, 0.13, 0.17, 0.21], [12,10,10,10,10,10]):
  fig.add_annotation(dict(xref='paper',yref='paper',x=-0.05,y=0.97-offset,xanchor='left',yanchor='top',
    font=dict(family='Arial',size=font_size,color='grey'),showarrow=False,
    text=t))

for e, gx, gy in zip(Education_levels, [0.48, 0.84, 0.13, 0.48, 0.84, 0.13, 0.48, 0.84], [1.06, 1.06, 0.66, 0.66, 0.66, 0.26, 0.26, 0.26]):
  fig.add_annotation(dict(xref='paper',yref='paper',x=gx,y=gy,xanchor='center',yanchor='top',
    font=dict(family='Arial', size=12, color='grey'),showarrow=False,
    text=e))

# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.09,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#30DayChartChallenge - 2021/04/27 | uncertainties | educational'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Data: http://dataexplorer.wittgensteincentre.org/wcde-v2'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.21,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))

fig.update_xaxes(color='grey', tickfont=dict(size=10))
fig.update_yaxes(color='grey', tickfont=dict(size=10))
fig.update_layout(template="plotly_dark")
fig.show()

