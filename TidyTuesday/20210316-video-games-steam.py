
import pandas as pd
import numpy as np

games = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-16/games.csv')

# summary of a database in terms of number of unique elements in each column
def vp_summ(df):
    print('#columns:', df.shape[1]) # number of columns
    print('#rows:', df.shape[0]) # number of rows
    for r in df.columns:
        print(r, ':', # column name
        df[r].unique().shape[0], # number of unique elements in the column
        '| example:', df[r][0]) # example of the first element in the column
vp_summ(games)

# date time converter
def vp_dt_convert(conv_type,df,y,m,d):
    if conv_type=='y-mstr-2dttm': # year and month-str to date time
        return (pd.to_datetime(df[y].astype(str)  + df[m], format='%Y%B'))
games['dttm'] = vp_dt_convert('y-mstr-2dttm', games, 'year', 'month','')

# Lets pick up top 6 games
top_6_games = list(games.groupby('gamename').mean()[['avg','peak']].reset_index().sort_values(by='avg', ascending=False).head(7).gamename[1:7])
top_6_games = sorted(top_6_games) # sort so that the same color is selected for same game in both charts

# select only the rows for those 6 games for the line chart
games[games.gamename.isin(top_6_games)]

# summarize at gamename and year level for selected game for the bar chart
gsumm = ((games[games.gamename.isin(top_6_games)].groupby(['gamename', 'year']).mean()['avg'])/1000).reset_index()
gsumm_pivoted = gsumm.pivot(index='year', columns='gamename', values='avg')

# Plotting
import matplotlib.pyplot as plt
import mplcyberpunk
plt.style.use("cyberpunk")
cm = 1/2.54  # centimeters in inches
#px = 1/plt.rcParams['figure.dpi']  # pixel in inches
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(30*cm, 20*cm)) #, sharex=True)
#fig.subplots_adjust(hspace=0.5)
fig.suptitle('Video Games Data from SteamCharts', fontsize=28, color='white')
fig.text(0.25, 0.05, 'Note: The charts show Average number of players (in Thousands) at the same time', fontsize = 12, color = "white") 
fig.text(0.2, 0.01, '#TidyTuesday - 2021/03/16 | twitter.com/vivekparasharr | github.com/vivekparasharr', style = 'italic', fontsize = 14, color = "white") 
for gname in top_6_games: 
    ax1.plot(list(games[games.gamename==gname].dttm), list(games[games.gamename==gname].avg/1000), label=gname) # marker='o'
    #ax2.plot(list(games[games.gamename==gname].dttm), list(games[games.gamename==gname].peak/1000)) # marker='o'
    #ax2.bar(list(gsumm[gsumm.gamename==gname].year), list(gsumm[gsumm.gamename==gname].avg), label=gname)
gsumm_pivoted.plot(stacked=True, kind='bar', rot=0, legend=False, ax=ax2)
ax1.legend(loc='upper center', ncol=3)
ax2.set_xlabel('Year', size=12)
mplcyberpunk.add_glow_effects(ax1)
mplcyberpunk.add_glow_effects(ax2)
#mplcyberpunk.make_lines_glow(ax1)
#mplcyberpunk.add_underglow(ax2)
plt.show()


