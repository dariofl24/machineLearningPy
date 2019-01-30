import numpy as np
import pandas as pd

from collections import Counter

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


lab1 = np.array([1,2,2,3,3])
lab2 = np.array(["a","a","b","b","b"])

print(label_voting(lab1)) #--> 2
print(label_voting(lab2)) #--> "b"
