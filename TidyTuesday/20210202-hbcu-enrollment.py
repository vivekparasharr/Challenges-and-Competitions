
import pandas as pd
import numpy as np
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

# np.where(condition, value if true, value if false)
df1['Year'] = np.where(df1['Year'] >= 10000, round(df1['Year']/10), df1['Year'])

df1.dropna(axis = 0, how = 'all', inplace = True)

# Rename to make them readable as stubnames
df1.columns=['Year', 'Pop_Total', 'Pop_White', 'Pop_Black', 'Pop_Hispanic', 'Pop_Asian', 'Pop_Pacific',
       'Pop_IndianNative', 'Pop_MixRace']
df1 = pd.wide_to_long(df1, stubnames='Pop', i=['Year'], j='Race', sep='_', suffix=r'\w+')
df1 = df1.reset_index()



df2=df1.copy()

# Window function on a dataframe 
df1.Pop = pd.to_numeric(df1.Pop, errors='coerce').fillna(0).astype(int) # working
df1['rank_race'] = df1[df1.Pop>0].groupby('Race')['Year'].rank(method='first') # window funciton
df1[df1['rank_race']==1]

race_list = df1[df1['rank_race']==1].Race.to_list()
year_list = df1[df1['rank_race']==1].Year.to_list()
pop_list = df1[df1['rank_race']==1].Pop.to_list()

for yr in year_list:
    print(round((yr-1910)/100,1))


import plotly.express as px

# color_list = ['dimgray', 'firebrick', 'olive', 'saddlebrown', 'steelblue', 'seagreen', 'darkviolet', 'crimson']

fig = px.line(df2, x="Year", y="Pop", color='Race') # color='Race'
annotations=[]
for yr,pop,race in zip(year_list,pop_list, race_list):
    annotations.append(dict(xref='paper', x=round((yr-1910)/100,1), y=pop,
                                    xanchor='right', yanchor='middle',
                                    text=race + ' {}%'.format(13.5),
                                    font=dict(family='Arial',
                                                size=12,color='black'),
                                    showarrow=False))
fig.update_layout(annotations=annotations)
fig.update_layout(
    autosize=False,
    width=950,
    height=1100,
    showlegend=False,
    #legend_title="Legend Title",
    title="High school completion among persons age 25 and over",
    xaxis_title="Year",
    yaxis_title="Percent of population (persons age 25 and over)",
    )
#fig.write_image("2021-02-02/fig1.png")
fig.show()


# df1 = df1.replace({ "-": np.nan, "&": np.nan })

'''
# wide to long format
df = pd.DataFrame({
    'famid': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'birth': [1, 2, 3, 1, 2, 3, 1, 2, 3],
    'hta': [2.8, 2.9, 2.2, 2, 1.8, 1.9, 2.2, 2.3, 2.1],
    'htb': [3.4, 3.8, 2.9, 3.2, 2.8, 2.4, 3.3, 3.4, 2.9]
})
pd.wide_to_long(df, stubnames='ht', i=['famid', 'birth'], j='age')
# above examples have integers as suffixes. It is possible to have non-integers as suffixes.
df = pd.DataFrame({
    'famid': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'birth': [1, 2, 3, 1, 2, 3, 1, 2, 3],
    'ht_one': [2.8, 2.9, 2.2, 2, 1.8, 1.9, 2.2, 2.3, 2.1],
    'ht_two': [3.4, 3.8, 2.9, 3.2, 2.8, 2.4, 3.3, 3.4, 2.9]
})
pd.wide_to_long(df, stubnames='ht', i=['famid', 'birth'], j='age', sep='_', suffix=r'\w+')
'''

