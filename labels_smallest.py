import numpy as np
import pandas as pd

### GRADED
### Code a function called "labels_of_smallest"
### ACCEPT three inputs:
### 1&2: numpy arrays, corresponding to 1: a numeric column and 2: a label column.
### ### The i-th member of the numeric column corresponds to the i-th member of the label column
### 3: an integer (>0); n.

### RETURN a list (or numpy array) of the n labels corresponding to
### ### the n smallest values in the numeric column.
### NOTE: Make sure the order of labels corresponds to the order of values.

### Hint: The labels are found in har_train_labels or y
### Hint: `pd.concat()` might be useful for this or subsequent exercisces
### YOUR ANSWER BELOW


def labels_of_smallest(numeric, labels, n):

    """
    Return the n labels corresponding to the n smallest values in the "numeric"
    numpy array.

    Positional Arguments:
        numeric -- a numpy array of numbers
        labels -- a numpy array of labels (string or numeric)
            corresponding to the values in "numeric"
        n -- a positive integer

    Example:
        numeric = np.array([7,6,5,4,3,2,1])
        labels = np.array(["a","a","b","b","b","a","a"])
        n = 6

        print(labels_of_smallest(numeric, labels, n))
        #--> np.array(['a', 'a', 'b', 'b', 'b', 'a'])
    """

    lot = list()

    for x in range( len(numeric) ):

        thistuple = (numeric[x],labels[x])
        lot.append(thistuple)

    lot.sort(key=lambda tt: tt[0])
    lot = lot[:n]

    result = list()

    for tup in lot:
        result.append(tup[1])


    return result





numeric = np.array([7,6,5,4,3,2,1])
labels = np.array(["a","a","b","b","b","a","a"])
n = 6

print(labels_of_smallest(numeric, labels, n))





#
