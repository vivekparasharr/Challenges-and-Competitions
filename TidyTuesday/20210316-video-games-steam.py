
import pandas as pd
import numpy as np

games = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-16/games.csv')


######  to be updated

df = raw_bechdel.groupby(['year','rating']).nunique()['id'].reset_index()

map_bechdel = {0:'Unscored movie', 1:'Movie has at least two [named] women in it', 
    2:'Who talk to each other', 3:'About something besides a man'}
df['rating_full'] = df['rating'].map(map_bechdel)


import plotly.express as px
fig = px.area(df[df.year>=1950], x="year", y="id", color='rating_full', 
        labels={'year':'Year', 'id':'Number of Movies', 'rating_full':'Rating'})
fig.update_layout(legend=dict(yanchor="top", y=0.8, xanchor="left", x=0.06))
annotations=[]
# Title
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=1.17,
                        xanchor='center', yanchor='top',
                        text='Bechdel Test',
                        font=dict(family='Arial', size=24, color='grey'),
                        showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=1.07,
                        xanchor='center', yanchor='top',
                        text='Measuring Hollywood’s gender bias!',
                        font=dict(family='Arial', size=14, color='grey'),
                        showarrow=False))
# Note
annotations.append(dict(xref='paper', yref='paper', x=0.88, y=0.95,
                        xanchor='right', yanchor='top',
                        text='Gender bias seems to have reduced over time.',
                        font=dict(family='Arial', size=12, color='grey'),
                        showarrow=False))
# Footer
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.20,
                        xanchor='center', yanchor='top',
                        text='#TidyTuesday - 2021/03/09 | twitter.com/vivekparasharr | github.com/vivekparasharr',
                        font=dict(family='Arial', size=12, color='grey'),
                        showarrow=False))
fig.update_layout(annotations=annotations)
fig.show()


