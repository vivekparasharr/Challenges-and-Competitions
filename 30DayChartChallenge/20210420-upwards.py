
import numpy as np
import pandas as pd

# Prepare data
df = pd.read_csv('Data/public-expenditure-on-healthcare-as-share-of-national-gdp.csv')

df.Entity.unique()

select_countries = ['United States','France', 'Norway','United Kingdom','Japan']
df2 = df[df.Entity.isin(select_countries)].reset_index(drop=True)
df2.columns = ['Entity', 'Code', 'Year', 'Expenditure']

# PLOTTING
import plotly.graph_objects as go
fig = go.Figure()
fig.update_layout(template="plotly_dark")
for c in select_countries:
    fig.add_trace(go.Scatter(
        x=list(df2[df2.Entity==c].Year), 
        y=list(df2[df2.Entity==c].Expenditure), 
        mode='lines',
        name=c,
        showlegend=False,
    ))
    fig.add_annotation(dict(xref='paper',yref='y',x=1.0,y=list(df2[df2.Entity==c].Expenditure)[-1]+0.3,xanchor='left',yanchor='top', 
    font=dict(family='Arial',size=12,color='grey'),showarrow=False, text=c))
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.22,xanchor='center',yanchor='top', 
font=dict(family='Arial',size=22,color='grey'),showarrow=False, 
text='Public healthcare expenditure as share of GDP, 1880 to 1994'))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.085,xanchor='center',yanchor='top',
font=dict(family='Arial',size=14,color='grey'),showarrow=False,
text='Public expenditure on healthcare as share of GDP for selected OECD countries'))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.10,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='#30DayChartChallenge - upward - 2021/04/20'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='Data from OWID'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.21,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
fig.show()

