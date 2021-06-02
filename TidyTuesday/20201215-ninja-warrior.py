
import numpy as np
import pandas as pd 
import altair as alt
#from altair_saver import save

df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-12-15/ninja_warrior.csv')

# numbers o unique levels by column
df.nunique()

df.groupby('season').nunique()[['location', 'round_stage', 'obstacle_name']]
df.groupby('round_stage').nunique()[['location', 'obstacle_name']]
df.groupby('location').nunique()[['obstacle_name']].sort_values(by='obstacle_name', ascending=False).plot(kind='bar')
df.groupby('season').nunique()[['obstacle_name']].sort_values(by='season').plot()
df.groupby(['season','round_stage']).nunique()[['obstacle_name']]
df.groupby(['season','round_stage']).nunique()[['location','obstacle_name']]

# unique obstacle_name by round_stage
df2=df.groupby('round_stage').nunique()[['obstacle_order']].reset_index()
df2['round_stage_cat']=np.where(    \
    (df2.round_stage=='National Finals - Stage 1') |    \
    (df2.round_stage=='National Finals - Stage 2') |    \
    (df2.round_stage=='National Finals - Stage 3') |    \
    (df2.round_stage=='National Finals - Stage 4')      \
    , "National Finals", df2.round_stage)
df2.groupby('round_stage_cat').sum()[['obstacle_order']].sort_values(by='obstacle_order', ascending=False).plot.bar()

# Table Bubble Plot (Github Punch Card)
c1=alt.Chart(df).mark_circle().encode(
    y='location:O',
    x='season:O',
    size='sum(obstacle_order):Q'
)
#chart.save('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/TidyTuesday/Data/2020-12-08/chart.png')

c2=alt.Chart(df).mark_circle().encode(
    y='location:O',
    x='round_stage:O',
    size='sum(obstacle_order):Q'
)

alt.hconcat(c1,c2)


# Facet grid
import matplotlib.pyplot as plt 
import seaborn as sns 
df=df[:20] # making the dataset smaller so its faster to render
g=sns.FacetGrid(df, row='round_stage', col='location', hue='obstacle_name')
kws=dict(s=50, linewidth=0.5, edgecolor='black') # passing these values through dictionary is optional
g=g.map(plt.scatter, 'season', 'obstacle_order', **kws)

# optional
# adjust the x and y axis limits
g.set(xlim=(start, end), ylim=(start, end))
# put a diagonal on each chart
for ax in g.axes.flat:
    ax.plot((0,100), (0,100), c="gray", ls="--")
# add ledend
g.add_legend()

# seaborn dashboard
# for seaborn native plots we need to specify the ax=axes[x,y]
# for matplotlib plots such as hist, we can specify axis as axes[x,y].hist(...)
sns.set_style('darkgrid')
f, axes = plt.subplots(2,2,figsize=(15,15))
k1=sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0,0])
k2=sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax=axes[0,1])
z=sns.violinplot(data=movies[movies.Genre == 'Drama'], x='Year', y='CriticRating', ax=axes[1,0])
axes[1,1].hist(movies.CriticRating, bins=15) 
plt.show()

