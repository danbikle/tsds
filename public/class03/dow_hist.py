"""
dow_hist.py

This script should create a visualization of pctlead vs Day of Week AKA dow:

Demo:
~/anaconda3/bin/python dow_hist.py
"""

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# I should get dates and prices.
csv_df      = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
cdate_cp_df = csv_df.copy()[['cdate','cp']]

# I should compute pctlead:
cdate_cp_df['pctlead'] = (100.0 * (cdate_cp_df.cp.shift(-1) - cdate_cp_df.cp) / cdate_cp_df.cp).fillna(0)

# I should compute dow:
dt_sr = pd.to_datetime(cdate_cp_df.cdate)
dow_l = [int(dt.strftime('%w')) for dt in dt_sr]
cdate_cp_df['dow'] = dow_l

# Over the past 30 years I should collect pctlead vs dow:
yr30_i                 = 252 * 30
cdate_dow_pctlead_df   = cdate_cp_df.iloc[-yr30_i:][['cdate','pctlead','dow']]
dow_pctlead_df         = cdate_dow_pctlead_df[['pctlead','dow']]
dow_pctlead_df.columns = ['Pct-Lead-Sum','Day-of-Week']

# I should groupby dow and compute sum():
dow_gb_df = dow_pctlead_df.groupby('Day-of-Week').sum()
print(dow_gb_df)

dow_gb_df.plot.bar(title="30 Year Pct-Lead-Sum vs Day-of-Week", figsize=(11,7))
plt.grid(True)
plt.show()

'bye'
