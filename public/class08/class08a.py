"""
class08a.py

This script should help me do the lab of class08.
Ref:
http://www.tsds4.us/cclasses/class08#lab

Demo:
rm -f                          allpredictions.csv
wget http://www.spy611.com/csv/allpredictions.csv
python class08a.py
"""

import pandas as pd

allpredictions_df = pd.read_csv('allpredictions.csv')

print(allpredictions_df.head())

'bye'
