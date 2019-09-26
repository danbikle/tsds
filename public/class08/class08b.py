"""
class08b.py

This script should help me do the lab of class08.
Ref:
http://www.tsds4.us/cclasses/class08#lab

Demo:
python class08b.py
"""
import pandas as pd

allpredictions_df = pd.read_csv('allpredictions.csv')
datepp_df         = allpredictions_df[['cdate','cp','prob_lr']]
print(datepp_df.head())

'bye'
