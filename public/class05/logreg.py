# logreg.py

# This script should do logistic regression.
# Demo:
# python logreg.py
import pdb
import pandas as pd
import numpy  as np

# As of today, allpredictions.csv contains 8955 rows.
# 8900 - 2600 is 6300 is 6300 days is 25 years.
# I should learn from 25 years of data:
csv_df = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')[2599:8900]

train_df = csv_df[['pctlead', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']]
train_a  = np.array(train_df)

x_train_a = train_a[:,1:]
pctlead_a = train_a[:,0]
label_a   = (pctlead_a > np.median(pctlead_a))

# Now I should learn from x_train_a,pctlead_a:
from sklearn import linear_model
clf_lr = linear_model.LogisticRegression()
clf_lr.fit(x_train_a, label_a)

print('Intercept:')
print(clf_lr.intercept_)
print('Coefficients:')
print(clf_lr.coef_)
# The above model assumes that each label relies somewhat on pctlag1,2,4,8,16
# The model returns the probability that label is TRUE
# If the probability is above 0.51 I consider that a bullish prediction.
# If the probability is below 0.49 I consider that a bearish prediction.

# Now I should predict one observation (quiet day):
just1x = [[0.001, 0.001, 0.001, 0.001, 0.001]]
updown_prediction = clf_lr.predict_proba(just1x)[0,1]
print('quiet day prediction:')
print(updown_prediction)

# Now I should predict one observation (strong down day):
just1x = [[-2.1, -2.2, -2.4, -2.8, -2.16]]
updown_prediction = clf_lr.predict_proba(just1x)[0,1]
print('down day prediction:')
print(updown_prediction)

# Now I should predict one observation (strong up day):
just1x = [[2.1, 2.2, 2.4, 2.8, 2.16]]
updown_prediction = clf_lr.predict_proba(just1x)[0,1]
print('up day prediction:')
print(updown_prediction)
