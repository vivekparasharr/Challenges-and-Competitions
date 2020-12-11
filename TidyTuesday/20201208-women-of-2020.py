
import numpy as np
import pandas as pd 
from dfply import * 

women = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-12-08/women.csv')
df = women[['name', 'category', 'country', 'role', 'description']]

df >> 

(df >> sift(X.name != 'Unsung hero')
    >> group_by(X.category)
    >> summarize(num_of_people = X.name.count())
).set_index('category').plot(title='# of Women Recognized by Category', y='num_of_people', ylabel='', legend=False, kind='pie')

(df >> sift(X.name != 'Unsung hero')
    >> group_by(X.role)
    >> summarize(num_of_people = X.name.count())
    >> arrange(X.num_of_people, {ascending=False}) # could not find a way to do this in dplython, so moved to dfply
)
