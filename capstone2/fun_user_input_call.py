import pandas as pd
import requests
 
class Stocksearch():
    def __init__(self, base_url = 'https://api.polygon.io', api_key = 'NF6fM5lz1m9crDksTVh0iXQcjGs5sOXG'):
        self.base_url = base_url
        self.api_key = api_key
        
    def agg(self):
        # Get aggregate bars for a stock over a given date range in custom time window sizes
        # This applies to STOCKS, OPTIONS, INDICES, FOREX, and CRYPTO
        parameters = input('ticker, day/week/month/year, duration(digits), from(YYYY-MM-DD), to(YYYY-MM-DD)')
        parameters = parameters.replace(',','').lower().split()
 
        TICKER     = parameters[0].upper()
        MULTIPLIER = parameters[1]
        TIMESPAN   = parameters[2]
        FROM       = parameters[3]
        TO         = parameters[4]
 
        # completing the link chunk
        AGGREGATES_Q = f'/v2/aggs/ticker/{TICKER}/range/{MULTIPLIER}/{TIMESPAN}/{FROM}/{TO}?adjusted=true&apiKey='
        holding_tank.append(AGGREGATES_Q)
 
    def openclose(self):
        # Get the daily open, high, low, and close (OHLC) for the entire stocks/equities markets
        # This applies to STOCKS, OPTIONS, and INDICES
        parameters = input('ticker, date(YYYY-MM-DD)')
        parameters = parameters.replace(',','').lower().split()
 
        TICKER = parameters[0].upper()
        DATE   = parameters[1]
 
        # completing the link chunk
        DAILY_OPENCLOSE_Q = f'/v1/open-close/{TICKER}/{DATE}?adjusted=true&apiKey='
        holding_tank.append(DAILY_OPENCLOSE_Q)
 
    def crypto_openclose(self):
        # Get the open, high, low, and close (OHLC) for the entire crypto market
        # Must specify from and to dates due to permanently open markets
        # For CRYPTO only
        parameters = input('crypto symbol(from), USD(or another reflection price), date(YYYY-MM-DD)')
        parameters = parameters.replace(',','').lower().split()
 
        CRYPTICK1 = parameters[0].upper()
        CRYPTICK2 = parameters[1].upper()
        DATE      = parameters[2]
 
        # completing the link chunk
        DAILY_CRYPTO_OPENCLOSE_Q = f'/v1/open-close/crypto/{CRYPTICK1}/{CRYPTICK2}/{DATE}?adjusted=true&apiKey='
        holding_tank.append(DAILY_CRYPTO_OPENCLOSE_Q)
 
    def prevclose(self):
        # Get the previous day's open, high, low, and close (OHLC) for the specified ticker
        # For STOCKS, OPTIONS, INDICES, FOREX, and CRYPTO
        parameters = input('ticker')
        parameters = parameters.replace(',','').lower().split()
 
        TICKER = parameters[0].upper()
 
        # completing the link chunk
        PREVIOUS_CLOSE_Q = f'/v2/aggs/ticker/{TICKER}/prev?adjusted=true&apiKey='
        holding_tank.append(PREVIOUS_CLOSE_Q)
 
    def grouped_daily(self):
        # Get the daily open, high, low, and close (OHLC) for the entire specified market
        # For STOCKS, FOREX, and CRYPTO
        parameters = input('stock/forex/crypto, date(YYYY-MM-DD)')
        parameters = parameters.replace(',','').lower().split()
 
        SFC  = parameters[0]
        DATE = parameters[1]
 
        # completing the link chunk
        GROUPED_DAILY_Q = f'/v2/aggs/grouped/locale/us/market/{SFC}/{DATE}?adjusted=true&apiKey='
        holding_tank.append(GROUPED_DAILY_Q)
 
    def indice_calc(self):
        # Get statistics for different types of data calculation
                # SMA = Simple Moving Average
                # EMA = Exponential Moving Average
                # MACD = Moving Average Convergence/Divergence 
                # RSI = Relative Strength Index
        # For INDICES only
        parameters = input('SMA/EMA/MACD/RSI, ticker')
        parameters = parameters.replace(',','').lower().split()
 
        CALC   = parameters[0]
        TICKER = parameters[1].upper()
 
        # completing the link chunk
        INDICES_CALC_Q = f'/v1/indicators/{CALC}/{TICKER}?adjusted=true&sort=asc&limit=50000&apiKey='
        holding_tank.append(INDICES_CALC_Q)
 
 
holding_tank = []
 
# Identifying which search
answer = input('1 = Aggregate Bars, 2 = OpenClose, 3 = CryptoOpenClose, 4 = Prevclose, 5 = GroupedDaily, 6 = IndiceCalcs')
answer = int(answer.strip())
 
# Syncing with its function
if answer == 1:
    Stocksearch().agg()
elif answer == 2:
    Stocksearch().openclose()
elif answer == 3:
    Stocksearch().crypto_openclose()
elif answer == 4:
    Stocksearch().prevclose()
elif answer == 5:
    Stocksearch().grouped_daily()
elif answer == 6:
    Stocksearch().indice_calc()
 
org_tank = [value for value in holding_tank if value != '']
CHUNK = org_tank[0]
 
# receiving from the API
response = requests.get('https://api.polygon.io' + CHUNK + 'NF6fM5lz1m9crDksTVh0iXQcjGs5sOXG')
if response.ok == True:
    market_data = response.json()
    ticker = market_data['ticker']
    df = pd.DataFrame(market_data['results'])
    df.rename(columns={'v':'trading_volume','vw':'volume_weighted_avg_price','o':'open_price','c':'close_price','h':'highest_price','l':'lowest_price','t':'date_time','n':'transaction_amt'}, inplace=True)
    df['date_time'] = pd.to_datetime(df['date_time'], unit='ms')
    df.to_csv(f'{ticker}.csv', index=False)
    print(f'{ticker}.csv file created successfully.')
else:
    checker = str(list(response))
    if "Data not found" in checker:
        print('The Markets were closed that day. Try another')
    elif "ERROR" in checker:
        print('Date is out of the available range. Choose a date within the last 5 years')




stock_search = Stocksearch()