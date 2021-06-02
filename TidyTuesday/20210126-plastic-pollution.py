
import numpy as np
import pandas as pd
import plotly.express as px

plastic = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-01-26/plastics.csv')
# plastic.to_csv('/Users/vivekparashar/Downloads/plastc.csv')

# Visualizing categorical variables in dataset using PARALLEL CATEGORIES chart
df = px.data.tips()
fig = px.parallel_categories(df)
fig.show()


# https://www.datacamp.com/community/tutorials/fuzzy-string-python
from fuzzywuzzy import fuzz 


# Partial slopegraph using altair
import altair as alt
from vega_datasets import data
source = data.barley()
alt.Chart(source).mark_line().encode(
    x='year:O',
    y='median(yield)',
    color='site'
)


# Preparing data
p2 = plastic.groupby(['year','parent_company']).sum()[['grand_total']]\
    .sort_values(by='grand_total', ascending=False).reset_index()\
    .pivot_table(index='parent_company', columns='year', values='grand_total')
p2.reset_index(inplace=True)
p2.columns=['parent_company', 'yr2019', 'yr2020']
p2=p2.fillna(0)
p2['total']=p2['yr2019']+p2['yr2020']
p2.sort_values(by='total', ascending=False).head(60)

v = pd.DataFrame({'company': ['The Coca-Cola Company', 'Nestle', 'Unilever', 'PepsiCo', 'Universal Robina Corporation', 'Philip Morris'],
    '2019': [11695.0, 4851.0, 3031.0, 3338.0, 2243.0, 2239.0],
    '2020': [13835.0, 8642.0, 5558.0, 5155.0, 6408.0, 2593.0]})
v.info()
v = v.melt(id_vars='company', value_vars=['2019', '2020'])

# Making the SLOPEGRAPH using plotly
import plotly.graph_objects as go
fig = go.Figure()
for x_val, y_val, company_val in zip([11695.0, 4851.0, 3031.0, 3338.0, 2243.0], [13835.0, 8642.0, 5558.0, 5155.0, 6408.0], ['Coca-Cola', 'Nestle', 'Unilever', 'PepsiCo', 'Universal Robina']):
    fig.add_trace(go.Scatter(x=[2019, 2020], y=[x_val, y_val], mode='lines+markers+text', text=[company_val, company_val], textposition=['middle left', 'middle right'] ))
fig.add_shape(type="line", x0=2019, y0=1500, x1=2019, y1=14500,line=dict(color="Grey",width=2))
fig.add_shape(type="line", x0=2020, y0=1500, x1=2020, y1=14500,line=dict(color="Grey",width=2))
fig.update_yaxes(range=[1500, 14500] ) #, showticklabels=False)
fig.update_xaxes(range=[2018, 2021] ) # showticklabels=False
fig.update_layout(showlegend=False, autosize=False, width=550, height=700,
    #title='Top Plastic Polluters: 2019 vs 2020', 
     title={
        'text': "Top Plastic Polluters: 2019 vs 2020",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.show()


