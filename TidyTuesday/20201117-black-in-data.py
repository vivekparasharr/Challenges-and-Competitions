
import pandas as pd
from dplython import (DplyFrame, X, diamonds, select, sift, sample_n,
    sample_frac, head, arrange, mutate, group_by, summarize, DelayFunction) 

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=6.4, 4.8

import numpy as np
import seaborn as sns
sns.set_theme(style="ticks", palette="pastel")
import altair as alt

firsts = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-06-09/firsts.csv')
firsts.to_csv('/Users/vivekparashar/Downloads/firsts.csv')

# Create/Convert a pandas dataframe to dplython df
firsts = DplyFrame(firsts)

firsts.columns
firsts.gender.unique()
firsts.category.unique()

# firsts df summary by category
t1=(firsts >>
    mutate(year_grp=((X.year/10).round())*10) >>
    group_by(X.year_grp, X.category) >>
    summarize(nrows=X.accomplishment.count()))
c1=alt.Chart(t1).mark_circle().encode(
    x='year_grp:O',
    y='category:O',
    size='nrows:Q'
)
c3=alt.Chart(t1).mark_bar().encode(
    x='year_grp',
    y='nrows',
    color='category'
)
# firsts df summary by gender
t2=(firsts >>
    mutate(year_grp=((X.year/10).round())*10) >>
    group_by(X.year_grp, X.gender) >>
    summarize(nrows=X.accomplishment.count()))
c2=alt.Chart(t2).mark_circle().encode(
    x='year_grp:O',
    y='gender:O',
    size='nrows:Q'
)

chart=alt.vconcat(c2, c1, c3)

chart.save('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/TidyTuesday/Data/2020-11-17/chart.png', scale_factor=2.0)
