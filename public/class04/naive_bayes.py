"""
naive_bayes.py

This script is a simple demo of using scikit-learn to run Naive Bayes.

Demo:
python naive_bayes.py
"""

import pandas as pd
import numpy  as np
import pdb
from sklearn.naive_bayes import GaussianNB

# I should use Pandas here:
data_df  = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
train_sr = (data_df.cdate > '1990') & (data_df.cdate < '2016')
test_sr  =  data_df.cdate == '2017-06-26'
train_df = data_df[['pctlead', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']][train_sr]
test_df  = data_df[['pctlead', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']][test_sr]

train_a   = np.array(train_df)
x_train_a = train_a[:,1:]
y_train_a = train_a[:,0]

train_median  = np.median(y_train_a)
label_train_a = y_train_a > train_median
# I should learn from x_train_a,label_train_a:
clf_nb = GaussianNB()
clf_nb.fit(x_train_a, label_train_a)

# Now that I have learned, I should predict:
test_a   = np.array(test_df)
x_test_a = test_a[:,1:]
xf_a     = x_test_a.astype(float)
xr_a     = xf_a.reshape(1, -1)

aprediction_nb = clf_nb.predict(xr_a)[0]

print('I predict that 2017-06-27 will be higher than 2017-06-26 is...')
print(aprediction_nb)

'bye'
