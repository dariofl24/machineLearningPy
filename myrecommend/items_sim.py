import numpy as np
import pandas as pd



df = pd.read_csv("../java/testproj/reviewsTable_0_30.csv").set_index('custid') # .iloc[0:4,:]
print(df.head())

users = df.index

for user in users:

    dict_rate ={0.5:0.,1.:0.,1.5:0.,2.:0.,2.5:0.,3.:0.,3.5:0.,4.:0.,4.5:0.,5:0.}

    user_ratings = df.loc[user][df.loc[user].fillna(0) != 0]

    for val in user_ratings.values:
        dict_rate[val] += (1./float( len(user_ratings.values) ))*100.

    print(dict_rate)
    print(np.sum(user_ratings.values)/float( len(user_ratings.values) ))



#
