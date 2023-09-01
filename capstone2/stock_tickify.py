### Stock Ticker Compiling and Cleaning ###

#imports

import pandas as pd
import json

#Reading in the CSV's

dfamex = pd.read_csv('/home/user/Documents/coding_temple/Capstone/capstone2/AMEX_list.csv')
dfnasdaq = pd.read_csv('/home/user/Documents/coding_temple/Capstone/capstone2/NASDAQ_list.csv')
dfnyse = pd.read_csv('/home/user/Documents/coding_temple/Capstone/capstone2/NYSE_list.csv')
dfforexfull = pd.read_csv('/home/user/Documents/coding_temple/Capstone/capstone2/FOREX.csv')
dfallindice = pd.read_csv('/home/user/Documents/coding_temple/Capstone/capstone2/allindices.csv')
with open('/home/user/Documents/coding_temple/Capstone/capstone2/cryptocurrencies.json', 'r') as f:
    cryptodict = json.load(f)
    f.close()

#  Next we are pulling the data from the csv's and cleaning
#  --------------- them down to one organized list of TICKER strings

#NYSE market 
dfnyse = dfnyse['Symbol']
dfnyse = list(dfnyse)

#AMEX market 
dfamex = dfamex['Symbol']
dfamex = list(dfamex)

#NASDAQ market
dfnasdaq = dfnasdaq['Symbol']
dfnasdaq = list(dfnasdaq)

#FOREX market
dfforexfull = list(dfforexfull['Symbol'])
dfforex = []
for indice in dfforexfull:
    if "USD" in indice:
        dfforex.append(indice[0:6]) 

#CRYPTO market
dfcrypto = list(cryptodict.keys())
#dfcrypto



#Indices
dfindices1 =[]
dfindices = []
dfindices1.append(str(list(dfallindice['$AMEX International Market Index Adr'])))
dfindices1 = list(dfindices1[0])

#   The cvs data for the indices was extremely jumbled and took a few
#   -------------------------- funny lookin' steps in order to 
del dfindices1[0] #---------------- get it how its needed 
del dfindices1[-1]
del dfindices1[0]
del dfindices1[-1]
dfindices = ''.join(dfindices1)
dfindices = ''.join(dfindices)
dfindices = dfindices.split(dfindices[0])
dfindices[0] = "AMEX', 'International Market Index Adr', '"
indicelist = []
for x in range(len(dfindices)):
    dfindices[x] = dfindices[x].replace("'", "")
    dfindices[x] = dfindices[x].replace(",","")
    dfindices[x] = dfindices[x].split()
    indicelist.append(dfindices[x][0])
    dfindices[x] = (''.join(dfindices[x][1:]))
dfindices # rest of info for tickers
dfindice = indicelist



#options_ticker = f'{tick}{expdate}{callput}{strike}'
#                     6 (yy)(mm)(dd) (c/p)  00000000


# Final TICKER Dictionary
TICKERDICT = {'NYSE' : dfnyse,
              'AMEX' : dfamex, 
              'NASDAQ' : dfnasdaq ,
              'FOREX' : dfforex ,
              'CRYPTO' : dfcrypto, 
              'INDICE' : dfindice
              }


#Our class to reference over
class KellieTickler():
    NYSE = TICKERDICT['NYSE']
    AMEX = TICKERDICT['AMEX']
    NASDAQ = TICKERDICT['NASDAQ']
    STOCK = TICKERDICT['NYSE']+TICKERDICT['AMEX']+TICKERDICT['NASDAQ']
    FOREX = TICKERDICT['FOREX']
    INDICE = TICKERDICT['INDICE']
    STOCKFOREX = STOCK+FOREX
    STOCKINDICE = STOCK+INDICE
    CRYPTO = TICKERDICT['CRYPTO']
    ALL = TICKERDICT['NYSE']+TICKERDICT['AMEX']+TICKERDICT['NASDAQ']+TICKERDICT['FOREX']+TICKERDICT['INDICE']
    