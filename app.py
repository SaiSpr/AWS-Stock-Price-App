# Importing libraries
import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime

# App title
st.markdown('''# Stock Market Report''')
st.write('---')

# Sidebar
st.sidebar.subheader('Date & Stock Listings')
start_date = st.sidebar.date_input("Start date", datetime.date(2019, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 3, 1))

# Retrieving tickers data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker
#tickerc = tickerData.earnings()
# Ticker information
logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(logo, unsafe_allow_html=True)

name = tickerData.info['longName']
st.header('**%s**' % name)

sector = tickerData.info['sector']
st.subheader(sector)

country = tickerData.info['country']
st.subheader(country)

website = tickerData.info['website']
st.subheader(website)

summary = tickerData.info['longBusinessSummary']
st.info(summary)

# Ticker data
st.header('**Ticker data**')
st.write(tickerDf)

st.write(tickerData.earnings)

# Bollinger bands
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)

st.markdown(''' 
**Credits**
- Chanin Nantasenamat
''')
