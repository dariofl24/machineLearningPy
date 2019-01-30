import numpy as np

training_y = np.array([208500, 181500, 223500,
                                140000, 250000, 143000,
                                307000, 200000, 129900,
                                118000])

training_x = np.array([[1710, 1262, 1786,
                                1717, 2198, 1362,
                                1694, 2090, 1774,
                                1077],
                               [2003, 1976, 2001,
                                1915, 2000, 1993,
                                2004, 1973, 1931,
                                1939]])


lambda_param = 10

def get_trans(matt):
    print('MATT')
    print(matt)
    print('SHAPE')
    print(matt.shape)

    if len(matt.shape) <= 1:
        len_2= 1
    else:
        len_2=matt.shape[1]

    if matt.shape[0] < len_2:
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

def lambda_matrix(lamb,n_size):

    ident =np.identity(n_size)

    return lamb * ident

def ridge_regression_weights(input_x, output_y, lambda_param):

    input_x = get_trans(input_x)
    output_y = get_trans(output_y)

    one_x = prepend_ones(input_x)

    one_t_one = np.matmul(np.transpose(one_x),one_x)

    x_lambda = lambda_matrix(lambda_param,one_t_one.shape[0])

    lamb_one_t_one = np.add(x_lambda,one_t_one)

    one_p_inv = np.linalg.inv(lamb_one_t_one)

    x_prod = np.matmul(one_p_inv,np.transpose(one_x))

    w12 = np.matmul(x_prod,output_y)

    return w12


print(ridge_regression_weights(training_x,training_y,0.00044))





#print(lambda_matrix(88,4))

#aa=2*np.identity(2)
#bb=3*np.identity(2)

#print(np.add(aa,bb))
