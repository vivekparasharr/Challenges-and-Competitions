
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

df[df.name != 'Unsung hero'].groupby('category').count()[['name']]\
    .plot(title='# of Women Recognized by Category', y='name', ylabel='', legend=False, kind='pie')

df[df.name != 'Unsung hero'].groupby('category').count()[['role']]\
    .plot(title='# of Women Recognized by Category', y='role', ylabel='', legend=False, kind='bar')

# add continent
# %conda install -c conda-forge pycountry
# import pycountry as pc

# %pip install geopy
# %conda install -c conda-forge geopy
# from geopy import geocoders

# %pip install countryinfo
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
df1 = df[df.name != 'Unsung hero'].groupby(['category','continent']).count()[['name']]\
    .reset_index()

# Sunburst chart
import plotly.express as px
fig=px.sunburst(df1, path=['continent', 'category'], values='name')
fig.show()

# Wordcloud (modified to wordcloud by continent)
# conda install -c conda-forge pillow 
# conda install -c conda-forge wordcloud
from os import path
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

l = ['Asia','Americas','Europe','Africa']
for item in l:
    df1 = df[df.continent==item].reset_index(drop=True)
    text = str(df1.description[0])
    for i in range(1,len(df1)):
        text = text + ' ' + str(df1.description[i])

    # Create stopword list: These words wont be included in the word cloud
    stopwords = set(STOPWORDS)
    stopwords.update(['women','S','year','years','name','female','Africa','UK'])

    # Create and generate a word cloud image:
    # wordcloud = WordCloud().generate(text)
    wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white").generate(text)
    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title('-'+item+'-', fontsize=24, color='firebrick')
    plt.show()

    # Save the image in the img folder:
    filepath = os.path.join('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/TidyTuesday/Data/2020-12-08/', item+'_word_cloud.png')
    wordcloud.to_file(filepath)

