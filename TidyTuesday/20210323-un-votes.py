
import pandas as pd
import numpy as np

unvotes = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-23/unvotes.csv')
roll_calls = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-23/roll_calls.csv')
issues = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-23/issues.csv')

roll_calls.head(2)

roll_calls.info()
roll_calls['date'] =  pd.to_datetime(roll_calls['date'], format='%Y-%m-%d')

rc = roll_calls.groupby(['date', 'short']).count()[['rcid']].reset_index()

import plotly.express as px
fig = px.area(rc, x="date", y="rcid", color='short', title='Number of issues by Year/Month')
fig.show()

unvotes[unvotes.rcid==4615]

# %pip install countryinfo
from countryinfo import CountryInfo
# Example
# CountryInfo('India').info()['region']

def foo(ctry_nm):
    try:
        return CountryInfo(ctry_nm).region() #info()['region']
    except:
        return 'NA'
##########
def eisenhower_action(is_important: bool, is_urgent: bool) -> int:
  return 2 * is_important + is_urgent

def list_impl(df):
  cutoff_date = datetime.date.today() + datetime.timedelta(days=2)
  return pd.Series([
    eisenhower_action(priority == 'HIGH', due_date <= cutoff_date)
    for (priority, due_date) in zip(df['priority'], df['due_date'])
  ])
%timeit data_sample['action_list'] = list_impl(data_sample)

def itertuples_impl(df):
  cutoff_date = datetime.date.today() + datetime.timedelta(days=2)  
  return pd.Series(
    eisenhower_action(
      row.priority == 'HIGH', row.due_date <= cutoff_date)
    for row in df.itertuples()
  )
%timeit data_sample['action_itertuples'] = itertuples_impl(data_sample)
#########

def itertuples_impl(df):
  return pd.Series(
    foo(df.country_code)
    for row in df.itertuples()
  )
%timeit u['continent'] = itertuples_impl(u)

u.country_code
foo('US')

# unvotes has almost 870k entries
u = unvotes.loc[:50]
%timeit u['continent'] = [ foo(x) for x in u['country_code']]

%timeit unvotes[unvotes.vote=='abstain']

unvotes.info()
roll_calls.info()
issues.info()

unvotes.head()
roll_calls.head(2)
issues.head(2)
issues.groupby('rcid').count()['issue']
# rcid 9095 has multiple issues related to it
issues[issues.rcid==9095]
# 9001 is just about palestenian conflict

roll_calls[roll_calls.rcid==9095]

unvotes[unvotes.rcid==9095].groupby('vote').count()[['rcid']].plot.bar()

roll_calls[roll_calls.short=='AMENDMENTS, RULES OF PROCEDURE']
roll_calls.sort_values(by='date', ascending=False)
pd.merge()



# issues - there are multiple issue per rcid in some cases
issues.groupby('issue').nunique()['rcid']

# so to get distinct rcid x issues
t = issues.pivot(index='rcid', columns='short_name').reset_index()
t['all_issues'] = ''
for c in ['co', 'di', 'ec', 'hr', 'me', 'nu']:
    t['all_issues'] = t['all_issues'].map(str) \
                    + t.issue[c].map(str).replace('nan','') 

t.groupby('all_issues').nunique()[['rcid']].sort_values(by='rcid', ascending=False)

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
        return CountryInfo(ctry_nm).region() #info()['region']
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


