
import pandas as pd
import numpy as np

employed = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-23/employed.csv')
earn = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-23/earn.csv')

employed2=employed[employed.race_gender=='TOTAL'].groupby(['year','major_occupation']).sum()['employ_n'].reset_index()

import plotly.express as px
fig = px.bar(employed2, x="year", y="employ_n", color="major_occupation",
        barmode = 'stack',
        labels={'year':'Year', 'employ_n':'Employed number', 'major_occupation':'Occupation'})
fig.update_layout(legend=dict(yanchor="top", y=-0.2,
    xanchor="left", x=0.01))
annotations=[]
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.735,
                        xanchor='center', yanchor='top',
                        text='#TidyTuesday - 2021/02/23 | twitter.com/vivekparasharr | github.com/vivekparasharr',
                        font=dict(family='Arial', size=12, color='grey'),
                        showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=1.2,
                        xanchor='center', yanchor='top',
                        text='US: Employed persons by occupation',
                        font=dict(family='Arial', size=24, color='grey'),
                        showarrow=False))
fig.update_layout(annotations=annotations)
fig.show()

employed3=employed[employed.race_gender=='TOTAL'].groupby(['year','major_occupation','minor_occupation']).sum('employ_n').reset_index()
fig = px.bar(employed3, x="year", y="employ_n", color="minor_occupation",
        barmode = 'stack', facet_col='major_occupation', facet_col_wrap=2, 
        labels={'year':'Year', 'employ_n':'Employed number'})
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
))
fig.show()

