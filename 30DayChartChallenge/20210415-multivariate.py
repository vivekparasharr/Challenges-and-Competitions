
# https://www.kaggle.com/maniyar2jaimin/interactive-plotly-guide-to-pca-lda-t-sne
# PCA (Principal Component Analysis), 
# LDA ( Linear Discriminant Analysis) and 
# TSNE ( T-Distributed Stochastic Neighbour Embedding)

import numpy as np
import pandas as pd

df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

# latest data
exclude_countries = ['OWID_AFR', 'OWID_ASI', 'OWID_EUN', 'OWID_INT', 'OWID_EUR',
'OWID_KOS', 'OWID_NAM','OWID_CYN', 'OWID_OCE', 'OWID_SAM', 'OWID_WRL']
features=['iso_code', 'continent', 'location', 'population_density', 
      'median_age', 'gdp_per_capita', 'cardiovasc_death_rate', 
      'diabetes_prevalence', 'life_expectancy', 'human_development_index'
      ,'total_cases_per_million']
chosen_features = ['gdp_per_capita', 'cardiovasc_death_rate', 
  'diabetes_prevalence', 'life_expectancy', 'human_development_index']

df2 = df[df.date==df.date.max()][~df.iso_code.isin(exclude_countries)][features].dropna().reset_index(drop=True)


'''
Annotation funciton
'''
def header_and_footer(header, offset_top, offset_bottom):
  # Title
  fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=offset_top,xanchor='center',yanchor='top', 
    font=dict(family='Arial',size=20,color='grey'),showarrow=False, 
    text=header))
  fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=(offset_top-0.07),xanchor='center',yanchor='top', 
    font=dict(family='Arial',size=16,color='grey'),showarrow=False, 
    text="Each point represents a country"))
  # Footer
  fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(offset_bottom),xanchor='center',yanchor='top',
    font=dict(family='Arial', size=12, color='grey'),showarrow=False,
    text='#30DayChartChallenge - multivariate - 2021/04/15 | Data: OWID | twitter.com/vivekparasharr'))
  fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(offset_bottom+0.05),xanchor='center',yanchor='top',
    font=dict(family='Arial', size=11, color='grey'),showarrow=False,
    text='*note: gdp per capita, cardiovasc death rate, diabetes prevalence, life expectancy, human development index'))




# PRINCIPAL COMPONENT ANALYSIS
# Using SKLEARN
# feature scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_scaled=sc.fit_transform(df2[chosen_features])
# pca
from sklearn.decomposition import PCA
pca = PCA(n_components=None)
x_pca = pca.fit_transform(x_scaled)

# variance explained by principal components
pca.explained_variance_ratio_
# Plotting explained variance
exp_var_cumul=pca.explained_variance_ratio_.cumsum()
import plotly.express as px
px.area(
    x=range(1, exp_var_cumul.shape[0] + 1),
    y=exp_var_cumul,
    labels={"x": "# Components", "y": "Explained Variance"}
)


# VISUALIZATION
# Using PLOTLY
# https://plotly.com/python/pca-visualization/
# Correlation plot of original features
import plotly.express as px
fig = px.scatter_matrix(df2, dimensions=chosen_features, color="continent", 
  labels={"gdp_per_capita": "gdp*",  
          "cardiovasc_death_rate": "heart*", 
          "diabetes_prevalence": "diabetes*",
          "life_expectancy": "life*", 
          "human_development_index": "hdi*"})
fig.update_traces(diagonal_visible=False, showupperhalf=False,)
fig.update_layout(template="plotly_dark")
header_and_footer("Scatter Matrix showing correlation between multiple variables", 1.2, 0.15)
fig.show() #renderer="browser")

# Visualize all principal components
import plotly.express as px
labels = {
    str(i): f"PC {i+1} ({var:.1f}%)"
    for i, var in enumerate(pca.explained_variance_ratio_ * 100)
}
fig = px.scatter_matrix(x_pca,labels=labels,dimensions=range(4),
    color=df2["continent"])
fig.update_traces(diagonal_visible=False)
fig.update_layout(template="plotly_dark")
fig.show()#(renderer="browser")

# 2D PCA Scatter Plot
import plotly.express as px
fig = px.scatter(x_pca, x=0, y=1, color=df2['continent'],
  labels={'0': 'PC 1 (59.2%)', '1': 'PC 2 (21.4%)',})
fig.update_layout(template="plotly_dark")
header_and_footer("Principal Component Analysis: 80.6pct of variance explained", 1.2, 0.15)
fig.show()


# Visualize Loadings
# indicate which feature a certain loading original belong to
# loadings = eigenvectors * sqrt(eigenvalues)
import plotly.express as px
fig = px.scatter(x_pca, x=0, y=1, color=df2['continent'])
# additional code for loading
loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
for i, feature in enumerate(chosen_features):
    fig.add_shape(
        type='line',
        x0=0, y0=0,
        x1=loadings[i, 0],
        y1=loadings[i, 1]
    )
    fig.add_annotation(
        x=loadings[i, 0],
        y=loadings[i, 1],
        ax=0, ay=0,
        xanchor="center",
        yanchor="bottom",
        text=feature,
    )
fig.show(renderer='browser')






# LDA - LINEAR DISCRIMINANT ANALYSIS
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(n_components=None)
# Taking in as second argument the Target as labels
x_lda = lda.fit_transform(df2[chosen_features], df2.continent.values)

# variance explained by linear discriminants
lda.explained_variance_ratio_
# Plotting explained variance
exp_var_cumul=lda.explained_variance_ratio_.cumsum()
import plotly.express as px
px.area(
    x=range(1, exp_var_cumul.shape[0] + 1),
    y=exp_var_cumul,
    labels={"x": "# Discriminants", "y": "Explained Variance"}
)

# Visualize all linear discriminants
import plotly.express as px
labels = {
    str(i): f"LD {i+1} ({var:.1f}%)"
    for i, var in enumerate(lda.explained_variance_ratio_ * 100)
}
fig = px.scatter_matrix(x_lda,labels=labels,dimensions=range(4),
    color=df2["continent"])
fig.update_traces(diagonal_visible=False)
fig.update_layout(template="plotly_dark")
fig.show(renderer="browser")

# 2D LDA Scatter Plot
import plotly.express as px
fig = px.scatter(x_lda, x=0, y=1, color=df2['continent'],
  labels={'0': 'LD 1 (74.1%)', '1': 'LD 2 (16.0%)'})
fig.update_layout(template="plotly_dark")
header_and_footer("Linear Discriminant Analysis: 90.1pct of variance explained", 1.2, 0.15)
fig.show()







# TSNE (T-Distributed Stochastic Neighbour Embedding
from sklearn.manifold import TSNE
tsne = TSNE()
# Taking in as second argument the Target as labels
x_tsne = tsne.fit_transform(df2[chosen_features])

# 2D Scatter Plot
import plotly.express as px
fig = px.scatter(x_tsne, x=0, y=1, color=df2['continent'])
fig.update_layout(template="plotly_dark")
header_and_footer("TSNE (T-Distributed Stochastic Neighbour Embedding", 1.2, 0.15)
fig.show()



