
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

df3 = df2.groupby(['Country','category']).sum()['tag'].reset_index()

countries = ['United States', 'France', 'Japan', 'Other',
       'Europe', 'China', 'India', 'Russia']

df2.groupby(['launch_year','Country']).sum()['tag'].sort_values(ascending=False)
df2.groupby(['launch_year','Country']).sum()['tag'].unique()


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
text='Space Launches'))
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
y_high = 0.14
y_low = 0.09
stepper = 0

for cou in countries:

    print(str(df3[df3.Country==cou][df3.category=='O'].tag.values[0])+' Failures')

    # Successes
    fig.add_annotation(dict(xref='paper',yref='paper',x=0.96,y=(y_high+stepper),xanchor='left',yanchor='top',
    font=dict(family='Arial', size=12, color='grey'),showarrow=False,
    text=str(df3[df3.Country==cou][df3.category=='O'].tag.values[0])+' Successes'))
    # Failures
    fig.add_annotation(dict(xref='paper',yref='paper',x=0.96,y=(y_low+stepper),xanchor='left',yanchor='top',
    font=dict(family='Arial', size=12, color='grey'),showarrow=False,
    text=str(df3[df3.Country==cou][df3.category=='F'].tag.values[0])+' Failures'))
    # Update stepper
    stepper+=0.12

fig.show()


