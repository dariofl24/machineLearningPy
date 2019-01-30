import pandas as pd
import numpy as np

def entropy(class1_n, class2_n):
    # If all of one category, log2(0) does not exist,
    # and entropy = 0
    if (class1_n == 0) or (class2_n == 0):
        return 0

    # Find total number of observations
    total = class1_n + class2_n
    print(total)
    # find proportion of both classes
    class1_proprtion = class1_n/total
    print(class1_proprtion)
    class2_proportion = class2_n/total
    print(class2_proportion)
    print("=========")

    # implement entropy function
    return  sum([-1 * prop * np.log2(prop)
                 for prop in [class1_proprtion, class2_proportion] ])

def find_splits(col):

    col.sort()
    print(col)

    mids = []

    for x in range(col.size - 1):

        if(col[x] != col[x+1]):
            res = (col[x] + col[x+1])/2.
            mids.append(res)
            print(res)


    return np.array(mids)


def ent_from_split(col, split_value, labels):

    node1 = []
    node1_label = []
    n_label_1 = [0,0]

    node2 =[]
    node2_label =[]
    n_label_2 = [0,0]

    for x in range(col.size):

        if(col[x] <= split_value):
            node1.append(col[x])
            node1_label.append(labels[x])
            n_label_1[labels[x]] += 1
        else:
            node2.append(col[x])
            node2_label.append(labels[x])
            n_label_2[labels[x]] += 1

    ent_node_1 = entropy(float(n_label_1[0]),float(n_label_1[1]))
    ent_node_2 = entropy(float(n_label_2[0]),float(n_label_2[1]))

    prop_1 = float(len(node1_label)) / float(len(node1_label) + len(node2_label))
    prop_2 = float(len(node2_label)) / float(len(node1_label) + len(node2_label))

    split_entr = (ent_node_1 * prop_1) + (ent_node_2 * prop_2)

    return split_entr


def pred_from_split(X, y, col_idx, split_value):

    column = X[:,col_idx]

    print(column)

    node1 = []
    node2 = []

    n_label_1 = [0,0]
    n_label_2 = [0,0]

    for ii in range(column.size):

        val = column[ii]
        label = y[ii]
        print(val)
        print(label)

        if(val <= split_value):

            node1.append(val)
            n_label_1[label] += 1

        else:

            node2.append(val)
            n_label_2[label] += 1

    print("=====================")
    print(node1)
    print(n_label_1)
    print("+++++++++++++++++++++")
    print(node2)
    print(n_label_2)
    print("=====================")

    left_pred = 0
    right_pred = 0

    node1_class_0_n = float(n_label_1[0])
    node1_class_1_n = float(n_label_1[1])

    ratio_n1 = 0

    if((node1_class_0_n + node1_class_1_n) > 0):
        ratio_n1 = node1_class_1_n / (node1_class_0_n + node1_class_1_n)

    node2_class_0_n = float(n_label_2[0])
    node2_class_1_n = float(n_label_2[1])

    ratio_n2 = 0

    if((node2_class_0_n + node2_class_1_n) > 0):
        ratio_n2 = node2_class_1_n / (node2_class_0_n + node2_class_1_n)

    if(ratio_n1 < .5):
        left_pred = 0
    elif (ratio_n1 > .5):
        left_pred = 1

    if(ratio_n2 < .5):
        right_pred = 0
    elif (ratio_n2 > .5):
        right_pred = 1

    if( (ratio_n1 == .5) and (ratio_n2 == .5) ):

        left_pred = 1
        right_pred = 1

    elif ((ratio_n1 != .5) and (ratio_n2 == .5)):

        right_pred = 1 - left_pred

    elif ((ratio_n1 == .5) and (ratio_n2 != .5)):

        left_pred = 1 - right_pred


    return (left_pred, right_pred)


