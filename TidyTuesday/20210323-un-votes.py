
import pandas as pd
import numpy as np

unvotes = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-23/unvotes.csv')
roll_calls = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-23/roll_calls.csv')
issues = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-23/issues.csv')

unvotes.tail(1)
roll_calls.tail(1)
issues.head(1)

# add issue name to unvotes dataset
m = pd.merge(left=unvotes, right=issues, left_on='rcid', right_on='rcid', how='inner')
# roll up unvotes dataset
m = m.groupby(['issue','country_code','vote']).count()[['rcid']].reset_index()
# add continent
from countryinfo import CountryInfo
def foo(ctry_nm):
    try:
        return CountryInfo(ctry_nm).region()
    except:
        return 'NA'
m['continent'] = [foo(x) for x in m['country_code']]
# roll up to continent level (remove country level)
m = m.groupby(['issue','continent','vote']).sum()[['rcid']].reset_index()
# drop rows where continenet = NA 
indexNames = m[m.continent == 'NA'].index
m.drop(indexNames , inplace=True)

'''
# Get indexes where name column has value john and value column equals to 0.0
indexNames = df[(df['name'] == 'john') & (df['value'] == 0.0)].index
# Delete these row indexes from dataFrame
df.drop(indexNames , inplace=True)
'''

# Plotting
import plotly.express as px
fig = px.bar(m, x='continent', y='rcid', color='vote', facet_col='issue', facet_col_wrap=2,
  labels={'continent':'Continent', 'rcid':'# of Votes', 'vote':'Vote choice', 'issue':'Issues'})
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.2,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
  text="UN Votes - Data from Harvard's Dataverse"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.12,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="Some disparity between the way Europe is voting vs rest of the world"))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.17,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#TidyTuesday - 2021/03/23 | twitter.com/vivekparasharr | github.com/vivekparasharr'))
fig.show()


# Example
tips = px.data.tips()
fig = px.scatter(tips, x="total_bill", y="tip", facet_row="time", facet_col="day", color="smoker")
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]))
fig.for_each_trace(lambda t: t.update(name=t.name.split("=")[1]))
fig.show()



