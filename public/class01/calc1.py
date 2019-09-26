"""
calc1.py
This script should calculate pctlag1 for a time series of closing prices.
"""

# pandas_datareader depends on shell command:
# conda install pandas-datareader

import pandas_datareader as pdr
import datetime

start_dt  = datetime.datetime(2016,  1,  1)
end_dt    = datetime.datetime(2016, 12, 31)
prices_df = pdr.DataReader('IBM', 'google', start_dt, end_dt)

# I should get the Close-column, which is closing-price, and shift it forward by 1:
lagprice_sr = prices_df.Close.shift(1)

# I should combine the above Series with prices_df.Close to get pctlag1 of prices_df.Close:
pct_lag1_sr = 100.0 * (prices_df.Close - lagprice_sr) / lagprice_sr

# I should visualize pct_lag1_sr:
prices_df['pct_lag1'] = pct_lag1_sr

# I should visualize only 3 columns of data:
vis_df = prices_df.copy()[['Close','pct_lag1']]

# I prefer the name closing_price instead of Close:
vis_df.columns = ['closing_price', 'pct_lag1']

print(vis_df.head(22))

'bye'
 
