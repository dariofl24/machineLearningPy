import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


#Main
df = pd.read_csv("../java/testproj/reviewsTable_0_30.csv").set_index('custid').fillna(0.)
print(df.head())

rates = []

all_n = str(len(df.columns.values))
count = 0

for pic in df.columns.values:

    count+=1

    print(str(count)+'/'+all_n)

    print(pic)
    cal = input(": ")
    print(cal)

    if cal != 'exit':

        if cal != '':
            rates.append(float(cal))
        else:
            rates.append(0.)

    else:
        break

print(rates)



#
