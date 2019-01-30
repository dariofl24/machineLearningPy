import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }


def column_cutoff(data_frame, cutoffs):
    """Subset data frame by cutting off limits on column values.

    Positional arguments:
        data -- pandas DataFrame object
        cutoffs -- list of tuples in the format:
        (column_name, min_value, max_value)

    Example:
        data_frame = read_into_data_frame('train.csv')
        # Remove data points with SalePrice < $50,000
        # Remove data points with GrLiveAre > 4,000 square feet
        cutoffs = [('SalePrice', 50000, 1e10), ('GrLivArea', 0, 4000)]
        selected_data = column_cutoff(data_frame, cutoffs)
    """

    column_names = list()

    for x in cutoffs:
      column_names.append(x[0])

    print(column_names)

    for xx in cutoffs:
        data2 = data_frame[data_frame[xx[0]] <= xx[2]]
        data_frame=data2[data2[xx[0]] >= xx[1]]

    new_df=data_frame[column_names]

    print(new_df)

    return new_df


data = pd.DataFrame(dict)
print(data)

print("..........................................")

cutoffs = [("area",2,10),("population",1200,1300)]

print(column_cutoff(data,cutoffs))
