#!/bin/bash

# Set your paths
PI_USER="gurov"
PI_HOST="160.85.152.248"
PI_PATH="/home/gurov/Monitoring_kombucha_growth/data/"
LOCAL_PATH="/c/Users/gurov/Python_Projects/BA/data/Experiment_1/"

# Sync from Raspberry Pi to your local PC
rsync -avz ${PI_USER}@${PI_HOST}:${PI_PATH} ${LOCAL_PATH}
