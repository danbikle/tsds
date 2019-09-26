#!/bin/bash

# tf013.bash

# This script should wrap tf01.py

# I should get the data into convenient CSV format:
python prep_gspc.py

# I should call tf01.py which uses softmax algo:
python tf01.py --train /tmp/gspc_train.csv --test /tmp/gspc_test.csv --num_epochs 10 --verbose True

exit
