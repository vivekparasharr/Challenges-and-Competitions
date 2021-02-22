
import pandas as pd
hs_students = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-02/hs_students.csv')
hbcu_all = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-02-02/hbcu_all.csv')

hs_students.columns = ['Year', 'Total pop',
       'Total pop se',
       'White', 'White se', 'Black',
       'Black se', 'Hispanic', 'Hispanic se',
       'Total Apac',
       'Total Apac se',
       'Asian',
       'Asian se',
       'Pacific',
       'Pacific se',
       'Indian Native',
       'Indian Native se',
       'Mix race', 'Mix race se']

df1 = hs_students[['Year', 'Total pop',
       'White', 'Black',
       'Hispanic',
       'Asian',
       'Pacific',
       'Indian Native',
       'Mix race']]

df1[df1['Year']>=10000].Year = round(df1[df1['Year']>=10000].Year/10)


