
import pandas as pd
import numpy as np

# read text file into a list
with open(r'C:\Users\vivek\Documents\Code\local-items\30daychartchallenge-data\HarryPotterandThePhilosophersStone.txt') as f:
    book = f.readlines()

# convert list to dataframe
df = pd.DataFrame(book, columns=['book_lines'])

df = df.book_lines.str.replace('\n', '')
df = pd.DataFrame(df, columns=['book_lines'])

df = df.book_lines.replace('', np.nan)
df = pd.DataFrame(df, columns=['book_lines'])

df = df.dropna()

df = df.reset_index(drop=True)

import dataprep.eda as eda
eda.plot(df,'book_lines')
eda.plot_correlation(df, 'numeric-column') 
eda.plot_missing(df, 'country')

import matplotlib.pyplot as plt

# wordclouds
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# wordcloud of artwork titles
# combine the text from all rows of the desired column into one big text variable
df1 = df
text = str(df1.book_lines[0])
for i in range(1,len(df1)):
    text = text + ' ' + str(df1.book_lines[i])
# Create stopword list: These words wont be included in the word cloud
stopwords = set(STOPWORDS)
stopwords.update(['page'])
#stopwords = set(STOPWORDS)
#stopwords.add("said")
# Create and generate a word cloud image:
hogwarts1_mask = np.array(Image.open("Data/hogwarts1.jpg"))
wc = WordCloud(background_color="white", max_words=2000, mask=hogwarts1_mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue')
# generate word cloud
wc.generate(text)
# show
cm = 1/2.54  # centimeters in inches
plt.figure(figsize=(50*cm, 35*cm))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.savefig('hogwarts1_wordcloud.png')
plt.show()

