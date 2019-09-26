#!/bin/bash

# tf011.bash

# This script should wrap tf01.py

python tf01.py \
       --train try_tf/simdata/linear_data_train.csv \
       --test try_tf/simdata/linear_data_eval.csv \
       --num_epochs 5 \
       --verbose True

exit
