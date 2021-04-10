
import pandas as pd
df = pd.read_csv('Data/biodiverse-countries.csv')

import plotly.graph_objects as go
fig = go.Figure(data=go.Choropleth(
    locationmode = "country names",
    locations = list(df.Country.values), #['Brazil', 'India'],
    z = list(df.Rank.values),
    text = list(df.Rank.values),
    autocolorscale=True,
    reversescale=False,
    colorbar_title='Biodiverse Rank',
))
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.22,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
  text="Top 50 Most Biodiverse Countries"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.08,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="Europe Needs to Act!"))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=0.05,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#30DayChartChallenge - animals - 2021/04/08'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=0,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Dataset from https://news.mongabay.com/2016/05/top-10-biodiverse-countries'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.08,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Ten Actions for a Biodiverse Europe'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.13,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='https://www.foeeurope.org/sites/default/files/biodiversity/2016/ten_actions_for_a_biodiverse_europe_-_final.pdf'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.22,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
fig.show()

###################### needs to be changed ##########################
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