def simple_binary_tree_predict(X, col_idx, split_value, left_pred, right_pred):
    """
    Create an array of predictions built from: observations in one column of X,
        a given split value, and given predictions for when observations
        are less-than-or-equal-to that split or greater-than that split value

    Positional arguments:
        X -- a 2-dimensional numpy array of predictor variable observations.
            rows are observations, columns are different features
        col_idx -- an integer index, such that X[:,col_idx] yeilds all the observations
            in a single feature.
        split_value -- a numeric split, such that the values of X[:,col_idx] that are
            <= split_value are in the left node, and those > are in the right node.
        left_pred -- class (0 or 1), that is predicted when observations
            are less-than-or-equal-to the split value
        right_pred -- class (0 or 1), that is predicted when observations
            are greater-than the split value

    Example:
        X = np.array([[0.5, 3. ], [1.,  2. ], [3.,  0.5],
                [2.,  3. ], [3.,  4. ]])
        col_idx = 0
        split_value = 1.5
        left_pred = 1
        right_pred = 0

        preds = simple_binary_tree_predict(X, col_idx, split_value, left_pred, right_pred)

        print(preds) #--> np.array([1,1,0,0,0])

    """

    column = X[:,col_idx]
    classes = []

    for ii in range(column.size):

        val = column[ii]

        if(val <= split_value):
            classes.append(left_pred)
        else:
            classes.append(right_pred)



    return np.array(classes)



def default_weights(n):
    """
    Create the default list of weights, a numpy array of length n
    with each value equal to 1/n

    Example:
        n = 10
        dw = default_weights(n)
        print(dw) #--> np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])

    """

    nf = float(n)

    res = []

    for xx in range(n):
        res.append( 1.0/nf )


    return np.array(res)



def calc_epsilon(y_true, y_pred, weights):

    """
    Calculate the value of epsilon, given the above equation

    Positional Arguments:
        y_true -- An np.array of 1's and 0's corresponding to whether each observation is
            a member of class 1 or class 2
        y_pred -- An np.array of 1's and 0's corresponding to whether each observation was
            predicted to be a member of class 1 or class 2
        weights -- An np.array of floats corresponding to each observation's weight.
            All the weights will sum up to 1.

    Example:
        y_true = np.array([1,0,1,1,0])
        y_pred = np.array([0,0,0,1,0])
        weights = np.array([.4,.4,.1,.05,.05])

        ep = calc_epsilon(y_true, y_pred, weights)

        print(ep) # --> .5

    Assumptions:
        Assume both the true labels and the predictions are both all 0's and 1's.
    """

    eps = float(0)

    for xx in range(y_true.size):

        if(y_true[xx] != y_pred[xx] ):
            eps += weights[xx]

    return eps

def calc_alpha(epsilon):
    """
    Calculate the alpha value given the epsilon observed from a model

    Positional Argument:
        epsilon -- The epsilon value calculated from a particular model
    Example:
        ep = .4
        alpha = calc_alpha(ep)
        print(alpha) # --> 0.2027325540540821
    """

    if (epsilon == 0):
        return np.inf


    return 0.5 * np.log( (1. - epsilon)/epsilon )




ep = .4
alpha = calc_alpha(ep)
print(alpha) # --> 0.2027325540540821









#y_true = np.array([1,0,1,1,0])
#y_pred = np.array([0,0,0,1,0])
#weights = np.array([.4,.4,.1,.05,.05])

#ep = calc_epsilon(y_true, y_pred, weights)

#print(ep) # --> .5








#n = 10
#dw = default_weights(n)
#print(dw) #--> np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])





#X = np.array([[0.5, 3. ],[1.,  2. ],[3.,  0.5],[2.,  3. ],[3.,  4. ]])

#col_idx = 0
#split_value = 1.5
#left_pred = 1
#right_pred = 0

#preds = simple_binary_tree_predict(X, col_idx, split_value, left_pred, right_pred)
#print(preds) #--> np.array([1,1,0,0,0])










#X = np.array([[0.5, 3. ],[1.,  2. ],[3.,  0.5],
#              [2.,  3. ],[3.,  4. ]])

#y = np.array([ 1, 1, 0, 0, 1])

#col_idx = 0
#split_value = 1.5

#pred_at_nodes = pred_from_split(X, y, col_idx, split_value)
#print(pred_at_nodes) # --> (1, 0)


#col = np.array([1,1,2,2,3,3,4])
#split = 2.5
#labels = np.array([0,1,0,0,1,0,1])

#ent = ent_from_split(col, split, labels)
#print(ent) # --> 0.8571428571428571




#col = np.array([0.5, 1. , 3. , 2. , 3. , 3.5, 3.6, 4. , 4.5, 4.7])
#splits  = find_splits(col)
#print(splits) # --> np.array([0.75, 1.5, 2.5, 3.25, 3.55, 3.8, 4.25, 4.6])


















#
