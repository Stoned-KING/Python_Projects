#%%

#import libraries
import pandas as pd
import numpy as np
from datetime import date
from nsepy import get_history
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
#%%
# Change values here...
#Stock Name; Date format yyyy,mm,dd ; sma1 and sma2 are Simple Moving Average 1 and 2
Stock ='sbin'
SD = date(2011,1,1)
ED = date(2021,2,26)
sma1 = 7
sma2 = 9
# Store the data acquired from 'get_history' func in 'nsepy' to a variable 'StockData'
StockData = get_history(symbol= Stock.upper() , start= SD, end= ED)
# Create SMA with 50 days time frame
SMA50 = pd.DataFrame()
SMA50['Close'] = StockData['Close'].rolling(window=sma1).mean()
SMA50
# Create SMA with 100 days time frame
SMA100 = pd.DataFrame()
SMA100['Close'] = StockData['Close'].rolling(window=sma2).mean()
SMA100
# create new dataframe to store all data
data = pd.DataFrame()
data['STOCK'] = StockData['Close']
data['SMA01'] = SMA50['Close']
data['SMA02'] = SMA100['Close']
data

def buy_sell(data):
  sigPriceBuy = []
  sigPriceSell = []
  flag = -1

  for i in range(len(data)):
    if data['SMA01'][i] > data['SMA02'][i]:
      if flag != 1:
        sigPriceBuy.append(data['STOCK'][i])
        sigPriceSell.append(np.nan)
        flag = 1
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    elif data['SMA01'][i] < data['SMA02'][i]:
      if flag != 0:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(data['STOCK'][i])
        flag = 0
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    else:
      sigPriceBuy.append(np.nan)
      sigPriceSell.append(np.nan)

  return (sigPriceBuy, sigPriceSell)

# store the buy sell data to a variable
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]
# visualize the data with the strategy to buy and sell
plt.figure(figsize=(16, 8))
plt.plot(data['STOCK'], label = 'Stock ' + str(Stock).upper() , alpha = 0.40)
plt.plot(data['SMA01'], label = 'SMA' + str(sma1), alpha = 0.50)
plt.plot(data['SMA02'], label = 'SMA' + str(sma2), alpha = 0.50)
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'BUY', marker = '^', color = 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'SELL', marker = 'v', color = 'red')
plt.title('Adjusted Closed Price History With Buy and Sell Signals')
plt.xlabel(str(SD) + " to " + str(ED))
plt.ylabel('Adjusted Close Price in INR')
plt.legend(loc = 'upper right')
plt.show
# %%
