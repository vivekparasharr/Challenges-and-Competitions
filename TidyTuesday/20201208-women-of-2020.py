
import numpy as np
import pandas as pd 
from dfply import * 

'''
# 11 Ways to Apply a Function to Each Row in Pandas DataFrame
# https://towardsdatascience.com/apply-function-to-pandas-dataframe-rows-76df74165ee4
# Dataframe
temp = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
# Function
def foo(p):
    return p+1
# Method 4. Pandas apply Function to every row
# Method 5. Python List Comprehension
temp['c'] = [ foo(x) for x in temp['a'] ]
# Method 6. Vectorization
'''

women = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-12-08/women.csv')
df = women[['name', 'category', 'country', 'role', 'description']]

'''
(df >> sift(X.name != 'Unsung hero')
    >> group_by(X.category)
    >> summarize(num_of_people = X.name.count())
).set_index('category').plot(title='# of Women Recognized by Category', y='num_of_people', ylabel='', legend=False, kind='pie')
'''
df[df.name != 'Unsung hero'].groupby('category').count()['name']\
    .plot(title='# of Women Recognized by Category', y='num_of_people', ylabel='', legend=False, kind='pie')

(df >> sift(X.name != 'Unsung hero')
    >> group_by(X.role)
    >> summarize(num_of_people = X.name.count())
    >> arrange(X.num_of_people, {ascending=False}) # could not find a way to do this in dplython, so moved to dfply
)

# add continent
# %conda install -c conda-forge pycountry
# import pycountry as pc

# pip install geopy
# %conda install -c conda-forge geopy
# from geopy import geocoders

# pip install countryinfo
from countryinfo import CountryInfo
# Example
# CountryInfo('India').info()['region']

def foo(ctry_nm):
    try:
        return CountryInfo(ctry_nm).info()['region']
    except:
        return 'NA'
df['continent'] = [ foo(x) for x in df['country']]
# summarize by continent
df=df[df.continent != 'NA']
(df >> group_by(X.continent)
    >> summarize(num_of_people = X.name.count())
).set_index('continent').plot(title='# of Women Recognized by Continent', y='num_of_people', ylabel='', legend=False, kind='pie')




# Wordcloud
# conda install -c conda-forge pillow 
# conda install -c conda-forge wordcloud
from os import path
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

text = str(df.description[0])
for i in range(1,len(df)):
    text = text + ' ' + str(df.description[i])

# Create stopword list: These words wont be included in the word cloud
stopwords = set(STOPWORDS)
stopwords.update(['women','S','year','years','name','female'])

# Create and generate a word cloud image:
# wordcloud = WordCloud().generate(text)
wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white").generate(text)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Save the image in the img folder:
wordcloud.to_file("/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/TidyTuesday/Data/2020-12-08/first_review.png")

