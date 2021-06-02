
import pandas as pd
import numpy as np
df = pd.read_csv('Data/share-deaths-from-natural-disasters.csv')
df.columns = ['Entity', 'Code', 'Year', 'Deaths'] #Deaths - Exposure to forces of nature - Sex: Both - Age: All Ages (Percent)

#select_countries = list(df.groupby('Entity').mean()[['Deaths']].reset_index().sort_values(by='Deaths', ascending=False).head(10).Entity)
select_countries = ['Australia', 
     'Brazil', 'Canada', 'Chile', 'China', 'Germany',  'India',
       'Japan', 'United Kingdom', 'United States']

df2 = df[df.Entity.isin(select_countries)].reset_index(drop=True)
df3 = df2.pivot(index='Year', columns='Entity', values='Deaths').reset_index()

df3 = df3[df.Year>=2008]


###### Using Plotly Figure Factory Library
import plotly.figure_factory as ff
import plotly.graph_objects as go
fig = ff.create_annotated_heatmap(
        z=np.log(df3.iloc[:, 1:].to_numpy().T), 
        x=list(df3.iloc[:,0].to_numpy()), 
        y=select_countries, 
        annotation_text=np.round(df3.iloc[:, 1:].to_numpy().T,decimals=3), 
        colorscale='YlOrRd',)
# Make text size smaller
for i in range(len(fig.layout.annotations)):
    fig.layout.annotations[i].font.size = 8
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.25,xanchor='center',yanchor='top', 
font=dict(family='Arial',size=20,color='grey'),showarrow=False, 
text='Deaths from natural disasters as a share of total deaths, 2008 to 2017'))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.1,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='#30DayChartChallenge - downward - 2021/04/23'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='Data from OWID'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.20,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
#fig.update_layout(template="plotly_dark")
fig.show()


###### Using Plotly Graph Objects Library
import plotly.graph_objects as go
fig = go.Figure(data=go.Heatmap(
        z=np.log(df3.iloc[:, 1:].to_numpy().T), #np.log(df3.iloc[:, 1:].to_numpy()), 
        x=df3.iloc[:,0].to_numpy(), 
        y=select_countries, 
        colorscale='YlOrRd')) #'Viridis'))
#fig.update_layout(xaxis_nticks=36, yaxis_nticks=36, )
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.25,xanchor='center',yanchor='top', 
font=dict(family='Arial',size=20,color='grey'),showarrow=False, 
text='Deaths from natural disasters as a share of total deaths, 2008 to 2017'))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.12,xanchor='center',yanchor='top',
font=dict(family='Arial',size=16,color='grey'),showarrow=False,
text='Plotted on log scale so the difference is more visible'))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.1,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='#30DayChartChallenge - downward - 2021/04/23'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='Data from OWID'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.20,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
fig.show()

