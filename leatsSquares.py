import numpy as np


training_y = np.array([[208500, 181500, 223500,
                        140000, 250000, 143000,
                        307000, 200000, 129900,
                        118000]])
training_x = np.array([[1710, 1262, 1786,
                        1717, 2198, 1362,
                        1694, 2090, 1774,
                        1077],
                        [2003, 1976, 2001,
                        1915, 2000, 1993,
                        2004, 1973, 1931,
                        1939]])

def get_trans(matt):

    if matt.shape[0] < matt.shape[1]:
        matt = np.transpose(matt)

        return matt

    return matt

def prepend_ones(matt):
    print(matt)
    trans = np.transpose(matt)

    ones = np.ones((1,trans.shape[1]),dtype=int)
    print(ones)
    print(trans)

    result = np.append(ones, trans,axis = 0)

    return np.transpose(result)

def least_squares_weights(input_x, target_y):

    input_x = get_trans(input_x)
    target_y = get_trans(target_y)

    print(input_x)
    print(target_y)
    print("-------------------------------")
    one_x = prepend_ones(input_x)

    print(one_x)

    one_t_one = np.matmul(np.transpose(one_x),one_x)

    one_p_inv = np.linalg.inv(one_t_one)

    x_prod = np.matmul(one_p_inv,np.transpose(one_x))

    w12 = np.matmul(x_prod,target_y)

    print("===================================")

    print(w12)





least_squares_weights(training_x,training_y)
