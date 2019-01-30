import numpy as np
import pandas as pd



def hidden(hp):
    if (hp<=0) or (hp >= 50):
        print("input out of bounds")

    nums = np.logspace(0,5,num = 1000)
    vals = nums ** 43.123985172351235134687934

    user_vals = nums ** hp

    return vals-user_vals

def minimize( passed_func):
    """
    Find the numeric value that minimizes the output of 'passed_func'

    Positional Argument:
        passed_func -- a function that takes a single number (between 0 and 50 exclusive)
            as input, and returns a list of 1000 floats.

    Example:
        passed_func = hidden
        min_hidden = minimize(passed_func)
        print(round(min_hidden,4))
        #--> 43.1204 (answers will vary, must be close to 43.123985172351)

    """
    count=0
    i = 0.01
    min_i = i

    min_val = abs(np.mean(passed_func(i)))

    while i < 50.0 :

        val = abs(np.mean(passed_func(i)))
        count += 1

        if val < min_val:
            min_val=val
            min_i = i

        i += 0.1

    aa = min_i-0.05
    bb = min_i+0.05
    print((aa,bb))
    ii = aa

    while ii < bb :

        val = abs(np.mean(passed_func(ii)))
        count += 1

        if val < min_val:
            min_val=val
            min_i = ii

        ii += 0.001

    aa = min_i-0.00005
    bb = min_i+0.00005
    ii = aa

    while ii < bb :

        val = abs(np.mean(passed_func(ii)))
        count += 1

        if val < min_val:
            min_val=val
            min_i = ii

        ii += 0.000001

    print(count)

    return float(min_i)



print(minimize(hidden))











#
