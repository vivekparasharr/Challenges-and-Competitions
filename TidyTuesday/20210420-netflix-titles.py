
from matplotlib.pyplot import xticks
import numpy as np
import pandas as pd
from dataprep.eda import plot

# Prepare data
netflix_titles = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-20/netflix_titles.csv')
df = netflix_titles.copy()

from dataprep.eda import create_report
create_report(df).show_browser()

df.columns
df2 = df[['show_id','date_added','release_year']].copy()
df2['added_year'] = df2.date_added.str.strip().str[-4:]
df2.dropna(inplace=True)
plot(df2, 'added_year', 'release_year')

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8,6))
ax = sns.boxplot(data=df2, 
    x='added_year', y='release_year',
    order=list(df2.added_year.sort_values(ascending=True).unique())
    )
ax.set(title='Netflix: how many old titles added?', 
      xlabel='Year added', ylabel='Year released',
    )
ax.figure.savefig("Data/2021-04-20.png")
