# dow_hist.py

# This script should create a visualization of pctlead vs Day of Week AKA dow:
# Demo:
# ~/anaconda3/bin/python dow_hist.py

import pandas as pd

# I should get dates and prices.
df10 = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')

# I should compute pctlead:
df10['pctlead'] = (100.0 * (df10.Close.shift(1) - df10.Close) / df10.Close).fillna(0)

# I should compute dow:
dt_sr = pd.to_datetime(df10.Date)
dow_l = [int(dt.strftime('%w')) for dt in dt_sr]
df10['dow'] = dow_l

# Over the past 30 years I should collect pctlead vs dow:
yr30_i = 252 * 30
df11   = df10[1:yr30_i][['pctlead','dow']]
df11.columns = ['Pct-Lead-Sum','Day-of-Week']

# I should groupby dow and compute sum():
dow_gb_df = df11.groupby('Day-of-Week').sum()
print(dow_gb_df)

import matplotlib
import matplotlib.pyplot as plt

dow_gb_df.plot.bar(title="30 Year Pct-Lead-Sum vs Day-of-Week", figsize=(11,7))
plt.grid(True)
plt.show()

'bye'
