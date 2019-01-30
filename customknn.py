import numpy as np
import pandas as pd

from collections import Counter

def labels_of_smallest(numeric, labels, n):

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

def label_voting(labels):
    """
    Given a numpy array of labels. Return the label that appears most frequently
    If there is a tie for most frequent, return the label that appears first.

    Positional Argument:
        labels -- a numpy array of labels

    Example:
        lab1 = np.array([1,2,2,3,3])
        lab2 = np.array(["a","a","b","b","b"])

        print(label_voting(lab1)) #--> 2
        print(label_voting(lab2)) #--> "b"

    """

    return Counter(labels).most_common(1)[0][0]

def custom_KNN( point, X_train, y_train, n):
    """
    Predict the label for a single point, given training data and a specified
    "n" number of neighbors.

    Positional Arguments:
        point -- a pandas Series corresponding to an observation of a point with
             unknown label.
        x_train -- a pandas DataFrame corresponding to the measurements
            of points in a dataset. Assume all values are numeric, and
            observations are in the rows; features in the columns
        y_train -- a pandas Series corresponding to the labels for the observations
            in x_train

    Example:
        point = pd.Series([1,2])
        X_train = pd.DataFrame([[1,2],[3,4],[5,6]])
        y_train = pd.Series(["a","a","b"])
        n = 2
        print(custom_KNN(point, X_train, y_train, n)) #--> 'a'
    """

    alldist = list()

    for x in range( X_train.shape[0] ):
        norm = np.linalg.norm( X_train.iloc[x,:] -  point)

        alldist.append( (norm,y_train[x]) )02012019175355

    alldist.sort(key=lambda tt: tt[0])
    alldist = alldist[:n]
    print(alldist)

    labs = list()

    for tt in alldist :
        labs.append(tt[1])


    return label_voting(labs)









point = pd.Series([1,2])
X_train = pd.DataFrame([[1,2],[3,4],[5,6]])
y_train = pd.Series(["a","a","b"])
n = 2
print(custom_KNN(point, X_train, y_train, n)) #--> 'a'


#
