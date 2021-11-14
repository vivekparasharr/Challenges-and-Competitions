
import numpy as np
import pandas as pd
from matplotlib.pyplot import xticks
import dataprep.eda as eda

records = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-25/records.csv')
drivers = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-25/drivers.csv')

'''
- separate 'shortcut' records 
- separate 'type' of record
- 16 tracks
- records start from 1996/97
'''

def vp_summ(df):
    print('#columns:', df.shape[1]) # number of columns
    print('#rows:', df.shape[0]) # number of rows
    for r in df.columns:
        print(r, ':', # column name
        df[r].unique().shape[0], # number of unique elements in the column
        '| example:', np.sort(df[r].unique())[0], '~', np.sort(df[r].unique())[-1]) # example of the first element in the column
vp_summ(records)

df=records
df['year']=pd.DatetimeIndex(pd.to_datetime(df.date)).year
df = df[df.type=='Single Lap'][df.shortcut=='No']
df = df.groupby(['track','year']).min()['time'].reset_index()

# After the first couple of years, there is not much improvement in record times
import altair as alt
alt.Chart(df).mark_line().encode(
    x='year',
    y='time',
    color='track',
    strokeDash='track',
)

# Rainbow Road and Wario Stadium are some of the longest tracks
alt.Chart(df[df.year==1997].sort_values(by='time')).mark_bar().encode(
    x='time:Q',
    y="track:O"
)

