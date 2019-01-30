import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

### GRADED
### Build a function called "x_preprocess"
### ACCEPT one input, a numpy array
### ### Array may be one or two dimensions

### If input is two dimensional, make sure there are more rows than columns
### ### Then prepend a column of ones for intercept term
### If input is one-dimensional, prepend a one

### RETURN a numpy array, prepared as described above,
### which is now ready for matrix multiplication with regression weights

def get_trans(matt):

    if matt.shape[0] < matt.shape[1]:
        matt = np.transpose(matt)

        return matt

    return matt

def prepend_ones(matt):

    trans = np.transpose(matt)

    ones = np.ones((1,trans.shape[1]),dtype=int)

    result = np.append(ones, trans,axis = 0)

    return np.transpose(result)

def x_preprocess(input_x):
    """
    Reshape the input (if needed), and prepend a "1" to every observation

    Positional Argument:
        input_x -- a numpy array, one- or two-dimensional

    Example:
        input1 = np.array([[2,3,6,9],[4,5,7,10]])
        input2 = np.array([2,3,6])
        input3 = np.array([[2,4],[3,5],[6,7],[9,10]])

        for i in [input1, input2, input3]:
            print(x_preprocess(i), "\n")

        # -->[[ 1.  2.  4.]
              [ 1.  3.  5.]
              [ 1.  6.  7.]
              [ 1.  9. 10.]]

            [1 2 3 6]

            [[ 1.  2.  4.]
             [ 1.  3.  5.]
             [ 1.  6.  7.]
             [ 1.  9. 10.]]

    Assumptions:
        Assume that if the input is two dimensional, that the observations are more numerous
            than the features, and thus, the observations should be the rows, and features the columns
    """

    result = np.array([])

    if len(input_x.shape) > 1:
        matt = get_trans(input_x)
        result = prepend_ones(matt)
    else:
        result = np.insert(input_x, 0, 1)


    return result



input1 = np.array([[2,3,6,9],[4,5,7,10]])
input2 = np.array([2,3,6])
input3 = np.array([[2,4],[3,5],[6,7],[9,10]])



for i in [input1, input2, input3]:
    print(x_preprocess(i), "\n")













#
