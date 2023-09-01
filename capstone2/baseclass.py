#imports
import pandas as pd
import requests, json
from stock_tickify import KellieTickler
from stock_timizer import TimeConstruct

class Stockshelves():
    """
    All connections to the API take place here
    API services the past 5 year of data
    API service allows for unlimited calls
    Data updated every 15 minutes
    """
 
    # initializing the class
    def __init__(self):
        # list to hold the final link search
        self.CHUNK_tank = []
 
        # the request link lego pieces
        self.BASE_URL = 'https://api.polygon.io'
        self.API_KEY = 'NF6fM5lz1m9crDksTVh0iXQcjGs5sOXG'
        self.ENDCAP = '?adjusted=true&limit=50000&apiKey='
 
class IndieMath():
    #   <---- CALC LIST ---->
    # SMA = Simple Moving Average
    # EMA = Exponential Moving Average
    # MACD = Moving Average Convergence/Divergence
    # RSI = Relative Strength Index
 
    def __init__(self, calculation):
        self.calculation = calculation
 
    def getCALC(self):
        CALCstamp = str(self.calculation).lower()
        return CALCstamp
 
class SergeantFirstClass():
    # Stocks = NYSE, AMEX, NASDAQ as a whole
    # FX     = Foreign exchange market
    # Crypto = Cryptocurrency market as a whole
 
    def __init__(self, market):
        self.market = market
 
    def getSFC(self):
        SFCstamp = str(self.market).lower()
        return SFCstamp
 
class CrypWalk():
    # Ticker 1 is the currency being observed
    # Ticker 2 is the display currency being exchanged into
    # USD is recommended for Ticker 2 for an easy understand of price points
 
    def __init__(self, ticker1, ticker2):
        self.ticker1 = ticker1
        self.ticker2 = ticker2
 
    def getTICKS(self):
        CRYstamp1 = str(self.ticker1)
        CRYstamp2 = str(self.ticker2)
        return CRYstamp1, CRYstamp2
 
class Shelves(Stockshelves):
    def __init__(self, CALC=None, TICKER=None, MULTIPLIER=None, TIMESPAN=None, FROM=None, TO=None, SFC=None, CRYPTIK1=None, CRYPTIK2=None, DATE=None):
        super().__init__()
        # initializations
        self.CALC = CALC
        self.TICKER = TICKER
        self.MULTIPLIER = MULTIPLIER
        self.TIMESPAN = TIMESPAN
        self.FROM = FROM
        self.TO = TO
        self.SFC = SFC
        self.CRYPTIK1 = CRYPTIK1
        self.CRYPTIK2 = CRYPTIK2
        self.DATE = DATE

 
        # Get aggregate bars for a stock over a given date range in custom time window sizes
    def agg(self, ticker, clock):
        # This applies to STOCKS, INDICES, FOREX, and CRYPTO
        AGGREGATES_Q = f'/v2/aggs/ticker/{ticker}/range/{clock}/{self.FROM}/{self.TO}{self.ENDCAP}'
        self.CHUNK_tank.append(AGGREGATES_Q)
 
        # Get the daily open, high, low, and close (OHLC) for the entire stocks/equities markets
    def openclose(self, ticker, clock):
        # This applies to STOCKS and INDICES
        DAILY_OPENCLOSE_Q = f'/v1/open-close/{ticker}/{self.DATE}{self.ENDCAP}'
        self.CHUNK_tank.append(DAILY_OPENCLOSE_Q)
 
        # Get the open, high, low, and close (OHLC) for the entire crypto market
    def cryptoopenclose(self, ticker1, ticker2, clock):
        # For CRYPTO only
        # Must specify from and to dates due to permanently open markets
        DAILY_CRYPTO_OPENCLOSE_Q = f'/v1/open-close/crypto/{ticker1}/{ticker2}/{self.DATE}{self.ENDCAP}'
        self.CHUNK_tank.append(DAILY_CRYPTO_OPENCLOSE_Q)
 
        # Get the previous day's open, high, low, and close (OHLC) for the specified ticker
    def prevclose(self, ticker):
        # For STOCKS, INDICES, FOREX, and CRYPTO
        PREVIOUS_CLOSE_Q = f'/v2/aggs/ticker/{ticker}/prev{self.ENDCAP}'
        self.CHUNK_tank.append(PREVIOUS_CLOSE_Q)
 
        # Get the daily open, high, low, and close (OHLC) for the entire specified market
    def groupeddaily(self, sfc, clock):
        # For STOCKS, FOREX, and CRYPTO
        GROUPED_DAILY_Q = f'/v2/aggs/grouped/locale/us/market/{sfc}/{self.DATE}{self.ENDCAP}'
        self.CHUNK_tank.append(GROUPED_DAILY_Q)
 
        # Get statistics for different types of data calculation
    def indicecalc(self, calc, indice):
        # !!FOR INDICES ONLY!!
        INDICES_CALC_Q = f'/v1/indicators/{calc}/{indice}{self.ENDCAP}'
        self.CHUNK_tank.append(INDICES_CALC_Q)
 

    def build_link_and_run_cal(self):

        # <---------------CALC--------------->
        thecalc = IndieMath(self.CALC)
        calc = thecalc.getCALC()
 

        # <---------------TICKER--------------->
        tickers = KellieTickler()
        stockindice = tickers.STOCKINDICE
        crypto = tickers.CRYPTO
        indice = tickers.INDICE
        alltickers = tickers.ALL
 
        # <---------------MULTIPLIER/TIMESPAN/FROM/TO/DATE--------------->
        all_agg_byday_time = TimeConstruct(MULTIPLIER=1, TIMESPAN="day", FROM="2018-09-05", TO="2023-08-31", DATE=None)
        stockindice_openclose_time = TimeConstruct(MULTIPLIER=None, TIMESPAN=None, FROM=None, TO=None, DATE="2018-09-05")
        stockforex_groupeddaily_time = TimeConstruct(MULTIPLIER=None, TIMESPAN=None, FROM=None, TO=None, DATE="2018-09-05")
        crypto_agg_byday_time = TimeConstruct(MULTIPLIER=1, TIMESPAN="day", FROM="2018-09-05", TO="2022-08-31", DATE=None)
        crypto_openclose_time = TimeConstruct(MULTIPLIER=None, TIMESPAN=None, FROM=None, TO=None, DATE="2018-09-05")
        crypto_groupeddaily_time = TimeConstruct(MULTIPLIER=None, TIMESPAN=None, FROM=None, TO=None, DATE="2018-09-05")
        AGG_clock = all_agg_byday_time.getAGG()
        SIOC_clock = stockindice_openclose_time.getOPENCLOSE()
        SFGD_clock = stockforex_groupeddaily_time.getGROUPED()
        CAGG_clock = crypto_agg_byday_time.getAGG()
        COC_clock = crypto_openclose_time.getCOPENCLOSE()
        CGD_clock = crypto_groupeddaily_time.getGROUPED()
 
        # <---------------SFC--------------->
        thesfc = SergeantFirstClass(self.SFC)
        sfc = 'stock'
        
        


        # Building df
        #self.df_stockdata = pd.DataFrame.from_dict(market_data)
        
        