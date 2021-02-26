#%%
# import libraries
import pandas as pd
import numpy as np
from datetime import date
from nsepy import get_history

#%%
# import data with nsepy "get_history function"
Stock = 'Gail'
StockData = get_history(symbol= Stock, start=date(2020, 1, 1), end=date(2020, 12, 31))

#%%
# storing and printing as dataframe
df = pd.DataFrame.from_records(StockData)
df

# %%
df.shape
df.info

# %%
pd.set_option('display.max_columns', 16)
pd.set_option('display.max_rows', 260)
# %%
df.head(20)
# %%
df['Close']
df [['Open','High']]
# %%
df.columns
# %%
df['%Deliverble']
# %%
df.iloc[[0,5], [10,11]]
# %%
df.loc[[0,5],['Turnover','Trades']]
# %%
df['Close'].value_counts()
# %%
df.iloc[3]
# %%
df.index

# %%
df.set_index('VWAP', inplace=True)

# %%
df
# %%
df.reset_index(inplace=True)
# %%
df.sort_index(ascending=True)
# %%
df.loc[[0],['VWAP']]
# %%
vwap = [126.53,127.26]
filt =df['VWAP'].isin(vwap)
# %%

# %%
df.loc[-filt,['VWAP']]

# %%
df.applymap(len)
# %%
