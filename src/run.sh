#!/bin/sh

python train.py --fold 0 --model rf
python train.py --fold 1 --model rf
# python train.py --fold 1
# python train.py --fold 2
# python train.py --fold 3
# python train.py --fold 4
