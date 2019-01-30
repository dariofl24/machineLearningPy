import numpy as np

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

sigma = 1000


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


map_coef = calculate_map_coefficients(aug_x, output_y,lambda_param, sigma)
ml_coef = calculate_map_coefficients(aug_x, output_y, 0,0)

print(map_coef)
print(ml_coef)











#print(np.add(aa,bb))
