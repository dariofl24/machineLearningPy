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

def sigmoid_single(x, y, w):
    """
    Obtain the value of a Sigmoid using training data.

    Arguments:
        x - a vector of length d
        y - either 1, or -1
        w - a vector of length d

    Example:
        x = np.array([23.0,75])
        y = -1
        w = np.array([2,-.5])
        sig = sigmoid_single(x, y, w)

        print(sig) #--> 0.0002034269780552065

        x2 = np.array([ 1. , 22., 0. , 1. , 7.25 , 0. , 3. , 1. , 1.])
        w2 = np.array([ -10.45 , -376.7215 , -0.85, -10.5 , 212.425475 , -1.1, -36.25 , -17.95 , -7.1])
        y2 = -1
        sig2 = sigmoid_single(x2,y2,w2)

        print(sig2) #--> 1
    """

    aarg= y * np.dot(x,w)

    exxp = np.exp(aarg)

    result = 0

    if(exxp >= np.inf):
        result = 1
    else:
        result = (exxp / (1. + exxp))

    return result


def to_sum(x,y,w):
    """
    Obtain the value of the function that will eventually be summed to
    find the gradient of the log-likelihood.

    Arguments:
        x - a vector of length d
        y - either 1, or -1
        w - a vector of length d

    Example:
        x = np.array([23.0,75])
        y = -1
        w = np.array([.1,-.2])
        print(to_sum(x,y,w)) # --> array([-7.01756737e-05, -2.28833719e-04])

    """

    diif = (1. - sigmoid_single(x,y,w)) * y

    return diif * x

def sum_all(x_input, y_target, w):
    """
    Obtain and return the gradient of the log-likelihood

    Arguments:
        x_input - *preprocessed* an array of shape n-by-d
        y_target - *preprocessed* a vector of length n
        w - a vector of length d

    Example:
        x = np.array([[1,22,7.25],[1,38,71.2833]])
        y = np.array([-1,1])
        w = np.array([.1,-.2, .5])
        print(sum_all(x,y,w)) #--> array([-0.33737816, -7.42231958, -2.44599168])

    """

    sum_result = np.zeros(w.shape[0])

    for ii in range(x_input.shape[0]):

        sum_result = sum_result + to_sum(x_input[ii],y_target[ii],w)

    return sum_result

def update_w(x_input, y_target, w, eta):
    """Obtain and return updated Logistic Regression weights

    Arguments:
        x_input - *preprocessed* an array of shape n-by-d
        y_target - *preprocessed* a vector of length n
        w - a vector of length d
        eta - a float, positive, close to 0

    Example:
        x = np.array([[1,22,7.25],[1,38,71.2833]])
        y = np.array([-1,1])
        w = np.array([.1,-.2, .5])
        eta = .1

        print(update_w(x,y,w, eta)) #--> array([ 0.06626218, -0.94223196,  0.25540083])
"""

    summ = sum_all(x_input, y_target, w)

    return w + (eta * summ)


def fixed_iteration(x_input, y_target, eta, steps):

    """
    Return weights calculated from 'steps' number of steps of gradient descent.

    Arguments:
        x_input - *NOT-preprocessed* an array
        y_target - *NOT-preprocessed* a vector of length n
        eta - a float, positve, close to 0
        steps - an int

    Example:
        x = np.array([[22,7.25],[38,71.2833],[26,7.925],[35,53.1]])
        y = np.array([-1,1,1,1])
        eta = .1
        steps = 100

        print(fixed_iteration(x,y, eta, steps)) #--> np.array([-0.9742495,  -0.41389924, 6.8199374 ])

    """

    x,y,w = prepare_data(x_input, y_target)

    print(w)

    for ii in range(steps):

        w = update_w(x,y,w,eta)
        print(w)


    return w



x = np.array([[22,7.25],[38,71.2833],[26,7.925],[35,53.1]])
y = np.array([-1,1,1,1])
eta = .1
steps = 100

print(fixed_iteration(x,y, eta, steps)) #--> np.array([-0.9742495,  -0.41389924, 6.8199374 ])










#x = np.array([[1,22,7.25],[1,38,71.2833]])
#y = np.array([-1,1])
#w = np.array([.1,-.2, .5])
#eta = .1

#print(update_w(x,y,w, eta)) #--> array([ 0.06626218, -0.94223196,  0.25540083])








#x = np.array([[1,22,7.25],[1,38,71.2833]])
#y = np.array([-1,1])
#w = np.array([.1,-.2, .5])
#print(sum_all(x,y,w)) #--> array([-0.33737816, -7.42231958, -2.44599168])









#x = np.array([23.0,75])
#y = -1
#w = np.array([.1,-.2])
#print(to_sum(x,y,w)) # --> array([-7.01756737e-05, -2.28833719e-04])




#x = np.array([23.0,75])
#y = -1
#w = np.array([2,-.5])
#sig = sigmoid_single(x, y, w)

#print(sig) #--> 0.0002034269780552065

#x2 = np.array([ 1. , 22., 0. , 1. , 7.25 , 0. , 3. , 1. , 1.])
#w2 = np.array([ -10.45 , -376.7215 , -0.85, -10.5 , 212.425475 , -1.1, -36.25 , -17.95 , -7.1])
#y2 = -1
#sig2 = sigmoid_single(x2,y2,w2)

#print(sig2) #--> 1









#
