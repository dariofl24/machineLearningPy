import numpy as np
import pandas as pd

### GRADED
### Code a function called "all_distances"
### ACCEPT two inputs:
### An observation from a data set.  e.g: har_train.iloc[50,:]
### The full data set. e.g. har_train.

### Create a <list> or numpy array of distances between:
### ### that single point, and all points in the full dataset

### RETURN the list of distances SORTED from smallest to largest.

### Notes:
### Use `np.linalg.norm()`, as described in above cell.
### The smallest distance should be 0.

### YOUR ANSWER BELOW


def all_distances(test_point, data_set):
    """
    Find and return a list of distances between the "test_point"
    and all the points in "data_set", sorted from smallest to largest.

    Positional Arguments:
        test_point -- a Pandas Series corresponding to a row in "data_set"
        data_set -- a Pandas DataFrame

    Example:
        test_point = har_train.iloc[50,:]
        data_set = har_train

        print(all_distances(test_point, data_set)[:5])
        #--> [0.0, 2.7970187358249854, 2.922792670143521, 2.966555149052483, 3.033982453218797]

    """

    alldist = list()

    for x in range( data_set.shape[0] ):
        norm = np.linalg.norm( data_set.iloc[x,:] -  test_point)
        alldist.append(norm)

    alldist.sort()

    return alldist





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



test_point = har_train.iloc[50,:]
data_set = har_train

print(all_distances(test_point, data_set)[:5])

#
