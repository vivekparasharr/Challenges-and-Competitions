
import pandas as pd
import numpy as np

youtube = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-02/youtube.csv')

# summary of a database in terms of number of unique elements in each column
def vp_summ(df):
    print('#columns:', df.shape[1]) # number of columns
    print('#rows:', df.shape[0]) # number of rows
    for r in df.columns:
        print(r, ':', # column name
        df[r].unique().shape[0], # number of unique elements in the column
        '| example:', df[r][0]) # example of the first element in the column
vp_summ(youtube)

# find most and least viewed ads
youtube.sort_values(by='view_count', ascending=True)[['year', 'brand', 'superbowl_ads_dot_com_url', 'view_count']]

df = youtube.groupby('year').mean()[['view_count', 'like_count', 
        'dislike_count', 'favorite_count', 'comment_count']].reset_index()

import plotly.express as px
fig = px.line(df, x="year", y="view_count", #title='#Views of SuperBowl ads', 
        labels={'year':'Year', 'view_count':'Number of Views'})
fig.update_layout(legend=dict(yanchor="top", y=-0.2,
    xanchor="left", x=0.01))
annotations=[]
annotations.append(dict(xref='paper', yref='paper', x=0.61, y=0.96,
                        xanchor='left', yanchor='top',
                        text='Doritos Sling Baby Ad, among other ads',
                        font=dict(family='Arial', size=12, color='grey'),
                        showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.8, y=0.02,
                        xanchor='left', yanchor='bottom',
                        text='Toyota Good Odds',
                        font=dict(family='Arial', size=12, color='grey'),
                        showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.15,
                        xanchor='center', yanchor='top',
                        text='#TidyTuesday - 2021/03/02 | twitter.com/vivekparasharr | github.com/vivekparasharr',
                        font=dict(family='Arial', size=12, color='grey'),
                        showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=1.17,
                        xanchor='center', yanchor='top',
                        text='Super Bowl Ads',
                        font=dict(family='Arial', size=24, color='grey'),
                        showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=1.07,
                        xanchor='center', yanchor='top',
                        text='Number of Views',
                        font=dict(family='Arial', size=14, color='grey'),
                        showarrow=False))
fig.update_layout(annotations=annotations)
fig.show()

