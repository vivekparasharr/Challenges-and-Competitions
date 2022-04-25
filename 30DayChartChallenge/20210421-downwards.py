
import numpy as np
import pandas as pd

# Prepare data
df = pd.read_csv(r'C:\Users\vivek\Documents\Code\local-items\30daychartchallenge-data\military-expenditure-share-gdp-sipri.csv')

df.Entity.unique()

select_countries = ['United States','World', 'China', 'India','Russia',]
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
text='Military expenditure (pct of GDP), 1960 to 2017'))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.085,xanchor='center',yanchor='top',
font=dict(family='Arial',size=14,color='grey'),showarrow=False,
text='Includes military and civil personnel; operation and maintenance; procurement; military R&D; and military aid'))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.10,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='#30DayChartChallenge - downward - 2021/04/21'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='Data from OWID'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.21,xanchor='center',yanchor='top',
font=dict(family='Arial', size=12, color='grey'),showarrow=False,
text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
fig.show()

