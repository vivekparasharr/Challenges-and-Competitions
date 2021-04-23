
import pandas as pd
df = pd.read_csv('Data/share-deaths-from-natural-disasters.csv')
df.columns = ['Entity', 'Code', 'Year', 'Deaths'] #Deaths - Exposure to forces of nature - Sex: Both - Age: All Ages (Percent)

select_countries = list(df.groupby('Entity').mean()[['Deaths']].reset_index().sort_values(by='Deaths', ascending=False).head(10).Entity)
df2 = df[df.Entity.isin(select_countries)].reset_index(drop=True)
df3 = df2.pivot(index='Year', columns='Entity', values='Deaths').reset_index()

import plotly.graph_objects as go
fig = go.Figure(data=go.Heatmap(
        z=df3.iloc[:, 1:].to_numpy(), #np.log(df3.iloc[:, 1:].to_numpy()), 
        x=df3.iloc[:,0].to_numpy(), 
        y=select_countries, 
        colorscale='Viridis'))

fig.update_layout(
    title='GitHub commits per day',
    xaxis_nticks=36)

fig.show()


