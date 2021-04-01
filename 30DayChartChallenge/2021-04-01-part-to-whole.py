
import pandas as pd
df = pd.read_csv('2021-04-01/netflix_titles.csv')


# EDA
def vp_summ(df):
    print('#columns:', df.shape[1]) # number of columns
    print('#rows:', df.shape[0]) # number of rows
    for r in df.columns:
        print(r, ':', # column name
        df[r].unique().shape[0], # number of unique elements in the column
        '| example:', df[r][0]) # example of the first element in the column
vp_summ(df)

import dataprep.eda as eda
eda.plot(df,'country')
eda.plot_correlation(df, 'numeric-column') 
eda.plot_missing(df, 'country')

# Summarizing
df.groupby('country').nunique()[['show_id']].sort_values(by='show_id', ascending=False)
df.groupby('country').nunique()[['show_id']].sum()
7280-923

# Plotting
import plotly.graph_objects as go

labels = ['All other movies','Indian movies']
values = [6357, 923]

# pull is given as a fraction of the pie radius
fig = go.Figure(data=[go.Pie(labels=labels, values=values, rotation=90, pull=[0, 0.2])])
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.22,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
  text="Share of Indian movies on Netflix"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.07,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="Netflix Movies and TV Shows Dataset"))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#30DayChartChallenge - part-to-whole - 2021/04/01'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.06,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Dataset from Kaggle: https://www.kaggle.com/shivamb/netflix-shows'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='twitter.com/vivekparasharr | github.com/vivekparasharr'))
fig.show()


