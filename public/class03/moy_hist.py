"""
moy_hist.py

This script should create a visualization of pctlead vs Month of Year AKA moy:
Demo:
~/anaconda3/bin/python moy_hist.py
"""

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# I should get dates and prices.
csv_df      = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
cdate_cp_df = csv_df.copy()[['cdate','cp']]

# I should compute pctlead:
cdate_cp_df['pctlead'] = (100.0 * (cdate_cp_df.cp.shift(-1) - cdate_cp_df.cp) / cdate_cp_df.cp).fillna(0)

# I should compute moy:
dt_sr = pd.to_datetime(cdate_cp_df.cdate)
moy_l = [int(dt.strftime('%-m')) for dt in dt_sr]
cdate_cp_df['moy'] = moy_l

# Over the past 30 years I should collect pctlead vs moy:
yr30_i                 = 252 * 30
cdate_moy_pctlead_df   = cdate_cp_df.iloc[-yr30_i:][['cdate','pctlead','moy']]
moy_pctlead_df         = cdate_moy_pctlead_df[['pctlead','moy']]
moy_pctlead_df.columns = ['Pct-Lead-Sum','Month-of-Year']

# I should groupby moy and compute sum():
moy_gb_df = moy_pctlead_df.groupby('Month-of-Year').sum()
# I should see a simple report:
print(moy_gb_df)

# I should see a plot of pct-lead vs MOY:
moy_gb_df.plot.bar(title="30 Year Pct-Lead-Sum vs Month-of-Year", figsize=(11,7))
plt.grid(True)
plt.show()

'bye'
