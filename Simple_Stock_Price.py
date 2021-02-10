import yfinance as yf
import streamlit as st
import pandas as pd

st.write('''
# Simple Stock Price App

Shown are the stock **closing price** and *volume* if Google!


''') # Header=# and more # more smaller. *abc* = italic, **abc** = bold

# define the ticket symbol
ticketSymbol = 'GOOGL'
# get data in this ticket
tickerData = yf.Ticker(ticketSymbol)
# get the historical prices this ticker
tickerDf = tickerData.history(period='1d', start='2019-5-31', end='2020-5-31')
# Open High    Low Close  Volume  Dividends  Stock Splits

st.write('''
	## Closing Price

	''') ##h2
st.line_chart(tickerDf.Close)

st.write('''
	## Volume Price

	''')

st.line_chart(tickerDf.Volume)

# cmd to path simple_stock_price.py and ...>streamlit run simple_stock_price.py
