
import numpy as np
import pandas as pd

# Prepare data
df = pd.read_csv('https://query.data.world/s/4fwx53aerhppx7t4dqdhtzqswkjjk6')

df2 = df[['date_time','summary']]
df2.dropna(inplace=True)

df2.date_time = pd.to_datetime(df2.date_time)

df2['year']=df2.date_time.dt.year

df3 = df2.groupby('year').count()[['summary']].reset_index()


import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(
    go.Scatter(x=df3.year, y=df3.summary)
)
fig.add_layout_image(
        dict(
            source="Data/unnamed.jpg",
            xref="x",
            yref="y",
            x=1970,
            y=9000,
            sizex=50,
            sizey=9000,
            sizing="stretch",
            opacity=0.5,
            layer="below")
)
fig.update_layout(template="plotly_dark")
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.22,xanchor='center',yanchor='top', 
font=dict(family='Arial',size=22,color='grey'),showarrow=False, 
text='UFO (unidentified flying objects) Sightings'))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.085,xanchor='center',yanchor='top',
font=dict(family='Arial',size=14,color='grey'),showarrow=False,
text='Registered sightings of UFOs have increased "a lot more" in the past two decades!'))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.10,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='#30DayChartChallenge - space - 2021/04/17'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='Dataset by Tim Renner https://data.world/timothyrenner/ufo-sightings'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.21,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
fig.show()

