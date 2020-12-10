
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

################# dfply ##################
# chaining operations on the data with the >> operator, or alternatively 
# starting with >>= for inplace operations.
df >> head(10) >> tail(3)
df >> select(X.name, X.category)
df >> drop(X.name, X.category)
df >> select(~X.name, ~X.category) # not operator, returns same as above drop statement

# select filters
df >> select(starts_with('c'))
'''
    starts_with(prefix): find columns that start with a string prefix.
    ends_with(suffix): find columns that end with a string suffix.
    contains(substr): find columns that contain a substring in their name.
    everything(): all columns.
    columns_between(start_col, end_col, inclusive=True): find columns between a specified start and end column. The inclusive boolean keyword argument indicates whether the end column should be included or not.
    columns_to(end_col, inclusive=True): get columns up to a specified end column. The inclusive argument indicates whether the ending column should be included or not.
    columns_from(start_col): get the columns starting at a specified column.
'''


############### dplython #################

from dplython import (DplyFrame, X, diamonds, select, sift,
  sample_n, sample_frac, head, arrange, mutate, group_by,
  summarize, DelayFunction)
df = DplyFrame(df)

df >> head(5)
df >> sample_n(5)
df >> select(X.name, X.category, X.country, X.role, X.description)
df >> sift(X.category == 'Leadership') # As in pandas, use bitwise logical operators like |, & (, is same as &)
df >> arrange(X.country) # couldnt find a way to sort descending so moved to dfply library
df >> mutate(carat_bin=X.carat.round())
df >> group_by(X.category) >> summarize(num_of_people = X.name.count())
# It's possible to pass the entire dataframe using X._
# The special Later name, "_" will refer to the entire DataFrame. 

# Combine multiple
(df >> sift(X.name != 'Unsung hero')
    >> group_by(X.category)
    >> summarize(num_of_people = X.name.count())
).set_index('category').plot(title='# of Women Recognized by Category', y='num_of_people', ylabel='', legend=False, kind='pie')
