
import scipy.stats as spss
import pandas as pd

# Data - continuous distributions
df_uniform = spss.uniform.rvs(size=10000,loc=10,scale=20)
df_normal = spss.norm.rvs(size=10000,loc=10,scale=100)
df_std_norm = spss.norm.rvs(size=10000,loc=0,scale=1) 
df_gamma = spss.gamma.rvs(a=5,size=10000)
df_exponential = spss.expon.rvs(scale=1,loc=0,size=10000)
df_beta = spss.beta.rvs(5, 2, loc=0, scale=1, size=10000) #, random_state=None)
# discrete distributions
df_binomial = spss.binom.rvs(n=10,p=0.8,size=10000)
df_poisson = spss.poisson.rvs(mu=3,size=10000)
df_bernoulli = spss.bernoulli.rvs(size=10000,p=0.6)


# Plot
from plotly.subplots import make_subplots
import plotly.graph_objects as go
fig = make_subplots(rows=3, cols=3, # shared_xaxes=True,
     vertical_spacing=0.2, horizontal_spacing=0.1,
    specs=[[{"type": "xy"}, {"type": "xy"}, {"type": "xy"}],
           [{"type": "xy"}, {"type": "xy"}, {"type": "xy"}],
           [{"type": "xy"}, {"type": "xy"}, {"type": "xy"}]])
    #subplot_titles=("Plot 1", "Plot 2"))

fig.add_trace(go.Histogram(x=df_uniform, showlegend=False), 
              row=1, col=1,)
fig.add_trace(go.Histogram(x=df_normal, showlegend=False), 
              row=1, col=2,)
fig.add_trace(go.Histogram(x=df_std_norm, showlegend=False), 
              row=1, col=3,)
fig.add_trace(go.Histogram(x=df_gamma, showlegend=False), 
              row=2, col=1,)
fig.add_trace(go.Histogram(x=df_exponential, showlegend=False), 
              row=2, col=2,)
fig.add_trace(go.Histogram(x=df_beta, showlegend=False), 
              row=2, col=3,)
fig.add_trace(go.Histogram(x=df_binomial, showlegend=False), 
              row=3, col=1,)
fig.add_trace(go.Histogram(x=df_poisson, showlegend=False), 
              row=3, col=2,)
fig.add_trace(go.Histogram(x=df_bernoulli, showlegend=False), 
              row=3, col=3,)

# Title
offset_top=0.12
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=offset_top+1.22,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
  text="Statistical Distributions"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=offset_top+1.095,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=16,color='grey'),showarrow=False,
  text="Arrangement of values of a variable showing their frequency of occurrence"))
# Footer
offset_bottom=0.05 
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(offset_bottom+0.02),xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#30DayChartChallenge - statistics - 2021/04/09'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(offset_bottom+0.075),xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Datasets created using scipy.stats'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-(offset_bottom+0.15),xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))

# Annotations
offset_chart_titles = 1.12
fig.add_annotation(dict(xref='paper',yref='paper',x=0.13,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Uniform Distribution'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.48,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Normal Distribution'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.84,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Standard Normal Distribution'))
offset_chart_titles = 0.72
fig.add_annotation(dict(xref='paper',yref='paper',x=0.13,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Gamma Distribution'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.48,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Exponential Distribution'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.84,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Beta Distribution'))
offset_chart_titles = 0.32
fig.add_annotation(dict(xref='paper',yref='paper',x=0.13,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Binomial Distribution'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.48,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Poisson Distribution'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.84,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Bernoulli Normal Distribution'))

# Annotations for formulas
offset_chart_titles = 1.07
fig.add_annotation(dict(xref='paper',yref='paper',x=0.13,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=10, color='grey'),showarrow=False,
  text='uniform.rvs(size=10000,loc=10,scale=20)'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.48,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=10, color='grey'),showarrow=False,
  text='norm.rvs(size=10000,loc=10,scale=100)'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.84,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=10, color='grey'),showarrow=False,
  text='norm.rvs(size=10000,loc=0,scale=1)'))
offset_chart_titles = 0.67
fig.add_annotation(dict(xref='paper',yref='paper',x=0.13,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=10, color='grey'),showarrow=False,
  text='gamma.rvs(a=5,size=10000)'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.48,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=10, color='grey'),showarrow=False,
  text='expon.rvs(scale=1,loc=0,size=10000)'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.84,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=10, color='grey'),showarrow=False,
  text='beta.rvs(5, 2, loc=0, scale=1, size=10000)'))
offset_chart_titles = 0.27
fig.add_annotation(dict(xref='paper',yref='paper',x=0.13,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=10, color='grey'),showarrow=False,
  text='binom.rvs(n=10,p=0.8,size=10000)'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.48,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=10, color='grey'),showarrow=False,
  text='poisson.rvs(mu=3,size=10000)'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.84,y=offset_chart_titles,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=10, color='grey'),showarrow=False,
  text='bernoulli.rvs(size=10000,p=0.6)'))

# Annotations for type of distribution
fig.add_annotation(dict(xref='paper',yref='paper',x=-0.09,y=1.06,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=16, color='grey'),showarrow=False,
  text='Continuous', textangle=270))
fig.add_annotation(dict(xref='paper',yref='paper',x=-0.09,y=0.68,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=16, color='grey'),showarrow=False,
  text='Continuous', textangle=270))
fig.add_annotation(dict(xref='paper',yref='paper',x=-0.09,y=0.25,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=16, color='grey'),showarrow=False,
  text='Discrete', textangle=270))

fig.show()

