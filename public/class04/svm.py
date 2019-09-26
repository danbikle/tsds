"""
svm.py

This script is a simple demo of using scikit-learn to run SVM.

Demo:
python svm.py
"""

import pandas as pd
import numpy  as np
import pdb
from sklearn.svm import SVC

# I should use Pandas here:
data_df  = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
train_sr = (data_df['cdate'] > '1990') & (data_df['cdate'] < '2016')
test_sr  =  data_df['cdate'] == '2017-06-26'
train_df = data_df[['pctlead', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']][train_sr]
test_df  = data_df[['pctlead', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']][test_sr]
train_a       = np.array(train_df)
x_train_a     = train_a[:,1:]
y_train_a     = train_a[:,0]
# I could set the class boundry at 0.0 rather than median of y_train_a.
# So, lets try that:
label_train_a = y_train_a > 0.0

# I should ask sklearn to give me a Linear SVM Classifier Algorithm:
clf_svm_lin = SVC(kernel="linear", C=0.025, probability=True)

# I should use the Algo to fit a model to the training data:
clf_svm_lin.fit(x_train_a, label_train_a)

# Now that I have learned, I should predict:
test_a   = np.array(test_df)
x_test_a = test_a[:,1:]
xf_a     = x_test_a.astype(float)
xr_a     = xf_a.reshape(1, -1)

aprediction_lr = clf_svm_lin.predict_proba(xr_a)[0,1]

print('The probability that 2017-06-26 will go up is...')
print(aprediction_lr)

'bye'
