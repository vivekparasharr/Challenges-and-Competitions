
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

from plotly.subplots import make_subplots
import plotly.graph_objects as go
fig = make_subplots(rows=1, cols=3, shared_yaxes=True,
     vertical_spacing=0.2, horizontal_spacing=0.05,
    specs=[[{"type": "xy"}, {"type": "xy"}, {"type": "xy"}],])
    #subplot_titles=("Plot 1", "Plot 2"))

n=45 # 30 day moving std
m=n-1

fig.add_trace(
  go.Scatter(
        x=list(crypto_usd.index[m:].strftime('%B %d, %Y')),
        y=list(crypto_usd.Open.iloc[m:]), showlegend=False) 
        , row=1, col=1,
)
fig.add_trace(
  go.Scatter(
        x=list(crypto_usd.index[m:].strftime('%B %d, %Y')),
        y=crypto_usd.Open.iloc[m:].to_numpy() + (crypto_usd.Open.rolling(n).std()/2).dropna().to_numpy(), showlegend=False)
        , row=1, col=1,
)
fig.add_trace(
  go.Scatter(
        x=list(crypto_usd.index[m:].strftime('%B %d, %Y')),
        y=crypto_usd.Open.iloc[m:].to_numpy() - (crypto_usd.Open.rolling(n).std()/2).dropna().to_numpy(), showlegend=False)
        , row=1, col=1,
)
# gold-usd
fig.add_trace(
  go.Scatter(
        x=list(gold_usd.index[m:].strftime('%B %d, %Y')),
        y=list(gold_usd.Open.iloc[m:]), showlegend=False)
        , row=1, col=2,
)
fig.add_trace(
  go.Scatter(
        x=list(gold_usd.index[m:].strftime('%B %d, %Y')),
        y=gold_usd.Open.iloc[m:].to_numpy() + (gold_usd.Open.rolling(n).std()/2).dropna().to_numpy(), showlegend=False)
        , row=1, col=2,
)
fig.add_trace(
  go.Scatter(
        x=list(gold_usd.index[m:].strftime('%B %d, %Y')),
        y=gold_usd.Open.iloc[m:].to_numpy() - (gold_usd.Open.rolling(n).std()/2).dropna().to_numpy(), showlegend=False)
        , row=1, col=2,
)
#fig.update_xaxes(matches='x')
fig.update_layout(template="plotly_dark")
fig.show()





import plotly.express as px
import pandas as pd

# data that hopefullt represents your real world dataset
data = pd.DataFrame({'Date': {0: '1993-10-01',
                              1: '1993-10-04',
                              2: '1993-10-05',
                              3: '1993-10-06',
                              4: '1993-10-07'},
                     'yieldspd': {0: 2.36, 1: 2.32, 2: 2.29, 3: 2.31, 4: 2.28}})
data.set_index('Date', inplace = True)

# rename 'yieldspd'
data = data.rename(columns={'yieldspd': 'Yield Spread'})

# produce figure
fig = px.line(data, x = data.index, y ='Yield Spread', line_shape="spline")

# show figure
fig.show()




import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Bar(
    name='Control',
    x=['Trial 1', 'Trial 2', 'Trial 3'], y=[3, 6, 4],
    error_y=dict(type='data', array=[1, 0.5, 1.5])
))
fig.add_trace(go.Bar(
    name='Experimental',
    x=['Trial 1', 'Trial 2', 'Trial 3'], y=[4, 7, 3],
    error_y=dict(type='data', array=[0.5, 1, 2])
))
fig.update_layout(barmode='group')
fig.update_layout(template="plotly_dark")
fig.show()




crypto_usd.Open.mean()
crypto_usd.Open.std()

gold_usd.Open.mean()
gold_usd.Open.std()


from scipy import stats
x.std()
stats.median_abs_deviation(x)



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

