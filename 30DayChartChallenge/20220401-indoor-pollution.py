
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-04-12/indoor_pollution.csv')
df[df.Entity=='World'][df.Year==2019]

df2 = pd.DataFrame.from_dict([
    {'metric':'Indoor Air Pollution','value':4.10},
    {'metric':'Other Causes','value':95.90}
    ])

fig = px.pie(df2, values='value', names='metric')
fig.update_layout(title_x=0.5, 
    title_text='Deaths attributed to indoor air pollution in 2019')
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(showlegend=False)
fig.add_annotation(y=-0.1, showarrow=False, 
    text="#30DayChartChallenge - part-to-whole - 2022/04/01")
fig.add_annotation(y=-0.15, showarrow=False, 
    text="Data - https://github.com/rfordatascience/tidytuesday/tree/master/data/2022/2022-04-12")
fig.add_annotation(y=-0.25, showarrow=False, 
    text="parashar.ca")
fig.show()


