import streamlit as st
import yfinance as yf

st.write("""
         
# Simple Stock Price Web App
         
Shown are the stock **closing price** and **volume**\n\n
**(2010-05-31 to 2020-05-31)**
         
""")

# Dropdown menu for ticker selection
tickerSymbol = st.selectbox(
    'Select a ticker symbol',
    ('GOOGL', 'AAPL', 'MSFT', 'AMZN', 'TSLA')
)

#Get Data To The Ticker
tickerdata = yf.Ticker(tickerSymbol)

tickerdf = tickerdata.history(period='1d', start='2010-5-31', end='2020-5-31')


st.write("""
## Closing Price
""")
st.line_chart(tickerdf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerdf.Volume)

