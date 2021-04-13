
from altair.vegalite.v4.api import Chart
import numpy as np
import pandas as pd
import altair as alt

df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
df.info()

df.iso_code.unique()
sel_cols = ['iso_code','total_cases','population',
    'median_age','life_expectancy','human_development_index']
exclude_countries = ['OWID_AFR', 'OWID_ASI', 'OWID_EUN', 'OWID_INT', 'OWID_EUR',
'OWID_KOS', 'OWID_NAM','OWID_CYN', 'OWID_OCE', 'OWID_SAM', 'OWID_WRL']
df2=df[df.date==df.date.max()][sel_cols].copy()
df2 = df2[~df2.iso_code.isin(exclude_countries)]
df2.dropna(inplace=True)
df2.reset_index(drop=True, inplace=True)


#alt.data_transformers.disable_max_rows()
chart = alt.Chart(df2).mark_circle().encode(
    alt.X(alt.repeat("column"), type='quantitative'),
    alt.Y(alt.repeat("row"), type='quantitative'),
    color='Origin:N'
).properties(
    width=150,
    height=150
).repeat(
    row=['median_age', 'life_expectancy', 'human_development_index'],
    column=['human_development_index', 'life_expectancy', 'median_age']
)

chart.properties(
    #width=550, height=140, 
    title={
      "text": ['Correlation between x, y, and z'], 
      "fontSize": 18,
      "font": 'Courier',
      "anchor": 'middle',
      "color": 'gray'
    }
)
alt.concat(chart, 
    title=alt.TitleParams(
        ['', '#30DayChartChallenge - correlation - 2021/04/14', 
        'Dataset: OWID', 
        'twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'],
        baseline='bottom',
        orient='bottom',
        anchor='end',
        fontWeight='normal',
        fontSize=12,
        color='gray'
    )
)
