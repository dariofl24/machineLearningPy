import numpy as np
import pandas as pd
### GRADED
### Code a function called "predict"
### ACCEPT four inputs, three numpy arrays, and one number:
### A 1-dimensional array corresponding to an augmented_x vector.
### A vector corresponding to the MAP weights, or "mu"
### A square matrix for the "big_sigma" term
### A positive number for the "sigma_squared" term

### Using the above equations

### RETURN mu_0 and sigma_squared_0 - a point estimate and variance
### for the prediction for x.

### YOUR ANSWER BELOW

def predict( aug_x, weights, big_sig, sigma):
    """
    Calculate point estimates and uncertainty for new values of x

    Positional Arguments:
        aug_x -- augmented matrix of observations for predictions
        weights -- MAP weights calculated from Bayesian LR
        big_sig -- The posterior covarience matrix, from Bayesian LR
        sigma -- The observed uncertainty in Bayesian LR

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

        map_weights = calculate_map_coefficients(aug_x, output_y, lambda_param, sigma)

        big_sig = calc_post_cov_mtx(aug_x, sigma, lambda_param)

        to_pred2 = np.array([1,1700,1980])

        print(predict(to_pred2, map_weights, big_sig, sigma))
        #-->(158741.6306608729, 1593503867.9060116)

    """

    mu_0 = np.dot(aug_x,weights)

    sigma_squared_0 = sigma + np.matmul(np.transpose(aug_x),np.matmul(big_sig,aug_x))

    return mu_0, sigma_squared_0










#
