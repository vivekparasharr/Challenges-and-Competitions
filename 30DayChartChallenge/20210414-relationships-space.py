
import numpy as np
import pandas as pd
import plotly.express as px


import plotly.graph_objects as go

launches = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2019/2019-01-15/launches.csv')
df=launches

def set_values(row, value):
    return value[row]
map_dictionary={'SU':'Russia', 'US':'United States', 'RU':'Russia', 'CN':'China', 
'F':'France', 'J':'Japan','IN':'India','I-ESA':'Europe', 
'IL':'Other', 'I':'Other', 'IR':'Other', 'KP':'Other',
'CYM':'Other', 'I-ELDO':'Europe', 'KR':'Other', 'UK':'Europe', 'BR':'Other'}
df['Country'] = df['state_code'].apply(set_values, args =(map_dictionary, )) 

df2 = df.groupby(['launch_year','Country','category']).count()[['tag']].reset_index()
df2.head()
df2.Country.unique()

countries = ['United States', 'France', 'Japan', 'Other',
       'Europe', 'China', 'India', 'Russia']
cou='United States'
categories = ['O', 'F']

cat='F'

((df2[df2.Country==cou][df2.category=='O'].tag)/10).to_list()


df2.groupby(['launch_year','Country']).sum()['tag'].plot(kind='bar')
df2.groupby(['launch_year','Country']).sum()['tag'].sort_values(ascending=False)

cou='United States'
((df2[df2.Country==cou][df2.category=='F'].tag)).to_list()

### PLOTTING
fig = go.Figure()
fig.update_layout(template="plotly_dark")

for cou in countries:
    fig.add_trace(go.Scatter(
        x=df2[df2.Country==cou][df2.category=='O'].launch_year.to_list(),
        y=df2[df2.Country==cou][df2.category=='O'].Country.to_list(),
        marker=dict(color="crimson", size=12), # ((df2[df2.Country==cou][df2.category=='O'].tag)).to_list()
        mode="markers",
        name="Women",
    ))

    fig.add_trace(go.Scatter(
        x=df2[df2.Country==cou][df2.category=='F'].launch_year.to_list(),
        y=df2[df2.Country==cou][df2.category=='F'].Country.to_list(),
        marker=dict(color="gold", size=6), # ((df2[df2.Country==cou][df2.category=='F'].tag)).to_list()
        mode="markers",
        name="Men",
    ))
'''
fig.update_layout(title="Number of Lau",
                  xaxis_title="Annual Salary (in thousands)",
                  yaxis_title="School")'''
fig.update_layout(showlegend=False)
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.22,xanchor='center',yanchor='top', 
font=dict(family='Arial',size=22,color='grey'),showarrow=False, 
text='Number of Space Launches'))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.085,xanchor='center',yanchor='top',
font=dict(family='Arial',size=14,color='grey'),showarrow=False,
text='Red - successful; Yellow - failed launch'))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.10,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='#30DayChartChallenge - space - 2021/04/14'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='Data comes from The Economist GitHub'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.21,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
# Annotation
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.0,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='xx'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='Data comes from The Economist GitHub'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.21,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.10,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='#30DayChartChallenge - space - 2021/04/14'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='Data comes from The Economist GitHub'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.21,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))

fig.show()






planets=pd.read_csv('Data/planets.csv')
df=planets

df.info()

sns.regplot(data=df2, x="launch_year", y="tag")

import plotly.express as px
fig = px.scatter(data=df2, x="launch_year", y="tag")
fig.show()

launches = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2019/2019-01-15/launches.csv')
df=launches
df.head()


sns.scatterplot(data=df2, x="launch_year", y="tag", hue='category'), size="pop", legend=False, sizes=(20, 2000))


df2 = df.groupby(['launch_year','state_code','category']).count()[['tag']].reset_index()
df2.head()

# PLOT
import seaborn as sns
import matplotlib.pyplot as plt
g = sns.pairplot(data=df2, 
    kind="scatter", hue="category", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5), corner=True)
g.map_lower(sns.kdeplot, levels=4, color=".2")
g.fig.text(0.35, 0.95,'Correlation between human development index,', fontsize=18) #add text
g.fig.text(0.35, 0.9,'   life expectancy, and median age by continent', fontsize=18) #add text
g.fig.text(0.55, 0.85,'Data: https://ourworldindata.org/coronavirus-source-data', fontsize=10) #add text
g.fig.text(0.55, 0.82,'#30DayChartChallenge - circular - 2021/04/13', fontsize=10) #add text
g.fig.text(0.55, 0.79,'twitter.com/vivekparasharr | github.com/vivekparasharr', fontsize=10) #add text
plt.show()



fig = px.line(df2, x="launch_year", y="tag", color="category",)
                 size='tag',)
    

fig = px.scatter(df2, x="launch_year", y="tag", color="category",
                 size='tag',)
fig.show()


# visualize categories
import plotly.express as px
fig = px.parallel_categories(df)
fig.show()

import dataprep.eda as eda
eda.plot(df)#,'book_lines')
eda.plot_correlation(df, 'launch_year') 
eda.plot_missing(df, 'country')


# prepare data
energy = energy[energy.Entity.isin(['United Kingdom', 'United States', \
    'Australia', 'Chile', 'India'])]
energy = energy[energy.Year.isin(['1965', '2019'])]
energy.columns = ['country', 'code', 'year', 'value']
energy.value = energy.value.round()

# calculate variables for plot
df = energy
year1=1965
year2=2019
vp_offset = (year2 - year1)/2
year1val = df[df.year==1965].value.to_list()
year2val = df[df.year==2019].value.to_list()
cat1val = df[df.year==1965].country.to_list()
vp_min = -min(year1val+year2val)*0.95
vp_max = max(year1val+year2val)*1.05

# Making the SLOPEGRAPH using plotly
import plotly.graph_objects as go
fig = go.Figure()
for x_val, y_val, cat_val in zip(year1val, year2val, cat1val):
    fig.add_trace(go.Scatter(x=[year1, year2], y=[x_val, y_val], mode='lines+markers+text', text=[cat_val, cat_val], textposition=['middle left', 'middle right'] ))
fig.update_layout(showlegend=False) 
fig.add_shape(type="line", x0=year1, y0=vp_min, x1=year1, y1=vp_max,line=dict(color="Grey",width=2))
fig.add_shape(type="line", x0=year2, y0=vp_min, x1=year2, y1=vp_max,line=dict(color="Grey",width=2))
fig.update_yaxes(range=[vp_min, vp_max] ) #, showticklabels=False)
fig.update_xaxes(range=[year1-vp_offset, year2+vp_offset] ) # showticklabels=False
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.22,xanchor='center',yanchor='top', 
font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
text='Energy Use Per Person'))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.085,xanchor='center',yanchor='top',
font=dict(family='Arial',size=14,color='grey'),showarrow=False,
text='1965 vs 2019'))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.07,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='#30DayChartChallenge - slope - 2021/04/05'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.13,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='https://ourworldindata.org/grapher/per-capita-energy-use'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.21,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
fig.show()
