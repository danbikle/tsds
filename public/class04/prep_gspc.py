# prep_gspc.py

# This script should prep /tmp/gspc_train.csv and /tmp/gspc_test.csv for TensorFlow.

# Demo:
# python prep_gspc.py

import pandas as pd

# I should use Pandas here:
data_df  = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
train_sr = (data_df['cdate'] > '2000') & (data_df['cdate'] < '2016')
test_sr  =  data_df['cdate'] > '2016'
train_df = data_df[['actual_dir', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']][train_sr]
test_df  = data_df[['actual_dir', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']][test_sr]

train_df.to_csv('/tmp/gspc_train.csv', float_format='%4.3f', index=False, header=False)
test_df.to_csv( '/tmp/gspc_test.csv' , float_format='%4.3f', index=False, header=False)

'bye'
