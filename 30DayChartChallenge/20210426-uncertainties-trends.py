

from altair.vegalite.v4.schema.channels import XError2
import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\vivek\Documents\Code\local-items\30daychartchallenge-data\lung-cancer-deaths-per-100000-by-sex-1950-2002.csv')
df.columns = ['Entity', 'Code', 'Year',
       'Female', # Female lung cancer deaths (per 100,000) (WHO (IARC) (2016))
       'Male']
df['Total']=df.Female+df.Male

df2 = pd.read_csv('Data/daily-smoking-prevalence.csv')
df2.columns = ['Entity', 'Code', 'Year',
       'Daily'] # Daily smoking prevalence - both (IHME, GHDx (2012))



## Plotted using seaborn
import seaborn as sns
ax = sns.regplot(x=df2[df2.Code=='CHL'][df2.Year<=2002].Daily.values, 
      y=df[df.Code=='CHL'][df.Year>=1980].Total.values, )
ax.set(title='Chile: Daily Smoker Prevalence vs Lung Cancer Deaths (1980-2002)', 
      xlabel='daily smokers (% of total populaiton)', ylabel='lung cancer deaths (per 100,000)')
ax.set(xlim=(32.8, 37.8),) # ylim=(0, 10))
ax.annotate(text='Each dot is representative of a year', xy=(33.05, 25.2), xycoords='data')
ax.annotate(text='#30DayChartChallenge - 2021/04/26 | trends', xy=(33.05, 24.8), xycoords='data')
ax.annotate(text='twitter.com/vivekparasharr', xy=(33.05, 24.6), xycoords='data')
ax.figure.savefig("Charts/2021-04-26.png")



### UNUSED CODE

################################################################################

import numpy as np
X=df2[df2.Code=='CHL'][df2.Year<=2002].Daily.values
y=df[df.Code=='CHL'][df.Year>=1980].Total.values

import statsmodels.api as sm
re = sm.OLS(y, X).fit()
print(re.summary())

from statsmodels.sandbox.regression.predstd import wls_prediction_std
prstd, iv_l, iv_u = wls_prediction_std(re)

from statsmodels.stats.outliers_influence import summary_table
st, data, ss2 = summary_table(re, alpha=0.05)

fittedvalues = data[:, 2]
predict_mean_se  = data[:, 3]
predict_mean_ci_low, predict_mean_ci_upp = data[:, 4:6].T
predict_ci_low, predict_ci_upp = data[:, 6:8].T

combined_data = pd.DataFrame(data = [X, fittedvalues, predict_mean_ci_low, predict_mean_ci_upp, predict_ci_low, predict_ci_upp], index=['X', 'fittedvalues', 'predict_mean_ci_low', 'predict_mean_ci_upp', 'predict_ci_low', 'predict_ci_upp']).T

# Check we got the right things
print (np.max(np.abs(re.fittedvalues - fittedvalues)))
print (np.max(np.abs(iv_l - predict_ci_low)))
print (np.max(np.abs(iv_u - predict_ci_upp)))

# Plotting using matplotlib
plt.plot(X, y, 'o')
plt.plot(X, fittedvalues, '-', lw=2)
#plt.plot(X, predict_ci_low, 'r--', lw=2)
#plt.plot(X, predict_ci_upp, 'r--', lw=2)
plt.plot(X, predict_mean_ci_low, 'r--', lw=1)
plt.plot(X, predict_mean_ci_upp, 'r--', lw=1)
plt.show()


# Plotting using plotly
import plotly.graph_objs as go

color_chart='white'
color_title='grey'
color_footer='grey'
color_annotations='white'

fig = go.Figure([
    go.Scatter(
        x=X,
        y=y,
        marker=dict(size=10, color=color_chart),
        mode='markers'
    ),
    go.Scatter(
        x=X,
        y=fittedvalues,
        line=dict(color=color_chart, width=4),
        mode='lines'
    ),
    go.Scatter(
        x=X,
        y=predict_mean_ci_low,
        line=dict(color=color_chart, width=1, dash='dash'),
        mode='lines'
    ),
    go.Scatter(
        x=X,
        y=predict_mean_ci_upp,
        line=dict(color=color_chart, width=1, dash='dash'),
        mode='lines'
    ),
    go.Scatter(
        x=X,
        y=predict_ci_low,
        line=dict(color=color_chart, width=1, dash='dot'),
        mode='lines'
    ),
    go.Scatter(
        x=X,
        y=predict_ci_upp,
        line=dict(color=color_chart, width=1, dash='dot'),
        mode='lines'
    ),
])
fig.update_xaxes(color=color_chart)
fig.update_layout(showlegend=False)
# Set the visibility ON
# fig.update_yaxes(title='y', visible=True, showticklabels=False)
# Set the visibility OFF
fig.update_xaxes(title='daily smokers', visible=True, showticklabels=True)
fig.update_yaxes(title='lung cancer deaths (per 100,000)', visible=True, showticklabels=True)
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.25,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color=color_title),showarrow=False, 
  text="Chile: Daily Smoking Prevalence vs Lung Cancer Deaths"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.13,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color=color_title),showarrow=False,
  text="Plotting a ols reg trendline along with 95% confidence intervals"))
# Annotate
for a,b in zip(list(combined_data.columns)[1:],  ['Fitted values', 'Predict Mean CI', 'Predict Mean CI', 'Predict CI', 'Predict CI']):
  fig.add_annotation(dict(xref='x',yref='y',x=combined_data.X.max()+0.05,y=combined_data[a].max(),xanchor='left',yanchor='middle',
    font=dict(family='Arial', size=12, color=color_annotations),showarrow=False,
    text=b))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.17,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color=color_footer),showarrow=False,
  text='#30DayChartChallenge - 2021/04/26 | uncertainties | trends | Data: ourworldindata.org'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.22,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color=color_footer),showarrow=False,
  text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))
fig.update_layout(template="plotly_dark")
fig.show()


################################################################################


# Plotted using plotly express
import plotly.express as px
fig = px.scatter(x=df2[df2.Code=='CHL'][df2.Year<=2002].Daily.values
, y=df[df.Code=='CHL'][df.Year>=1980].Total.values,  
error_y_minus =df[df.Code=='CHL'][df.Year>=1980].Total.values , 
trendline="ols")
fig.show()

results = px.get_trendline_results(fig)
print(results)
#results.query("sex == 'Male' and smoker == 'Yes'").px_fit_results.iloc[0].summary()
results.px_fit_results.iloc[0].summary()

