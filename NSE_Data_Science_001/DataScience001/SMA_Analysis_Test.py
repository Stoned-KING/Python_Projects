#%%

#import libraries
import pandas as pd
import numpy as np
from datetime import date
from nsepy import get_history
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Store the data acquired from 'get_history' func in 'nsepy' to a variable 'StockData'
StockData = get_history(symbol="SBIN", start=date(2017,1,1), end=date(2021,1,31))

#Plot the Stock History taken from 'nsepy' using matplotlib.pyplot
plt.figure(figsize=(16, 10))
plt.plot(StockData['Close'], label = 'SBIN')
plt.title('Adjusted Closed Price History')
plt.xlabel('1.JAN.2017  -  31.JAN.2021')
plt.ylabel('Adjusted Close Price in INR')
plt.legend(loc = 'upper right')
plt.show

#%%
# Create SMA with 50 days time frame
SMA50 = pd.DataFrame()
SMA50['Close'] = StockData['Close'].rolling(window=50).mean()
SMA50

#%%
# Create SMA with 100 days time frame
SMA100 = pd.DataFrame()
SMA100['Close'] = StockData['Close'].rolling(window=100).mean()
SMA100

#%%

# visualize the data
plt.figure(figsize=(16, 10))
plt.plot(StockData['Close'], label = 'SBIN')
plt.plot(SMA50['Close'], label = 'SMA50')
plt.plot(SMA100['Close'], label = 'SMA100')
plt.title('Adjusted Closed Price History')
plt.xlabel('1.JAN.2017  -  31.JAN.2021')
plt.ylabel('Adjusted Close Price in INR')
plt.legend(loc = 'upper right')
plt.show

# %%

# create new dataframe to store all data
data = pd.DataFrame()
data['SBIN'] = StockData['Close']
data['SMA50'] = SMA50['Close']
data['SMA100'] = SMA100['Close']
data

# %%

def buy_sell(data):
  sigPriceBuy = []
  sigPriceSell = []
  flag = -1

  for i in range(len(data)):
    if data['SMA50'][i] > data['SMA100'][i]:
      if flag != 1:
        sigPriceBuy.append(data['SBIN'][i])
        sigPriceSell.append(np.nan)
        flag = 1
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    elif data['SMA50'][i] < data['SMA100'][i]:
      if flag != 0:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(data['SBIN'][i])
        flag = 0
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    else:
      sigPriceBuy.append(np.nan)
      sigPriceSell.append(np.nan)

  return (sigPriceBuy, sigPriceSell)

# %%

# store the buy sell data to a variable
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

# show the data
data

# %%

# visualize the data with the strategy to buy and sell
plt.figure(figsize=(16, 8))
plt.plot(data['SBIN'], label = 'SBIN', alpha = 0.40)
plt.plot(data['SMA50'], label = 'SMA50', alpha = 0.50)
plt.plot(data['SMA100'], label = 'SMA100', alpha = 0.50)
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'BUY', marker = '^', color = 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'SELL', marker = 'v', color = 'red')
plt.title('Adjusted Closed Price History With Buy and Sell Signals')
plt.xlabel('1.JAN.2017  -  31.JAN.2021')
plt.ylabel('Adjusted Close Price in INR')
plt.legend(loc = 'upper right')
plt.show

# %%
