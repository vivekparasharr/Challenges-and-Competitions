
# https://www.geeksforgeeks.org/how-to-plot-mean-and-standard-deviation-in-pandas/
# https://pypi.org/project/yfinance/

import numpy as np
import pandas as pd
import yfinance as yf

# Using yfinance
'''
tickerSymbol = 'GOOG'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2021-4-25')
tickerDf.plot(y='Open')
'''
# get a list of crypto ticker symbols from yahoo
crypto_list = list(pd.read_html('https://finance.yahoo.com/cryptocurrencies/')[0].Symbol)

# calling Yahoo finance API and requesting to get data for the last 1 week, with an interval of 90 minutes
# data = yf.download(tickers='BTC-USD', period = '1wk', interval = '90m')
crypto_usd = yf.download(tickers=crypto_list[1], period = 'ytd', interval = '1d') # btc-usd
gold_usd = yf.download(tickers='GC=F', period = 'ytd', interval = '1d') # gold-usd

# df.rolling(2).sum()
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html

DEFAULT_PLOTLY_COLORS=['rgb(31, 119, 180)', 'rgb(255, 127, 14)',
                       'rgb(44, 160, 44)', 'rgb(214, 39, 40)',
                       'rgb(148, 103, 189)', 'rgb(140, 86, 75)',
                       'rgb(227, 119, 194)', 'rgb(127, 127, 127)',
                       'rgb(188, 189, 34)', 'rgb(23, 190, 207)',
                       'rgb(201, 157, 102)', 'rgb(255, 215, 0)']
DEFAULT_PLOTLY_COLORS_A=['rgba(31, 119, 180, 10)', 'rgba(255, 127, 14, 10)',
                       'rgba(44, 160, 44, 10)', 'rgba(214, 39, 40, 10)',
                       'rgba(148, 103, 189, 10)', 'rgba(140, 86, 75, 10)',
                       'rgba(227, 119, 194, 10)', 'rgba(127, 127, 127, 10)',
                       'rgba(188, 189, 34, 10)', 'rgba(23, 190, 207, 10)',
                       'rgba(201, 157, 102, 10)', 'rgba(255, 215, 0, 10)']

from plotly.subplots import make_subplots
import plotly.graph_objects as go
fig = make_subplots(rows=1, cols=3, shared_yaxes=True,
     vertical_spacing=0.2, horizontal_spacing=0.05,
    specs=[[{"type": "xy"}, {"type": "xy"}, {"type": "xy"}, ],])
    #subplot_titles=("Plot 1", "Plot 2"))

n=45 # 45 day moving std
m=n-1
date_format = '%d-%b' # '%B %d, %Y'   # '%d-%m-%Y'
fig.add_trace(
  go.Scatter(
        x=list(crypto_usd.index[m:].strftime(date_format)), 
        y=list(crypto_usd.Open.iloc[m:]), line=dict(color=DEFAULT_PLOTLY_COLORS[-2]), showlegend=False) 
        , row=1, col=1,
)
fig.add_trace(
  go.Scatter(
        x=list(crypto_usd.index[m:].strftime(date_format)),
        y=crypto_usd.Open.iloc[m:].to_numpy() + (crypto_usd.Open.rolling(n).std()/2).dropna().to_numpy(), 
        line=dict(color=DEFAULT_PLOTLY_COLORS[2]), showlegend=False)
        , row=1, col=1,
)
fig.add_trace(
  go.Scatter(
        x=list(crypto_usd.index[m:].strftime(date_format)),
        y=crypto_usd.Open.iloc[m:].to_numpy() - (crypto_usd.Open.rolling(n).std()/2).dropna().to_numpy(), 
        line=dict(color=DEFAULT_PLOTLY_COLORS[2]), showlegend=False)
        , row=1, col=1,
)
# gold-usd
fig.add_trace(
  go.Scatter(
        x=list(gold_usd.index[m:].strftime(date_format)),
        y=list(gold_usd.Open.iloc[m:]), 
        line=dict(color=DEFAULT_PLOTLY_COLORS[-1]), showlegend=False)
        , row=1, col=2,
)
fig.add_trace(
  go.Scatter(
        x=list(gold_usd.index[m:].strftime(date_format)),
        y=gold_usd.Open.iloc[m:].to_numpy() + (gold_usd.Open.rolling(n).std()/2).dropna().to_numpy(), 
        line=dict(color=DEFAULT_PLOTLY_COLORS[2]), showlegend=False)
        , row=1, col=2,
)
fig.add_trace(
  go.Scatter(
        x=list(gold_usd.index[m:].strftime(date_format)),
        y=gold_usd.Open.iloc[m:].to_numpy() - (gold_usd.Open.rolling(n).std()/2).dropna().to_numpy(), 
        line=dict(color=DEFAULT_PLOTLY_COLORS[2]), showlegend=False)
        , row=1, col=2,
)
fig.add_trace(go.Bar(
    name='Control',
    x=['Ethereum', ], y=[crypto_usd.Open.mean()],
    error_y=dict(type='data', array=[crypto_usd.Open.std()], color=DEFAULT_PLOTLY_COLORS[2]) , 
    marker_color=DEFAULT_PLOTLY_COLORS[-2], showlegend=False
), row=1, col=3,)
fig.add_trace(go.Bar(
    name='Experimental',
    x=['Gold',], y=[gold_usd.Open.mean()],
    error_y=dict(type='data', array=[gold_usd.Open.std()], color=DEFAULT_PLOTLY_COLORS[2]) , 
    marker_color=DEFAULT_PLOTLY_COLORS[-1], showlegend=False
), row=1, col=3,)
#fig.update_xaxes(matches='x')

# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.32, xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
  text="Deviation in Price of Ethereum vs Gold"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.21,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="Looking at the 45 day moving standard deviation, Gold price is much more stable compared to Ethereum"))

# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.155,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#30DayChartChallenge - 2021/04/29 | uncertainties | deviations'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.195,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Data: daily since Jan 2021 using yahoo finance api'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.235,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))

fig.update_xaxes(color='grey', tickfont=dict(size=10))
fig.update_yaxes(color='grey', tickfont=dict(size=10))
fig.update_layout(template="plotly_dark")
fig.show()

