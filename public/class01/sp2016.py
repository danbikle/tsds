"""
sp2016.py
This script should create a scatter-plot from 2016 data in allpredictions.csv
"""

import pandas            as pd
import matplotlib.pyplot as plt

spy611_df = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
sp0_sr    = spy611_df.cdate > '2016'
sp0_df    = spy611_df[sp0_sr]
x_sr      = sp0_df.pctlag1
y_sr      = sp0_df.pctlead

plt.scatter(x_sr, y_sr)
plt.show()

'bye'
