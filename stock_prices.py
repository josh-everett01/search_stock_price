import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Search any ticker and see the stock **closing price** and ***volume*** !


""")

tickerName = st.text_input("Search for a stock ticker")

st.button("Search")
tickerSymbol = tickerName

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-12-30')

st.write("""
## Closing Price
 """)
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
 """)
st.line_chart(tickerDf.Volume)