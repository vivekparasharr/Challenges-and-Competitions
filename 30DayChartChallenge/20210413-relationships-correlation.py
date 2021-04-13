
# https://www.python-graph-gallery.com/111-custom-correlogram
# https://seaborn.pydata.org/generated/seaborn.pairplot.html

import numpy as np
import pandas as pd

# Prepare data
df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
df.info()

df.iso_code.unique()
sel_cols = ['iso_code','continent','total_cases','population',
    'median_age','life_expectancy','human_development_index']
exclude_countries = ['OWID_AFR', 'OWID_ASI', 'OWID_EUN', 'OWID_INT', 'OWID_EUR',
'OWID_KOS', 'OWID_NAM','OWID_CYN', 'OWID_OCE', 'OWID_SAM', 'OWID_WRL']
df2=df[df.date==df.date.max()][sel_cols].copy()
df2 = df2[~df2.iso_code.isin(exclude_countries)]
df2.dropna(inplace=True)
df2.reset_index(drop=True, inplace=True)

# PLOT
import seaborn as sns
import matplotlib.pyplot as plt
g = sns.pairplot(data=df2[['continent', 'human_development_index', 'life_expectancy', 'median_age']], 
    kind="scatter", hue="continent", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5), corner=True)
g.map_lower(sns.kdeplot, levels=4, color=".2")
g.fig.text(0.35, 0.95,'Correlation between human development index,', fontsize=18) #add text
g.fig.text(0.35, 0.9,'   life expectancy, and median age by continent', fontsize=18) #add text
g.fig.text(0.55, 0.85,'Data: https://ourworldindata.org/coronavirus-source-data', fontsize=10) #add text
g.fig.text(0.55, 0.82,'#30DayChartChallenge - circular - 2021/04/13', fontsize=10) #add text
g.fig.text(0.55, 0.79,'twitter.com/vivekparasharr | github.com/vivekparasharr', fontsize=10) #add text
plt.show()






# UNUSED PLOTS


# Basic correlogram
# kind = (possible kinds are ‘scatter’, ‘kde’, ‘hist’, ‘reg’)
sns.pairplot(df2[['human_development_index', 'life_expectancy', 'median_age']], 
    kind="scatter")
plt.show()

# left
sns.pairplot(data=df2[['human_development_index', 'life_expectancy', 'median_age']], 
    kind="scatter", hue="continent", markers=["o", "s", "D"], palette="Set2")
plt.show()

# You can custom it as a density plot or histogram so see the related sections
sns.pairplot(df, diag_kind="kde", diag_kws=dict(shade=True, bw_adjust=.05, vertical=False) )





# PLOT USING ALTAIR

from altair.vegalite.v4.api import Chart
import altair as alt

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
chart = alt.concat(chart, 
    title=alt.TitleParams(
        ['Correlation between x, y, and z'],
        baseline='top', #'bottom',
        orient='top', #'bottom', 
        anchor='middle', #'end',
        font='Courier',
        fontWeight='normal',
        fontSize=18,
        color='gray'
    )
)
alt.concat(chart, 
    title=alt.TitleParams(
        ['', '#30DayChartChallenge - correlation - 2021/04/13', 
        'Dataset: https://ourworldindata.org/coronavirus-source-data', 
        'twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'],
        baseline='bottom',
        orient='bottom',
        anchor='end',
        fontWeight='normal',
        fontSize=12,
        color='gray'
    )
)

