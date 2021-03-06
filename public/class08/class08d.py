"""
class08d.py

This script should help me do the lab of class08.
Ref:
http://www.tsds4.us/cclasses/class08#lab

This script demonstrates some ideas:

 * Alternative Pandas Series syntax
 * Predicate creation with Pandas Series
 * Definition of Positive Prediction, Negative Prediction.
 * Definition of True Prediction, False Prediction.
 * Definition of True Positive, True Negative.
 * Definition of False Positive, False Negative.
 * Negation of Pandas Series
 * Pandas Logic And-Operator
 * DataFrame copy() method
 * Filling a column with DataFrame.loc method

Demo:
python class08d.py
"""

import pandas as pd
import numpy  as np

allpredictions_df = pd.read_csv('allpredictions.csv')
datepp_df         = allpredictions_df[['cdate','cp','prob_lr']]

# I should use NumPy to compute pct-lead for each cp.

cp_a              = np.array(datepp_df.cp)
# I should get the last element, copy it, append it:
last_elem_a       = cp_a[-1:]
lead_1toolong_a   = np.append(cp_a,last_elem_a)
# That is too long; I remove first element:
lead_a            = lead_1toolong_a[1:]
# I should test:
len(cp_a) == len(lead_a) # should be True

# I should use arithmetic:
pctlead_a = 100.0 * (lead_a - cp_a) / cp_a
# If this were JavaScript, I'd need to use a loop here.

# I should create a DataFrame with four columns:
dateppl_df            = datepp_df.copy() # first 3 columns
dateppl_df['pctlead'] = list(pctlead_a) # 4th

#
# Create DataFrame column named accuracy and fill it
# ########################################################

# Create a predicate to give me all positive predictions:

posp_sr = (dateppl_df.prob_lr >= 0.5)

# Create a predicate to give me all positive pctlead values

posl_sr = (dateppl_df.pctlead >= 0.0)

# I should get True Positives
tp_sr = posp_sr & posl_sr
# I should get True Negatives
tn_sr = (-posp_sr) & (-posl_sr)

# I should get False Positives
fp_sr = posp_sr & (-posl_sr)
# I should get False Negatives
fn_sr = (-posp_sr) & posl_sr

dateppla_df = dateppl_df.copy()

# I should initialize accuracy-column to be 'unknown':
dateppla_df['accuracy'] = ['unknown']*len(dateppla_df)

unk_sr = (dateppla_df.accuracy == 'unknown')
len(unk_sr) == len(dateppla_df) # Should be True

# I should copy accuracy indicators into DataFrame:
dateppla_df.loc[tp_sr,'accuracy'] = 'True Positive'
dateppla_df.loc[tn_sr,'accuracy'] = 'True Negative'

dateppla_df.loc[fp_sr,'accuracy'] = 'False Positive'
dateppla_df.loc[fn_sr,'accuracy'] = 'False Negative'

# The unknowns should be known now:
unk_sr = (dateppla_df.accuracy == 'unknown')
np.sum([int(bool) for bool in unk_sr]) == 0 # Should be true

# I should look at it:
print(dateppla_df[-22:])

'bye'
