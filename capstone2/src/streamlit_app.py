import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title='Market Data')
st.header('Stock market prices & patterns')

#Image
image = Image.open('https://github.com/bhoffman0229/Coding_Temple/blob/main/capstone2/src/stockspic.jpg')

# Streamlit UI
st.image(image, caption="", use_column_width=True)
st.title("Find your data")
### --- Load Dataframe
input_ticker = st.text_input("Ticker (ex: AAPL, TSLA, AMZN, DIS)").upper()
input_timespan = st.radio("By the...",key = 'time',options = ['second', 'minute', 'hour', 'day', 'week', 'month', 'quarter', 'year']).lower()
#input_multiplier = st.text_input("Size of the Timespan(ex: 1,2,3)")
input_fromdate = st.date_input("Start Date (data will go back 5 years)")
input_todate = st.date_input("End Date")

ticker = input_ticker
multiplier = '1'
timespan = input_timespan
fromdate = input_fromdate
todate = input_todate
response = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{fromdate}/{todate}?adjusted=true&limit=50000&apiKey=NF6fM5lz1m9crDksTVh0iXQcjGs5sOXG")
if response.ok==True:
    stockdata = response.json()
    indexlist = []
    df = pd.DataFrame(stockdata)
    newdf = df['results']
    result = pd.DataFrame(newdf)
    #result.rename(columns = {'v':'trading_volume','vw':'volume_weighted_avg_price','o':'open_price','c':'close_price','h':'highest_price','l':'lowest_price','t':'date_time','n':'transaction_amt'}, inplace=True)
    trading_volume_list = [row['v'] for row in result['results']]
    #volume_weighted_list = [row['vw'] for row in result['results']]
    open_price_list = [row['o'] for row in result['results']]
    close_price_list = [row['h'] for row in result['results']]
    highest_price_list = [row['h'] for row in result['results']]
    lowest_price_list = [row['l'] for row in result['results']]
    date_time_list = [row['t'] for row in result['results']]
    transaction_amt_list = [row['t'] for row in result['results']]
    data = pd.DataFrame({'trading_volume':trading_volume_list,
                         #'volume_weighted_avg_price':volume_weighted_list,
                         'open_price':open_price_list,
                         'close_price':close_price_list,
                         'highest_price':highest_price_list,
                         'lowest_price':lowest_price_list,
                         'date_time':date_time_list,
                         'transaction_amt':transaction_amt_list})
    data['date_time'] = data['date_time'].astype(str).astype(int)
    data['ID'] = ticker
    data = data[['ID','date_time','open_price','close_price','trading_volume','highest_price','lowest_price','transaction_amt']]
    datelist = data['date_time']
    datelist = list(datelist)
    datelist = pd.to_datetime(datelist, unit='ms').to_pydatetime()
    data['date_time'] = datelist
    df = data
    st.dataframe(df)
else: st.write('Data is either incomplete or incorrect')

# Streamlit UI

st.title("Interact")

    # Data for chart

answer = st.radio("Is it graphin' time?",key = 'stockvalue',options = ['Open Price', 'Close Price', 'Trading Volume', 'Highest Price', 'Lowest Price', 'Transaction Amount'])
if answer == 'Open Price':
    thetype = 'open_price'
elif answer == 'Close Price':
    thetype = 'close_price'
elif answer == 'Trading Volume':
    thetype = 'trading_volume'
elif answer == 'Highest Price':
    thetype = 'highest_price'
elif answer == 'Lowest Price':
    thetype = 'lowest_price'
elif answer == 'Transaction Amount':
    thetype = 'transaction_amt'    

    # Chart type

answer2 = st.radio("Which type?",key = 'graphtype',options = ['Bar', 'Line', 'Scatter'])
if response.ok==True:
    if answer2 == 'Line':
        fig = px.line(df, x='date_time', y=thetype, title=f"{input_ticker}")
        fig.update_traces(marker=dict(color='purple'))
        st.plotly_chart(fig)
    if answer2 == 'Bar':
        fig = px.bar(df, x='date_time', y=thetype, title=f"{input_ticker}")
        fig.update_traces(marker=dict(color='purple'))
        st.plotly_chart(fig)
    if answer2 == 'Scatter':
        fig = px.scatter(df, x='date_time', y=thetype, title=f"{input_ticker}")
        fig.update_traces(marker=dict(color='purple'))
        st.plotly_chart(fig)
else: pass