#!/bin/bash

# tf022.bash

# This script should feed the gspc data to tf02.py

python prep_gspc.py
python tf02.py --train /tmp/gspc_train.csv --test /tmp/gspc_test.csv --num_epochs 100 --num_hidden 5

exit
