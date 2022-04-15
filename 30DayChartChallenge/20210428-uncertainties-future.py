
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

# calling Yahoo finance API and requesting to get data for the last 1 week, with an interval of 90 minutes
data = yf.download(tickers='BTC-USD', period = '1wk', interval = '90m')


# PLOTTING
DEFAULT_PLOTLY_COLORS=['rgb(31, 119, 180)', 'rgb(255, 127, 14)',
                       'rgb(44, 160, 44)', 'rgb(214, 39, 40)',
                       'rgb(148, 103, 189)', 'rgb(140, 86, 75)',
                       'rgb(227, 119, 194)', 'rgb(127, 127, 127)',
                       'rgb(188, 189, 34)', 'rgb(23, 190, 207)']

#from plotly.subplots import make_subplots
import plotly.graph_objects as go
fig = go.Figure()

#Candlestick
fig.add_trace(go.Candlestick(x=data.index,
                open=data.Open,
                high=data.High,
                low=data.Low,
                close=data.Close, name = 'market data'))

# Add titles
fig.update_layout(
    #title='Bitcoin live share price evolution',
    yaxis_title='Bitcoin Price (Thousand USD)')

# X-Axes
'''fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=6, label="6h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)'''
# Title
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.48,xanchor='center',yanchor='top', 
  font=dict(family='Arial',size=24,color='grey'),showarrow=False, 
  text="Crypto: Future of Currency!"))
# Subtitle
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=1.31,xanchor='center',yanchor='top',
  font=dict(family='Arial',size=14,color='grey'),showarrow=False,
  text="Atleast my friend Raj would say that!"))

# Footer
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.51,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='#30DayChartChallenge - 2021/04/28 | uncertainties | future'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.59,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='Data: last 1 week, with an interval of 90 minutes using yahoo finance api'))
fig.add_annotation(dict(xref='paper',yref='paper',x=0.5,y=-0.67,xanchor='center',yanchor='top',
  font=dict(family='Arial', size=12, color='grey'),showarrow=False,
  text='twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'))

fig.update_xaxes(color='grey', tickfont=dict(size=10))
fig.update_yaxes(color='grey', tickfont=dict(size=10))
fig.update_layout(template="plotly_dark")
fig.show()

