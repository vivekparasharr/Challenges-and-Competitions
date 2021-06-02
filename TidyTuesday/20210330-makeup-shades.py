
import pandas as pd
import numpy as np

sephora = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-30/sephora.csv')
ulta = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-30/ulta.csv')
allCategories = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-30/allCategories.csv')
allShades = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-30/allShades.csv')
allNumbers = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-30/allNumbers.csv')

# summary of a database in terms of number of unique elements in each column
def vp_summ(df):
    print('#columns:', df.shape[1]) # number of columns
    print('#rows:', df.shape[0]) # number of rows
    for r in df.columns:
        print(r, ':', # column name
        df[r].unique().shape[0], # number of unique elements in the column
        '| example:', df[r][0]) # example of the first element in the column
vp_summ(allShades)

p = allShades.groupby(['brand']).nunique()[['product']].reset_index().sort_values(by='product', ascending=False)
h = allShades.groupby(['brand']).nunique()[['hex']].reset_index().sort_values(by='hex', ascending=False)
m = pd.merge(left=p, right=h, left_on='brand', right_on='brand', how='inner')
m = m.loc[:10]
m['hex2']=m.hex * (-1)


# Plotting
from plotly.subplots import make_subplots
import plotly.graph_objects as go
fig = make_subplots(rows=2, cols=1,
    shared_xaxes=True, vertical_spacing=0.02,)
    #subplot_titles=("Plot 1", "Plot 2"))
fig.add_trace(
    go.Bar(x=list(m['brand']), y=list(m['hex2']),
        text=list(m['hex']),textposition='auto'),
    row=1, col=1
)
fig.add_trace(
    go.Bar(x=list(m['brand']), y=list(m['product']),
        text=list(m['product']),textposition='auto'),
    row=2, col=1
)
# Set the visibility ON
# fig.update_yaxes(title='y', visible=True, showticklabels=False)
# Set the visibility OFF
fig.update_yaxes(title='y', visible=False, showticklabels=False)
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.25,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
  text="Makeup Products vs Shades"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.13,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="Plot showing number of products vs number of shades for top 10 brands"))
# Notes
fig.add_annotation(dict(xref='paper',yref='paper',x=-0.005,y=0.75,xanchor='right',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="Shades   ->"))
fig.add_annotation(dict(xref='paper',yref='paper',x=-0.005,y=0.25,xanchor='right',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="Products ->"))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.32,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#TidyTuesday - 2021/03/30 | twitter.com/vivekparasharr | github.com/vivekparasharr'))
fig.show()


