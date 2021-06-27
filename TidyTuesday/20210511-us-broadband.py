
import numpy as np
import pandas as pd
from matplotlib.pyplot import xticks
import dataprep.eda as eda

broadband = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-11/broadband.csv')
broadband.columns=['ST', 'COUNTY_ID', 'COUNTY_NAME', 'AVAILABILITY', 'USAGE']

eda.create_report(broadband).show_browser()

eda.plot(broadband, 'ST', 'BROADBAND AVAILABILITY PER FCC').show_browser()
eda.plot(broadband, 'ST', 'BROADBAND USAGE').show_browser()

eda.plot_correlation(broadband).show_browser()

broadband_zip = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-11/broadband_zip.csv')

broadband.loc[50:55,] # there is a - in data
broadband = broadband.drop(broadband[broadband.AVAILABILITY=='-'].index)
broadband = broadband.drop(broadband[broadband.USAGE=='-'].index)

broadband.info()
broadband.AVAILABILITY=pd.to_numeric(broadband.AVAILABILITY)
broadband.USAGE=pd.to_numeric(broadband.USAGE)

br = broadband.groupby(['ST']).mean()[['AVAILABILITY', 'USAGE']].reset_index()

import plotly.express as px
fig = px.scatter(br, x='AVAILABILITY', 
            y='USAGE', color='ST', opacity=0,
            title='US states by broadband usage vs availability')
fig.update_layout(showlegend=False)
for i,j,s in zip(br.AVAILABILITY.to_list(), br.USAGE.to_list(), br.ST.to_list()):
    fig.add_annotation(dict(xref='x',yref='y',x=i,y=j,
        xanchor='center',yanchor='middle', 
    font=dict(family='Arial',size=11,color='grey'),showarrow=False, 
    text=s))
fig.add_annotation(dict(xref='paper',yref='paper',x=-0.1,y=-0.2,
    xanchor='left',yanchor='middle', 
    font=dict(family='Arial',size=11,color='grey'),showarrow=False, 
    text='percent of people per county with access to fixed terrestrial broadband at speeds of 25 Mbps/3 Mbps as of the end of 2017'))
fig.show()

