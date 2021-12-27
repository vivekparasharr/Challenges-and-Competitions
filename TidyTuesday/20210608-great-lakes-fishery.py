# lib
import pandas as pd
import numpy as np

# udf
def vp_summ(df):
    print('#columns:', df.shape[1]) # number of columns
    print('#rows:', df.shape[0]) # number of rows
    for r in df.columns:
        print(r, ':', # column name
        df[r].unique().shape[0], # number of unique elements in the column
        '| example:', np.sort(df[r].unique())[0], '~', np.sort(df[r].unique())[-1]) # example of the first element in the column

# data
fishing = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-06-08/fishing.csv')
stocked = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-06-08/stocked.csv')

fishing.to_csv(r'\Users\vivekparashar\Downloads\fishing.csv', index = False)

# analysis
vp_summ(fishing)
'''
import dataprep.eda as eda
eda.plot(df,'country')
eda.plot_correlation(df, 'numeric-column') 
eda.plot_missing(df, 'country')
'''
# top species by volume
fishing.head(3)
f_species=fishing.groupby(['species']).sum()[['grand_total']].reset_index()
f_species_sorted_top=f_species.sort_values(by='grand_total',ascending=False).head(5)
f_species_top=list(f_species_sorted_top.species)

fishing[fishing.species.isin(f_species_top)]

fishing.groupby(['year','lake','species','grand_total']).count('region')


# preparing data for plotting
# s2 is a subset of summary dataset
s2 = summary[['season','viewers_premier','viewers_finale']]
s2_pivoted = pd.wide_to_long(s2,
    stubnames='viewers', 
    i=['season'], j='episode',
    sep='_',
    suffix=r'\w+')
s2_pivoted.reset_index(inplace=True)

# vis
import plotly.express as px
fig = px.line(s2_pivoted, x="season", y="viewers", color='episode')
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.175,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
  text="Viewership of Survivour TV Series"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.07,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="Viewership declined over time, however season finale mostly saw higher viewership"))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#TidyTuesday - 2021/06/01'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.20,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='twitter.com/vivekparasharr'))
fig.show()

