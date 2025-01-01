import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
         
Shown are the stock **closing price** and **volume** of Google!


""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'GOOGL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol);
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2014-12-12', end='2024-12-12')
# Open High     Low Close    Volume Devidens     Stock Splits

st.write("""
# Closing Price
""")
st.line_chart(tickerDf.Close);
("""
# Volume Price
""")
st.line_chart(tickerDf.Volume);

