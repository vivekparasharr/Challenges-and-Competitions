
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=11,16 # make the chart wider
import altair as alt 

gender = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-01-19/gender.csv')
crops = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-01-19/crops.csv')
households = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-01-19/households.csv')

crops[crops.SubCounty=='KENYA'].plot(kind='barh')

crops[crops.SubCounty!='KENYA'][['SubCounty','Farming']].set_index('SubCounty').sort_values(by='Farming').plot(kind='barh')

c = crops[crops.SubCounty!='KENYA']
c['Tea_pct'] = c.Tea / c.Farming
crop_list = ['Tea','Coffee','Avocado','Citrus','Mango','Coconut','Macadamia', 'Cashew Nut', 'Khat (Miraa)']

pd.merge(left=gender, right=crops,
      left_on='County', right_on='SubCounty',
      how='inner',
      suffixes=('_gender','_crops')
      )

artwork.id.count()
artwork[artwork.artist=='Turner, Joseph Mallord William'].count()
artwork.artist.nunique() #3336 unique artists

# top 10 artists - Turner, Joseph Mallord William has 39,389 works
artwork[artwork.artist!='Turner, Joseph Mallord William'].groupby(['artist']).nunique()[['id']].sort_values(by='id', ascending=False).head(15).plot(kind='barh', title='Top 15 Artists with most artwork!')

# what time are the artists from? most artists from 1900-1980
artists.groupby(['gender','yearOfBirth']).nunique()[['id']].reset_index().pivot(index='yearOfBirth',columns='gender',values='id').plot(title='What time are the artists from?')

# wordclouds
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# wordcloud of artwork titles
# combine the text from all rows of the desired column into one big text variable
df1 = artwork
text = str(df1.title[0])
for i in range(1,len(df1)):
    text = text + ' ' + str(df1.title[i])
# Create stopword list: These words wont be included in the word cloud
stopwords = set(STOPWORDS)
stopwords.update(['an example stopword','Blank','title'])
# Create and generate a word cloud image:
# wordcloud = WordCloud().generate(text)
wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white").generate(text)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('wordcloud of artwork titles', fontsize=24, color='firebrick')
plt.show()

# wordcloud showing where the artists are from
df1 = artists
placeOfBirthText = str(df1.placeOfBirth[0])
for i in range(1,len(df1)):
    placeOfBirthText = placeOfBirthText + ' ' + str(df1.placeOfBirth[i])
# Create stopword list: These words wont be included in the word cloud
stopwords = set(STOPWORDS)
stopwords.update(['an example stopword','nan'])
# Create and generate a word cloud image:
# wordcloud = WordCloud().generate(text)
wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white").generate(placeOfBirthText)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('A wordcloud showing where the artists are from.', fontsize=24, color='firebrick')
plt.show()

# Artists from india
artists[artists.placeOfBirth=='Bharat']

