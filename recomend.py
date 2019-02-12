import numpy as np
import pandas as pd
import datetime


def e_sim(ser1, ser2):
    """
    Given two Pandas series, compute the euclidean similarity score;
        1 / 1+euclidean distance

    Positional Arguments --
        ser1: a Pandas Series of length n
        ser2: a Pandas Series of length n

    Example --
        ser1 = ex_hand.iloc[:,0]
        ser2 = ex_hand.iloc[:,1]
        print(e_sim(ser1, ser2)) #--> 0.28989794855663564
    """

    diff = ser1 - ser2
    print(diff)

    sqrtt= diff ** 2.

    print(sqrtt)
    print(sqrtt.sum())

    distt = sqrtt.sum() ** .5

    return 1. / (1. + distt)


def drop_val (df, to_drop):

    """
    Drop rows from the DataFrame containing the specified values

    Positional Arguments --
        df: a Pandas DataFrame
        to_drop: a value found in some rows of df

    Example --

        df = ex.loc[:,"Mozart":"Bach"]
        to_drop = 5
        print(drop_val(df,to_drop)) # -->          Mozart  Bach
                                            Abel        0     1
                                            Erik        3     3
                                            Frank       2     2


    """

    for col in df.columns:
        df = df[ df[col] !=  to_drop]

    return df




dd = {'col1': [2,2,5], 'col2': [1,3,3], 'col3': [3,3,2]}
ex_hand = pd.DataFrame(data=dd)

df = ex_hand.loc[:,"col1":"col2"]

print(df)

to_drop = 1

print(drop_val(df,to_drop)) # -->          Mozart  Bach
                                    #Abel        0     1
                                    #Erik        3     3
                                    #Frank       2     2




















#dd = {'col1': [2,2,5], 'col2': [1,3,3], 'col3': [3,3,2]}
#ex_hand = pd.DataFrame(data=dd)

#ser1 = ex_hand.iloc[:,0]
#print(ser1)
#ser2 = ex_hand.iloc[:,1]
#print(ser2)

#print(e_sim(ser1, ser2)) #--> 0.28989794855663564














#
