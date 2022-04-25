
import pandas as pd
# df = pd.read_csv('Data/himalayan-peaks.csv')

# Alternative way of getting data
import sqlite3
con = sqlite3.connect(r'C:\Users\vivek\Documents\Code\local-items\30daychartchallenge-data\30daychartchallenge-data.sqlite3')
df = pd.read_sql_query("SELECT * from 'himalayan-peaks'", con)



df.columns = ['PeakID', 'Height', 'PeakName', 'Region', 'Open', 'Status']
df.Height = df.Height.str.replace('m', '')
df.Height = df.Height.astype(int)
df.info()

# 
df[df.Status=='Unclimbed'].sort_values(by='Height')
# Climbed
5550, Chhukung Ri	, Khumbu-Rolwaling-Makalu	
8850, Everest (Sagarmatha, Chomolungma, Qomolungma), Khumbu-Rolwaling-Makalu
# Unclimbed
5407, Roma, Far West-Kanjiroba	
8077, Yalung Kang West	, Kangchenjunga-Janak	

# Plot 1
import plotly.express as px
df1 = px.data.tips()
fig = px.histogram(df, x="Height", color="Region", marginal="box", # or violin, rug
                   hover_data=df.columns, nbins=10)
fig.show()

# Plot 2
import plotly.figure_factory as ff
import numpy as np
x1 = df[df.Status=='Climbed'].Height.values
x2 = df[df.Status=='Unclimbed'].Height.values
# Group data together
hist_data = [x1, x2]
group_labels = ['Climbed', 'Unclimbed']
# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=100)
## 
# Title
ofs1 = 0.0
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=(ofs1+1.22),xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
  text="Himalayan Mountain Range"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=(ofs1+1.09),xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="Most unclimbed mountains are between 6-7km high"))
# Footer
ofs2 = 0.06
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(ofs2+0.02),xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#30DayChartChallenge - physical - 2021/04/07'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(ofs2+0.09),xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Dataset from www.himalayandatabase.com'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(ofs2+0.15),xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='twitter.com/vivekparasharr | github.com/vivekparasharr'))
# Additional annotations
fig.add_annotation(dict(xref='paper',yref='paper',x=0.06,y=0.25,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='orange'),showarrow=False,
  text='5407, Roma'),
  showarrow=True,align='left',arrowhead=1,arrowsize=1,
  arrowwidth=1,arrowcolor='orange')
fig.add_annotation(dict(xref='paper',yref='paper',x=0.745,y=0.25,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='orange'),showarrow=False,
  text='8077, Yalung Kang West'),
  showarrow=True,align='left',arrowhead=1,arrowsize=1,
  arrowwidth=1,arrowcolor='orange')
fig.add_annotation(dict(xref='paper',yref='paper',x=0.095,y=0.05,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='cornflowerblue'),showarrow=False,
  text='5550, Chhukung Ri'),
  showarrow=True,align='left',arrowhead=1,arrowsize=1,
  arrowwidth=1,arrowcolor='cornflowerblue')
fig.add_annotation(dict(xref='paper',yref='paper',x=0.94,y=0.05,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='cornflowerblue'),showarrow=False,
  text='8850, Everest'),
  showarrow=True,align='left',arrowhead=1,arrowsize=1,
  arrowwidth=1,arrowcolor='cornflowerblue')
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
eda.plot(df)
eda.plot_correlation(df) 
eda.plot_missing(df, 'country')

