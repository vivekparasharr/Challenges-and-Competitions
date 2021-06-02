
import numpy as np
import pandas as pd
import plotly.express as px

georgia_pop = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-16/georgia_pop.csv')
census = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-16/census.csv')
furniture = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-16/furniture.csv')
city_rural = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-16/city_rural.csv')
income = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-16/income.csv')
freed_slaves = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-16/freed_slaves.csv')
occupation = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-16/occupation.csv')
conjugal = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-16/conjugal.csv')

# dubois challenge 1
# Population change by race in Georgia.
yr = georgia_pop.Year.values
xC = georgia_pop.Colored.values
xW = georgia_pop.White.values

import plotly.graph_objects as go
fig = go.Figure()
fig.update_layout(width=500, height=700, 
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.55), #showlegend=False,
    title="Population change by race in Georgia",title_x=0.5,)
fig.add_trace(go.Scatter(x=xC, y=yr, mode='lines', name='African American'))
fig.add_trace(go.Scatter(x=xW, y=yr, mode='lines', name='White American'))
annotations=[]
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                        xanchor='center', yanchor='top',
                        text='#TidyTuesday - 2021/02/16 | twitter.com/vivekparasharr | github.com/vivekparasharr',
                        font=dict(family='Arial', size=12, color='grey'),
                        showarrow=False))
fig.update_layout(annotations=annotations)
fig.show()

# dubois challenge 2
# Marriage status
# Prepare data
conjugal = conjugal.replace('Negroes','African Americans')
conjugal.columns = ['Population', 'Age', 'c_Single', 'c_Married', 'c_Divorced_and_Widowed']
conjugal = pd.wide_to_long(conjugal, stubnames='c', i=['Population', 'Age'], j='Conjugal_Status', sep='_', suffix=r'\w+').reset_index()
conjugal.columns = ['Population', 'Age', 'Conjugal_Status', 'Conjugal_Status_Value']

import plotly.graph_objects as go
fig = go.Figure()
fig.update_layout(
    template="simple_white",
    yaxis=dict(title_text="Age"), xaxis=dict(title_text="Race Share Pct"),
    barmode="stack",
    legend=dict(yanchor="top", y=1.25, xanchor="left", x=0.50), #showlegend=False,
    title="Conjugal condition",title_x=0.5,
)
colors = ['firebrick','olive','dodgerblue']#,'blueviolet','dimgrey','tomato','sienna','darkorange','forestgreen','steelblue','royalblue','orchid']
#selected_colors = colors[:y_axis_levels]
labels={'Single':'Single', 'Married':'Married', 'Divorced_and_Widowed':'Divorced and Widowed'}
for r, c in zip(conjugal.Conjugal_Status.unique(), colors):
    plot_df = conjugal[conjugal.Conjugal_Status == r]
    fig.add_trace(
        go.Bar(y=[plot_df.Age, plot_df.Population], x=plot_df.Conjugal_Status_Value, name=labels[r], marker_color=c, orientation='h', ),
    )
fig

# dubois challenge 3
# occupation

import plotly.graph_objects as go

labels = occupation.Category.tolist()
labels = ['Negroes: Agriculture, Fisheries and Mining',
 'Negroes: Manufacturing and Mechanical Industries',
 'Negroes: Domestic and Personal Service',
 'Negroes: Professions',
 'Negroes: Trade and Transportation',
 'Blank: Right',
 'Whites: Agriculture, Fisheries and Mining',
 'Whites: Manufacturing and Mechanical Industries',
 'Whites: Domestic and Personal Service',
 'Whites: Professions',
 'Whites: Trade and Transportation',
 'Blank: Left']

white_space=50 # this can be modified as needed
values = occupation.Percentage.tolist()
values = [62.0, 5.0, 28.0, 0.8, 4.5, white_space, 64.0, 12.5, 5.5, 4.0, 13.0, white_space]

color_list = ['dimgray', 'firebrick', 'olive', 'saddlebrown', 'steelblue', 'white', 'dimgray', 'firebrick', 'olive', 'saddlebrown', 'steelblue', 'white']

fig = go.Figure(data=[go.Pie(labels=None, values=values, 
    direction='clockwise', 
    rotation=(-((white_space/sum(values))*360)), 
    sort=False, showlegend=False, 
    title='Occupation by race')]) # , labels=labels, hole=0.4 to make a donut
fig.update_traces(marker=dict(colors=color_list), textinfo='none') #, line=dict(color='#000000', width=2)))
fig.show()





