"""
many_predictions_rpt.py
This script should report from data in many_predictions.csv

Demo:
python many_predictions_rpt.py
"""

import pandas as pd
import numpy  as np
import pdb

predictions_df = pd.read_csv('many_predictions.csv')
predictions_df.head()

# I should report long-only-effectiveness:
eff_lo_f = np.sum(predictions_df.pctlead)
print('Long-Only-Effectiveness:')
print(eff_lo_f)

# I should report Linear-Regression-Effectiveness:
eff_sr     = predictions_df.pctlead * np.sign(predictions_df.pred_linr)
predictions_df['eff_linr'] = eff_sr
eff_linr_f                 = np.sum(eff_sr)
print('Linear-Regression-Effectiveness:')
print(eff_linr_f)

# I should report GBRT-Regression-Effectiveness:
eff_sr     = predictions_df.pctlead * np.sign(predictions_df.pred_gbr)
predictions_df['eff_gbr'] = eff_sr
eff_gbr_f                 = np.sum(eff_sr)
print('GBRT-Regression-Effectiveness:')
print(eff_gbr_f)

# I should report Logistic-Regression-Effectiveness:
eff_sr     = predictions_df.pctlead * np.sign(predictions_df.pred_logr - 0.5)
predictions_df['eff_logr'] = eff_sr
eff_logr_f                 = np.sum(eff_sr)
print('Logistic-Regression-Effectiveness:')
print(eff_logr_f)
'bye'
