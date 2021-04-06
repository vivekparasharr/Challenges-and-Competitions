
import pandas as pd
import numpy as np

data = pd.read_csv('http://lib.stat.cmu.edu/datasets/CPS_85_Wages', skiprows=27, skipfooter=6, sep=None,
    header=None, names=['education', 'gender', 'wage'],
    usecols=[0, 2, 5],)

# Convert genders to strings (this is particulary useful so that the
# statsmodels formulas detects that gender is a categorical variable)
data['gender'] = np.choose(data.gender, ['male', 'female'])

# Log-transform the wages, because they typically are increased with
# multiplicative factors
data['wage'] = np.log10(data['wage'])

# Plot 2 linear fits for male and female.
import seaborn
seaborn.lmplot(y='wage', x='education', col='gender', data=data)

seaborn.set_style("white")
seaborn.color_palette("pastel")
seaborn.lmplot(y='wage', x='education', hue='gender', data=data, x_jitter=.15)

import scipy.stats as stats
data.boxplot(by =['gender'], column =['wage'], grid = False)

# statistical analysis
# Note that this model is not the plot displayed above: it is one
# joined model for male and female, not separate models for male and
# female. The reason is that a single model enables statistical testing
import statsmodels.formula.api as sm
result = sm.ols(formula='wage ~ education + gender', data=data).fit()
print(result.summary())

# The plots above highlight that there is not only a different offset in wage but also a different slope
# We need to model this using an interaction
result = sm.ols(formula='wage ~ education + gender + education * gender',
                data=data).fit()
print(result.summary())


# Prep data
data.info()
data.education=data.education.astype(object)
data.education.unique()
df=data[data.education>=8]

# Plot
import plotly.express as px
fig = px.box(df, y="wage", x="education", color="gender", notched=True,
          hover_data=df.columns)
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.175,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
  text="Gender Wage Comparison"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.07,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="Do men with same level of education have higher salary than women?"))
# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.15,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#30DayChartChallenge - part-to-whole - 2021/04/06'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.20,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Dataset from http://lib.stat.cmu.edu/datasets/CPS_85_Wages | twitter.com/vivekparasharr'))
fig.show()




