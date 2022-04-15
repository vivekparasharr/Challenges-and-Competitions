
import numpy as np
import pandas as pd

df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

# prepare data for chile
chl = df[df.iso_code=='CHL'].copy()
chl.date = pd.to_datetime(chl.date)
chl['year'] = chl.date.dt.year
#chl['dayofyear'] = chl.date.dt.dayofyear
#chl['dayofweek'] = chl.date.dt.dayofweek
chl['week'] = chl.date.dt.week
#chl.reset_index(drop=True, inplace=True)
#chl2 = chl.iloc[47:].copy()
#chl3 = chl[chl.dayofweek==5].copy()
#chl3.reset_index(drop=True, inplace=True)
#chl.groupby(['year','week']).mean()[['new_cases']]

chl.new_cases.max() # this is 13990 , i.e. 14000.. 
# we need to divide 14000 by 3500 to get 4.. 
# which is the max_height for our chart..
# so we divide all new_cases by 3500 to get proportional value


import numpy as np
import matplotlib.pyplot as plt

N = 413 #80
bottom = 8
max_height = 8 #4

theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = (chl.new_cases/1750).to_list() #max_height*np.random.rand(N)
width = (2*np.pi) / N

cm = 1/2.54  # centimeters in inches
fig = plt.figure(figsize=(20*cm, 20*cm))
fig.suptitle('Daily Coronavirus Cases in Chile (2020-02-23 to 2021-04-10)', fontsize=22, color='royalblue')
fig.text(0.00, 0.04, '#30DayChartChallenge - circular - 2021/04/11', style = 'italic', fontsize = 14, color = "royalblue") 
fig.text(0.00, 0.01, 'https://twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com', style = 'italic', fontsize = 14, color = "royalblue") 
ax = fig.add_subplot(111, polar=True)
#ax.grid(False)
bars = ax.bar(theta, radii, width=width, bottom=bottom)

# Use custom colors and opacity
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.8)

plt.show()

plt.savefig('Data/chl_covid_cases.png')


#####################################################################
####################### unused code -- attempted to do k-means clustering

df2 = df[df.date==df.date.max()]
not_countries=['OWID_AFR','OWID_ASI','OWID_EUR','OWID_EUN','OWID_INT','OWID_KOS','OWID_NAM','OWID_CYN','OWID_OCE','OWID_SAM','OWID_WRL']
df2 = df2[~df2.iso_code.isin(not_countries)]

sel_col=['location', 'total_cases_per_million', 'total_deaths_per_million', 
'population_density','gdp_per_capita','extreme_poverty',
'cardiovasc_death_rate','diabetes_prevalence','female_smokers',
'male_smokers','handwashing_facilities','hospital_beds_per_thousand',
'life_expectancy','human_development_index']
df3 = df2[sel_col]
df3.dropna(inplace=True)

df3.info()
df3.describe()


import dataprep.eda as eda
eda.plot(df3) #,'country')
eda.plot_correlation(df3) #, 'numeric-column') 
eda.plot_missing(df3) #, 'country')

# Log-transform the wages, because they typically are increased with
# multiplicative factors
# data['wage'] = np.log10(data['wage'])

# K-Means Clustering
# Convert pd df to np ar
X = df3.iloc[:, 1:].values

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# visualize elbow method output
import plotly.express as px
fig = px.line(x=list(range(1, 11)), y=wcss, 
          labels={'x':'Number of clusters', 'y':'Within Cluster Sum of Squares (WCSS)'},
          title='The Elbow Method')
fig.show()

# Training the K-Means model on the dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)
y_kmeans.shape

# Visualising the clusters
import plotly.graph_objects as go
fig = go.Figure()
for i in range(0, n_clusters):
  fig.add_trace(go.Scatter(x=X[y_kmeans == i, 0], y=X[y_kmeans == i, 1],
                    mode='markers', #'lines+markers'
                    name='markers'))
fig.show()


########################## k means #######################

# K-Means Clustering

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Training the K-Means model on the dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)
y_kmeans.shape
# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()


