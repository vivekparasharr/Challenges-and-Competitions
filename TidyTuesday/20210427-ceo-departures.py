
from matplotlib.pyplot import xticks
import numpy as np
import pandas as pd

# dataset documenting the reasons for CEO departure in S&P 1500 firms from 2000 through 2018
departures = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-27/departures.csv')

departures.head()
departures.shape

long_df = departures.groupby(['departure_code','fyear']).count()[['dismissal_dataset_id']].reset_index()

import plotly.express as px
fig = px.bar(long_df, x='fyear', y='dismissal_dataset_id', 
    color='departure_code', 
    title='Type of CEO exits by year',
    labels={'fyear':'Fiscal year', 
            'dismissal_dataset_id':'# of CEO exits'})
fig.update(layout_coloraxis_showscale=False)
fig.add_annotation(dict(xref='paper',yref='paper',
    x=0.01,y=0.65,xanchor='left',yanchor='middle', 
    font=dict(family='Arial',size=14,color='peru'),showarrow=False, 
    text='M&A related exit'))
fig.add_annotation(dict(xref='paper',yref='paper',
    x=0.01,y=0.25,xanchor='left',yanchor='middle', 
    font=dict(family='Arial',size=14,color='mediumvioletred'),showarrow=False, 
    text='CEO retired'))
fig.add_annotation(dict(xref='paper',yref='paper',
    x=0.01,y=0.02,xanchor='left',yanchor='middle', 
    font=dict(family='Arial',size=14,color='purple'),showarrow=False, 
    text='Dismissed'))
fig.show()


# dtale eds
# pip install dtale
import dtale
d=dtale.show(departures)
d.open_browser()

# pandas-profiling
# pip install pandas-profiling
import pandas_profiling
pandas_profiling.ProfileReport(departures)

# AutoViz
from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()

sep = ','
dft = AV.AutoViz(filename="",sep=sep, 
            depVar='fyear', dfte=departures, 
            header=0, verbose=2, 
            lowess=False, 
            chart_format='svg', 
            max_rows_analyzed=150000, 
            max_cols_analyzed=30)



from dataprep.eda import create_report
create_report(df).show_browser()

df.columns
df2 = df[['show_id','date_added','release_year']].copy()
df2['added_year'] = df2.date_added.str.strip().str[-4:]
df2.dropna(inplace=True)

from dataprep.eda import plot
plot(df2, 'added_year', 'release_year')

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8,6))
ax = sns.boxplot(data=df2, 
    x='added_year', y='release_year',
    order=list(df2.added_year.sort_values(ascending=True).unique())
    )
ax.set(title='Netflix: how many old titles added?', 
      xlabel='Year added', ylabel='Year released',
    )
ax.figure.savefig("Data/2021-04-20.png")

