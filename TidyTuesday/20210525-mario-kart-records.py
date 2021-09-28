
import numpy as np
import pandas as pd
from matplotlib.pyplot import xticks
import dataprep.eda as eda

records = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-25/records.csv')
drivers = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-25/drivers.csv')

- separate 'shortcut' records 
- separate 'type' of record
- 16 tracks
- records start from 1996/97
 
- 


df=records[records.track == 'Luigi Raceway']
df['year']=pd.DatetimeIndex(pd.to_datetime(df.date)).year
df.groupby(['track','type','shortcut','year']).mean()['time'].head(200)

df[df.type=='Single Lap']

records.system_played.unique()


records.groupby('track').count()[['player']].sort_values(by='player', ascending=False).head(10)

df = records.groupby('track').count()[['player']].sort_values(by='player', ascending=False).head(10)
df.plot(kind='bar')


records.head(5)

drivers.info()

