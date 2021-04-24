
import pandas as pd
df = pd.read_csv('Data/share-deaths-from-natural-disasters.csv')
df.columns = ['Entity', 'Code', 'Year', 'Deaths'] #Deaths - Exposure to forces of nature - Sex: Both - Age: All Ages (Percent)

#select_countries = list(df.groupby('Entity').mean()[['Deaths']].reset_index().sort_values(by='Deaths', ascending=False).head(10).Entity)
select_countries = ['Afghanistan',  'Australia', 
     'Brazil', 'Canada', 'Chile', 'China', 'Egypt', 'England', 
       'Finland', 'France', 'Germany',  'India',
       'Indonesia', 'Italy',
       'Japan', 'Malaysia', 'Mexico', 
       'New Zealand',  'Peru', 'Poland',
       'Portugal',  'Russia',  'Saudi Arabia', 'South Africa',
        'Spain', 'Sri Lanka',
        'United Kingdom', 'United States']

df2 = df[df.Entity.isin(select_countries)].reset_index(drop=True)
df3 = df2.pivot(index='Year', columns='Entity', values='Deaths').reset_index()

import plotly.graph_objects as go
fig = go.Figure(data=go.Heatmap(
        z=np.log(df3.iloc[:, 1:].to_numpy()), 
        x=df3.iloc[:,0].to_numpy(), 
        y=select_countries, 
        colorscale='Viridis'))
fig.update_layout(xaxis_nticks=36)

# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.25,xanchor='center',yanchor='top', 
font=dict(family='Arial',size=22,color='grey'),showarrow=False, 
text='Military expenditure (pct of GDP), 1960 to 2017'))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.12,xanchor='center',yanchor='top',
font=dict(family='Arial',size=14,color='grey'),showarrow=False,
text='Includes military and civil personnel; operation and maintenance; procurement; military R&D; and military aid'))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.14,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='#30DayChartChallenge - downward - 2021/04/21'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.17,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='Data from OWID'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.22,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
fig.show()


