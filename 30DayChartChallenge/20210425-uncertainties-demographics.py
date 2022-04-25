
import numpy as np
import pandas as pd
df = pd.read_csv(r'C:\Users\vivek\Documents\Code\local-items\30daychartchallenge-data\world_population_and_projection.csv')
df = df[df.Year>=2000]
for c in df.columns.to_list()[1:]:
  df[c] = df[c].str.replace(' ','')
  df[c] = df[c].str.replace(',','')
  df[c] = pd.to_numeric(df[c])

# Plotting
import plotly.graph_objs as go

chosen_color='grey'
x = list(df.Year)
y = list(df.Actual_Median)
y_upper = list(df.Upper_95)
y_lower = list(df.Lower_95)
y_upper2 = list(df.Upper_80)
y_lower2 = list(df.Lower_80)

fig = go.Figure([
    go.Scatter(
        x=x,
        y=y,
        line=dict(color='rgb(0,100,80)'),
        mode='lines'
    ),
    go.Scatter(
        x=[2020],
        y=[list(df[df.Year==2020]['Actual_Median'])[0]],
        marker=dict(size=10, color='rgb(0,100,80)'),
        mode='markers'
    ),
    go.Scatter(
        x=x+x[::-1], # x, then x reversed
        y=y_upper+y_lower[::-1], # upper, then lower reversed
        fill='toself',
        fillcolor='rgba(0,100,80,0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        hoverinfo="skip",
        showlegend=False
    ),
    go.Scatter(
        x=x+x[::-1], # x, then x reversed
        y=y_upper2+y_lower2[::-1], # upper, then lower reversed
        fill='toself',
        fillcolor='rgba(0,100,80,0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        hoverinfo="skip",
        showlegend=False
    )
])
fig.update_xaxes(color=chosen_color)
fig.update_layout(showlegend=False)
# Set the visibility ON
# fig.update_yaxes(title='y', visible=True, showticklabels=False)
# Set the visibility OFF
fig.update_yaxes(title='y', visible=False, showticklabels=False)
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.25,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color=chosen_color),showarrow=False, 
  text="World Population Estimate and Projection"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.13,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color=chosen_color),showarrow=False,
  text="Since the projeciton is uncertain, there is a median value along with 80% and 95% prediction intervals"))
# Annotate
for a in list(df.columns)[1:]:
  fig.add_annotation(dict(xref='x',yref='y',x=2100,y=list(df[df.Year==2100][a])[0],xanchor='left',yanchor='middle',
    font=dict(family='Arial', size=12, color=chosen_color),showarrow=False,
    text=str(np.round(list(df[df.Year==2100][a])[0]/1000000,2))+' Bn'))
fig.add_annotation(dict(xref='x',yref='y',x=2020,y=list(df[df.Year==2020]['Actual_Median'])[0],xanchor='left',yanchor='top',
  font=dict(family='Arial', size=12, color=chosen_color),showarrow=False,
  text=str(np.round(list(df[df.Year==2020]['Actual_Median'])[0]/1000000,2))+' Bn'))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.09,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color=chosen_color),showarrow=False,
  text='#30DayChartChallenge - 2021/04/25 | uncertainties | demographic'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color=chosen_color),showarrow=False,
  text='Data: https://population.un.org/wpp2019/Download/Standard/Population/'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.21,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color=chosen_color),showarrow=False,
  text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
fig.update_layout(template="plotly_dark")
fig.show()

