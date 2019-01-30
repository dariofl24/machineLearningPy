import numpy as np
import pandas as pd

def lambda_matrix(lamb,n_size):

    ident =np.identity(n_size)

    return lamb * ident

def calc_post_cov_mtx(aug_x, sigma, lambda_param):
    """
    Calculate the covariance of the posterior for Bayesian parameters

    Positional arguments:
        aug_x -- matrix of training input data; preprocessed
        sigma -- estimation of sigma^2
        lambda_param -- lambda parameter that controls how heavily
        to penalize large weight values

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
        lambda_param = 0.01

        ml_weights = calculate_map_coefficients(aug_x, output_y,0,0)

        sigma = estimate_data_noise(aug_x, output_y, ml_weights)

        print(calc_post_cov_mtx(aug_x, sigma, lambda_param))
        # --> [[ 9.99999874e+01 -1.95016334e-02 -2.48082095e-02]
               [-1.95016334e-02  6.28700339e+01 -3.85675510e+01]
               [-2.48082095e-02 -3.85675510e+01  5.10719826e+01]]

    Assumptions:
        -- training_input_y is a vector whose length is the same as the
        number of rows in training_x
        -- lambda_param has a value greater than 0

    """

    one_t_one = (1./sigma) * np.matmul(np.transpose(aug_x),aug_x)
    lamb_matt = lambda_matrix(lambda_param,one_t_one.shape[0])

    lamb_one_t_one = np.add(lamb_matt,one_t_one)

    one_p_inv = np.linalg.inv(lamb_one_t_one)

    return one_p_inv












#
