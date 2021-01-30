
import numpy as np
import pandas as pd
import plotly.express as px

#gender = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-01-19/gender.csv')
crops = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-01-19/crops.csv')
#households = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-01-19/households.csv')

c1=crops[1:].sort_values(by='Farming', ascending=False).copy() # exclude kenya total row and sort by farming produce descending
c2=c1[['SubCounty','Farming']].set_index('SubCounty').copy()

c3=c1.copy()
# pct is based on crop volume of particular type / total crop volume of a state 
c3['Tea %']=c3.Tea / c3.Farming
c3['Coffee %']=c3.Coffee / c3.Farming
c3['Avocado %']=c3.Avocado / c3.Farming
c3['Citrus %']=c3.Citrus / c3.Farming
c3['Mango %']=c3.Mango / c3.Farming
c3['Coconut %']=c3.Coconut / c3.Farming
c3['Macadamia %']= c3.Macadamia / c3.Farming
c3['Cashew Nut %']=c3['Cashew Nut'] / c3.Farming
c3['Khat (Miraa) %']=c3['Khat (Miraa)'] / c3.Farming

c3 = c3.fillna(0)

c3.drop(['Farming', 'Tea', 'Coffee', 'Avocado', 'Citrus', 'Mango',
       'Coconut', 'Macadamia', 'Cashew Nut', 'Khat (Miraa)'], axis=1, inplace=True)

c3=c3.set_index('SubCounty')

# q signifies quantile
# crops['tea_q']= pd.qcut(crops['tea_pct'], q = 4, labels = False) # throws error as there are a lot of 0 which causes duplicates
# crops['tea_q']= pd.qcut(crops['tea_pct'].rank(method='first'), q = 4, labels = False) # make equal sized (in terms of frequency) quartiles

# PLOTTING
# Draw a heatmap with the numeric values in each cell
fig, ax = plt.subplots(1,2, figsize=(15, 11))
fig.suptitle('Kenya: Crop Data by County', fontsize=32, color='blue')
fig.text(0.05, 0.01, 'https://twitter.com/vivekparasharr', style = 'italic', fontsize = 14, color = "blue") 

b=sns.barplot(data=c2, y='SubCounty', x='Farming', palette="rocket", edgecolor=".6", ax=ax[0])
b.set_ylabel('')
b.set_title('Total farming output by County', fontsize=22, color='blue')
h=sns.heatmap(c3, annot=True, fmt='.0%', linewidths=.5, cmap=sns.cm.rocket_r, cbar=False, yticklabels=False, ax=ax[1])
h.set_xticklabels(h.get_xticklabels(), rotation=30) 
#h.set_yticklabels("") 
h.set_ylabel('')
h.set_title('Prevelant Crops (% of County\'s Farming Output)', fontsize=22, color='blue')
plt.savefig('/Users/vivekparashar/OneDrive/GitHub-OneDrive/Challenges-and-Competitions/TidyTuesday/Data/2021-01-19/20210119-Kenya-Crop-Data.png', dpi=300, facecolor='w')

plt.show()

