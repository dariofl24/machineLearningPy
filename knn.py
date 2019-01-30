import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

FEATURE_NAMES = '/Users/darioflores/Documents/machineLearn/uci/features.txt'
TRAIN_DATA = '/Users/darioflores/Documents/machineLearn/uci/train/X_train.txt'
TRAIN_LABELS = '/Users/darioflores/Documents/machineLearn/uci/train/y_train.txt'

# read feature names
feats = pd.read_table(FEATURE_NAMES, sep='\n', header=None)

# read in training data
har_train = pd.read_table(TRAIN_DATA, sep='\s+', header=None)

# read in training labels
har_train_labels = pd.read_table(TRAIN_LABELS, sep='\n', header=None, names=["label"], squeeze = True)

har_train.columns = feats.iloc[:,0]

print(har_train_labels.value_counts())

















#
