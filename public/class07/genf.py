"""
genf.py

This script should generate a csv file full of features:
Day-of-Week (dow) and Month-of-Year (moy).
A synonym of feature is independent-variable.
This script should also generate a dependent variable called pctlead.
The input data is GSPC prices from Yahoo.
Demo:
~/anaconda3/bin/python genf.py

If you have questions, e-me: bikle101@gmail.com
"""

import numpy  as np
import pandas as pd

gspc0_df = pd.read_csv('http://tkrprice.herokuapp.com/static/gspc.csv')
gspc1_df         = gspc0_df.copy()[['Date','Close']]
gspc1_df.columns = ['cdate','cp']
# I should sort by cdate ascending
gspc_df          = gspc1_df.sort_values('cdate')
# I should compute pctlead and then get pctlag1 from it:
gspc_df['pctlead'] = (100.0 * (gspc_df.cp.shift(-1) - gspc_df.cp) / gspc_df.cp).fillna(0)
gspc_df['pctlag1'] = gspc_df.pctlead.shift(1).fillna(0)

# I should generate Date features:
dt_sr = pd.to_datetime(gspc_df.cdate)
dow_l = [float(dt.strftime('%w' )) for dt in dt_sr]
moy_l = [float(dt.strftime('%-m')) for dt in dt_sr]
gspc_df['dow'] = dow_l
gspc_df['moy'] = moy_l

# I should write to CSV file to be used later:
gspc_df.to_csv('feat.csv', float_format='%4.2f', index=False)
'bye'
