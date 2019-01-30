import numpy as np

def lambda_matrix(lamb,n_size):

    ident =np.identity(n_size)

    return lamb * ident

def calculate_map_coefficients(input_x, output_y, lambda_param,sigma2):

    one_x = input_x

    one_t_one = np.matmul(np.transpose(one_x),one_x)

    x_lambda = lambda_matrix((lambda_param * sigma2),one_t_one.shape[0])

    lamb_one_t_one = np.add(x_lambda,one_t_one)

    one_p_inv = np.linalg.inv(lamb_one_t_one)

    x_prod = np.matmul(one_p_inv,np.transpose(one_x))

    w12 = np.matmul(x_prod,output_y)

    return w12

def estimate_data_noise(aug_x, output_y, weights):
    """Return empirical data noise estimate \sigma^2
    Use the LR weights in the equation supplied above

    Positional arguments:
        aug_x -- matrix of training input data
        output_y -- vector of training output values
        weights -- vector of LR weights calculated from output_y and aug_x


    Example:
        output_y = np.array([208500, 181500, 223500,
                                140000, 250000, 143000,
                                307000, 200000, 129900,
                                118000])
        aug_x = np. array([[   1., 1710., 2003.],
                           [   1., 1262., 1976.],
                           [   1., 1786., 2001.],
                           [   1., 1717., 1915.],
                           [   1., 2198., 2000.],
                           [   1., 1362., 1993.],
                           [   1., 1694., 2004.],
                           [   1., 2090., 1973.],
                           [   1., 1774., 1931.],
                           [   1., 1077., 1939.]])

        ml_weights = calculate_map_coefficients(aug_x, output_y, 0, 0)

        print(ml_weights)
        # --> [-2.29223802e+06  5.92536529e+01  1.20780450e+03]

        sig2 = estimate_data_noise(aug_x, output_y, ml_weights)
        print(sig2)
        #--> 1471223687.1593

    Assumptions:
        -- training_input_y is a vector whose length is the same as the
        number of rows in training_x
        -- input x has more observations than it does features.
        -- lambda_param has a value greater than 0
    """

    dot = np.dot(aug_x,weights)

    sum_sqrt =0

    for yy in range(len(output_y)):

        diff = output_y[yy]-dot[yy]

        sum_sqrt += diff ** 2

    denom = aug_x.shape[0] - aug_x.shape[1]

    result = sum_sqrt / denom


    return result


output_y = np.array([208500, 181500, 223500,
                        140000, 250000, 143000,
                        307000, 200000, 129900,
                        118000])
aug_x = np. array([[   1., 1710., 2003.],
                   [   1., 1262., 1976.],
                   [   1., 1786., 2001.],
                   [   1., 1717., 1915.],
                   [   1., 2198., 2000.],
                   [   1., 1362., 1993.],
                   [   1., 1694., 2004.],
                   [   1., 2090., 1973.],
                   [   1., 1774., 1931.],
                   [   1., 1077., 1939.]])

ml_weights = calculate_map_coefficients(aug_x, output_y, 0, 0)

dot = np.dot(aug_x,ml_weights)

print(ml_weights)
print(len(dot))
print(dot)

sum_sqrt =0

for yy in range(len(output_y)):

    diff = output_y[yy]-dot[yy]

    sum_sqrt += diff ** 2

    print(dot[yy])
    print(output_y[yy])

denom = aug_x.shape[0] - aug_x.shape[1]

print(aug_x.shape)
print(denom)
result = sum_sqrt / denom
print(result)













#
