import numpy as np
import pandas as pd

def standardize( num_list):
    """
    Standardize the given list of numbers
    Positional arguments:
        num_list -- a list of numbers
    Example:
        num_list = [1,2,3,3,4,4,5,5,5,5,5]
        nl_std = standardize(num_list)
        print(np.round(nl_std,2))
        #--> np.array([-2.11, -1.36, -0.61, -0.61,
                0.14,  0.14,  0.88,  0.88,  0.88,
                0.88,  0.88])
    """

    standard_dev = np.std(num_list)
    mean = np.mean(num_list)

    print(standard_dev)
    print(mean)

    result = list()

    for xx in num_list:
        result.append( (xx-mean)/standard_dev )

    return result

def preprocess_for_regularization(data, y_column_name, x_column_names):
    y_set = data[y_column_name]

    y_mean = np.mean(y_set)
    print("y_mean")
    print(y_mean)

    y_mean_center = lambda yy : yy - y_mean

    centered_y =data[y_column_name].map(y_mean_center)

    print(centered_y)

    data[y_column_name] = centered_y

    for x_col_name in x_column_names:

        x_data = data[x_col_name]

        x_std_dev = np.std(x_data)
        x_mean = np.mean(x_data)

        x_mean_center = lambda xx : (xx - x_mean)/x_std_dev

        new_data = data[x_col_name].map(x_mean_center)
        data[x_col_name] = new_data

        print(x_col_name)
        print(x_std_dev)
        print(x_mean)
        print(new_data)
        print("**************************")

    x_column_names.append(y_column_name)
    print(x_column_names)

    return data[x_column_names]

tr_path = './train.csv'

data = pd.read_csv(tr_path)

print("============================")

prepro_data = preprocess_for_regularization(data,'SalePrice', ['GrLivArea','YearBuilt'])
print(prepro_data)




















print("============================")
