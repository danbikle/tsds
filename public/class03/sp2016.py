"""
sp2016.py

This script should create a scatter-plot from 2016 data in allpredictions.csv
"""

import pandas as pd
import matplotlib.pyplot as plt

easier_df = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
cdate1_sr = easier_df['cdate'] > '2016'
cdate2_sr = easier_df['cdate'] < '2017'
cdate_sr  = cdate1_sr & cdate2_sr
sp0_df    = easier_df[cdate_sr]
x_sr      = sp0_df['pctlag1']
y_sr      = sp0_df['pctlead']

plt.scatter(x_sr, y_sr)
plt.show()

'bye'
