readme_nn.txt

To write a script which demonstrates Neural Networks, I rely on TensorFlow.

I follow these steps.

If I have anaconda3 installed, I move it out of the way with shell commands:

cd ~
mv anaconda3 anaconda3backup

Then I install anaconda3 with more shell commands:

cd ~
curl http://repo.continuum.io/archive/Anaconda3-4.0.0-Linux-x86_64.sh > Anaconda3-4.0.0-Linux-x86_64.sh
bash Anaconda3-4.0.0-Linux-x86_64.sh
cd ~/anaconda3/bin
mv curl curl_ana
cd ~
echo 'export PATH=${HOME}/anaconda3/bin:$PATH' >> ~/.bashrc
bash

Next I install TensorFlow with one shell command:

pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp35-cp35m-linux_x86_64.whl

Then I clone a simple git repo with these shell commands:

cd ~
rm -rf try-tf
git clone https://github.com/jasonbaldridge/try-tf

Using more shell commands,
I enhance the repo so I can run a script with python3:

cd ~/try-tf
sed '/print/s/print/print(/' hidden.py | sed '/print/s/$/)/' > hidden35.py
sed -i '/for line in file/s/file/open/' hidden35.py
sed -i '/xrange/s/xrange/range/'        hidden35.py
diff hidden.py hidden35.py

I run a demo with python3:

~/anaconda3/bin/python hidden35.py --train simdata/moon_data_train.csv --test simdata/moon_data_eval.csv --num_epochs 100 --num_hidden 5

If that runs okay, I am confident that hidden35.py works well enough.

Next I prepare some stock market data for hidden35.py

I create a python script with this syntax inside it:

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

train_df.to_csv('gspc_train.csv', float_format='%4.3f', index=False, header=False)
test_df.to_csv( 'gspc_test.csv' , float_format='%4.3f', index=False, header=False)

'bye'

After I create the above script I run it:

python prep_gspc.py

The above script should give me two CSV files.

I should format the first column in each file with 6 shell commands:

sed -i '/^0.000/s/0.000/0/' gspc_train.csv
sed -i '/^0.000/s/0.000/0/' gspc_test.csv

sed -i '/^1.000/s/1.000/1/' gspc_train.csv
sed -i '/^1.000/s/1.000/1/' gspc_test.csv

sed -i '/^-1.000/s/-1.000/0/' gspc_train.csv
sed -i '/^-1.000/s/-1.000/0/' gspc_test.csv


Then, I run hidden35.py which runs a neural network to classify my stock market data:

~/anaconda3/bin/python hidden35.py --train gspc_train.csv --test gspc_test.csv --num_epochs 100 --num_hidden 5

And that ends the demo.

For more info about TensorFlow, check out the introduction:

https://www.tensorflow.org/versions/r0.9/get_started/index.html

