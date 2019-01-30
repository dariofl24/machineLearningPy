import numpy as np
import pandas as pd

def get_trans(matt):

    if len(matt.shape) <= 1:
        len_2= 1
    else:
        len_2=matt.shape[1]

    if matt.shape[0] < len_2:
        matt = np.transpose(matt)

        return matt

    return matt

def prepend_ones(matt):

    trans = np.transpose(matt)

    ones = np.ones((1,trans.shape[1]),dtype=int)
    
    result = np.append(ones, trans,axis = 0)

    return np.transpose(result)

def prepare_data(input_x, target_y):
    """
    Confirm dimensions of x and y, transpose if appropriate;
    Add column of ones to x;
    Ensure y consists of 1's and -1's;
    Create weights array of all 0s

    Return X, y, and weights.

    Arguments:
        input_x - a numpy array
        target_y - a numpy array

    Returns:
        prepared_x -- a 2-d numpy array; first column consists of 1's,
            more rows than columns
        prepared_y -- a numpy array consisting only of 1s and -1s
        initial_w -- a 1-d numpy array consisting of "d+1" 0s, where
            "d+1" is the number of columns in "prepared_x"

    Example:
        x = np.array([[1,2,3,4],[11,12,13,14]])
        y = np.array([1,0,1,1])
        x,y,w = prepare_data(x,y)

        print(x) #--> array([[ 1,  1, 11],
                            [ 1,  2, 12],
                            [ 1,  3, 13],
                            [ 1,  4, 14]])

        print(y) #--> array([1, -1, 1, 1])

        print(w) #--> array([0., 0., 0.])

    Assumptions:
        Assume that there are more observations than features in `input_x`
    """

    for x in range(target_y.shape[0]):

        if(target_y[x] == 0):
            target_y[x] = -1

        print(target_y[x])

    input_x = get_trans(input_x)
    one_x = prepend_ones(input_x)

    initial_w = np.zeros( one_x.shape[1] )

    return one_x, target_y, initial_w




x = np.array([[1,2,3,4],[11,12,13,14]])
y = np.array([1,0,1,1])

print(prepare_data(x,y))


















    #
