
import pandas as pd
import numpy as np

unvotes = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-23/unvotes.csv')
roll_calls = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-23/roll_calls.csv')
issues = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-23/issues.csv')

# votes cast by issue
issues.groupby('issue').nunique()['rcid']

issues.sort_values(by='rcid')
i2 = issues.pivot(index='rcid', columns='short_name').reset_index()

t = i2
t['all_issues'] = ''
for c in ['co', 'di', 'ec', 'hr', 'me', 'nu']:
    t['all_issues'] = t['all_issues'].map(str) \
                    + t.issue[c].map(str).replace('nan','') 

t.groupby('all_issues').nunique()[['rcid']]

# Example of If condition in 1 line
# "neg" if b < 0 else "pos" if b > 0 else "zero"
',' if t.issue['co'].map(str) else ''


pd.merge(left=unvotes, right=issues, left_on='rcid', right_on='rcid')

u2 = unvotes.groupby(['country', 'vote']).count()['rcid'].reset_index()
u3 = u2.pivot(index='country', columns='vote', values='rcid').reset_index()

# %pip install countryinfo
from countryinfo import CountryInfo
# Example
# CountryInfo('India').info()['region']

def foo(ctry_nm):
    try:
        return CountryInfo(ctry_nm).info()['region']
    except:
        return 'NA'
u3['continent'] = [ foo(x) for x in u3['country']]
# summarize by continent
a = u3.groupby(['continent']).sum()[['abstain', 'no', 'yes']].reset_index()
b = u3.groupby(['continent']).count()['country'].reset_index()

u4 = pd.merge(left=a, right=b, left_on='continent', right_on='continent')
u4['total_votes'] = u4.abstain + u4.no + u4.yes



roll_calls.short.unique()





#### to be edited

df = raw_bechdel.groupby(['year','rating']).nunique()['id'].reset_index()

map_bechdel = {0:'Unscored movie', 1:'Movie has at least two [named] women in it', 
    2:'Who talk to each other', 3:'About something besides a man'}
df['rating_full'] = df['rating'].map(map_bechdel)


import plotly.express as px
fig = px.area(df[df.year>=1950], x="year", y="id", color='rating_full', 
        labels={'year':'Year', 'id':'Number of Movies', 'rating_full':'Rating'})
fig.update_layout(legend=dict(yanchor="top", y=0.8, xanchor="left", x=0.06))
annotations=[]
# Title
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=1.17,
                        xanchor='center', yanchor='top',
                        text='Bechdel Test',
                        font=dict(family='Arial', size=24, color='grey'),
                        showarrow=False))
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=1.07,
                        xanchor='center', yanchor='top',
                        text='Measuring Hollywood’s gender bias!',
                        font=dict(family='Arial', size=14, color='grey'),
                        showarrow=False))
# Note
annotations.append(dict(xref='paper', yref='paper', x=0.88, y=0.95,
                        xanchor='right', yanchor='top',
                        text='Gender bias seems to have reduced over time.',
                        font=dict(family='Arial', size=12, color='grey'),
                        showarrow=False))
# Footer
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.20,
                        xanchor='center', yanchor='top',
                        text='#TidyTuesday - 2021/03/09 | twitter.com/vivekparasharr | github.com/vivekparasharr',
                        font=dict(family='Arial', size=12, color='grey'),
                        showarrow=False))
fig.update_layout(annotations=annotations)
fig.show()


