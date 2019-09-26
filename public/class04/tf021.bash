#!/bin/bash

# tf021.bash

# This script should feed the moon data to tf02.py

python tf02.py --train try_tf/simdata/moon_data_train.csv --test try_tf/simdata/moon_data_eval.csv --num_epochs 100 --num_hidden 5

exit
