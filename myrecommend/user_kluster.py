import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

me_rate = [3.5, 0.0, 3.0, 3.0, 5.0, 2.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 4.5, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 4.0, 4.5, 0.0, 3.0, 0.0, 2.0, 0.0, 0.0, 3.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 4.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 3.5, 0.0, 2.0, 2.0, 4.5, 0.0, 0.0, 4.0, 2.0, 0.0, 0.0, 0.0, 0.0, 5.0, 5.0, 4.5, 0.0, 0.0, 5.0, 0.0, 0.0, 2.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 4.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 3.0, 3.5, 2.0, 0.0, 0.0, 3.0, 0.0, 0.0, 2.0, 3.5, 0.0, 4.0, 0.0, 5.0, 0.0, 4.0, 0.0, 4.5, 2.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 5.0, 5.0, 0.0, 0.0, 3.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 4.0, 0.0, 4.0, 0.0, 4.5, 0.0, 0.0, 4.5, 4.5, 5.0, 0.0, 0.0, 0.0, 4.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 4.5, 3.5, 0.0, 0.0, 0.0, 5.0, 0.0, 2.0, 0.0, 3.0, 0.0, 0.0, 0.0, 4.5, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 4.0, 0.0, 4.5, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 2.0, 3.5, 2.0, 0.0, 0.0, 0.0, 4.5, 4.0, 0.0, 0.0, 2.0, 4.5, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 3.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0, 0.0, 5.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 3.5, 0.0, 3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 3.0, 4.5, 0.0, 0.0, 0.0, 2.0, 0.0, 3.5, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 3.5, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 3.5, 0.0, 5.0, 5.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 2.0, 3.5, 0.0, 5.0, 3.5, 0.0, 4.5, 0.0, 0.0, 2.0, 0.0, 4.0, 4.5, 0.0, 0.0, 0.0, 3.0, 3.5, 3.0, 0.0, 0.0, 0.0, 2.0, 3.0, 3.0, 3.5, 4.0, 0.0, 2.0, 0.0, 3.0, 0.0, 2.0, 3.5, 2.0, 5.0, 0.0, 0.0, 4.5, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0, 0.0, 4.0, 0.0, 3.5, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 4.0, 4.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 5.0, 3.0, 4.0, 0.0, 0.0, 0.0, 4.0, 2.0, 0.0, 3.5, 0.0, 3.5, 0.0, 0.0, 0.0, 4.0, 2.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 5.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 4.0, 4.5, 4.0, 4.0, 4.0, 0.0, 0.0, 3.0, 0.0, 4.5, 4.0, 0.0, 0.0, 0.0, 2.0, 0.0, 3.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 4.5, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 4.0, 2.0, 0.0, 3.5, 4.0, 0.0, 5.0, 3.5, 0.0, 0.0, 0.0, 0.0, 3.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 2.0, 0.0, 0.0, 4.0, 4.0, 0.0, 0.0, 0.0, 3.5, 2.0, 2.0, 4.5, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 4.5, 2.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.5, 4.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 4.0, 0.0, 0.0, 4.5, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 2.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 4.0, 0.0, 4.0, 0.0, 4.5, 4.5, 0.0, 4.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 2.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 4.0, 3.5, 4.5, 0.0, 5.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0]

# me [3.5, 0.0, 3.0, 3.0, 5.0, 2.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 4.5, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 4.0, 4.5, 0.0, 3.0, 0.0, 2.0, 0.0, 0.0, 3.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 4.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 3.5, 0.0, 2.0, 2.0, 4.5, 0.0, 0.0, 4.0, 2.0, 0.0, 0.0, 0.0, 0.0, 5.0, 5.0, 4.5, 0.0, 0.0, 5.0, 0.0, 0.0, 2.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 4.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 3.0, 3.5, 2.0, 0.0, 0.0, 3.0, 0.0, 0.0, 2.0, 3.5, 0.0, 4.0, 0.0, 5.0, 0.0, 4.0, 0.0, 4.5, 2.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 5.0, 5.0, 0.0, 0.0, 3.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 4.0, 0.0, 4.0, 0.0, 4.5, 0.0, 0.0, 4.5, 4.5, 5.0, 0.0, 0.0, 0.0, 4.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 4.5, 3.5, 0.0, 0.0, 0.0, 5.0, 0.0, 2.0, 0.0, 3.0, 0.0, 0.0, 0.0, 4.5, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 4.0, 0.0, 4.5, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 2.0, 3.5, 2.0, 0.0, 0.0, 0.0, 4.5, 4.0, 0.0, 0.0, 2.0, 4.5, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 3.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0, 0.0, 5.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 3.5, 0.0, 3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 3.0, 4.5, 0.0, 0.0, 0.0, 2.0, 0.0, 3.5, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 3.5, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 3.5, 0.0, 5.0, 5.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 2.0, 3.5, 0.0, 5.0, 3.5, 0.0, 4.5, 0.0, 0.0, 2.0, 0.0, 4.0, 4.5, 0.0, 0.0, 0.0, 3.0, 3.5, 3.0, 0.0, 0.0, 0.0, 2.0, 3.0, 3.0, 3.5, 4.0, 0.0, 2.0, 0.0, 3.0, 0.0, 2.0, 3.5, 2.0, 5.0, 0.0, 0.0, 4.5, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0, 0.0, 4.0, 0.0, 3.5, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 4.0, 4.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 5.0, 3.0, 4.0, 0.0, 0.0, 0.0, 4.0, 2.0, 0.0, 3.5, 0.0, 3.5, 0.0, 0.0, 0.0, 4.0, 2.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 5.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 4.0, 4.5, 4.0, 4.0, 4.0, 0.0, 0.0, 3.0, 0.0, 4.5, 4.0, 0.0, 0.0, 0.0, 2.0, 0.0, 3.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 4.5, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 4.0, 2.0, 0.0, 3.5, 4.0, 0.0, 5.0, 3.5, 0.0, 0.0, 0.0, 0.0, 3.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 2.0, 0.0, 0.0, 4.0, 4.0, 0.0, 0.0, 0.0, 3.5, 2.0, 2.0, 4.5, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 4.5, 2.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.5, 4.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 4.0, 0.0, 0.0, 4.5, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 2.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 4.0, 0.0, 4.0, 0.0, 4.5, 4.5, 0.0, 4.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 2.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 4.0, 3.5, 4.5, 0.0, 5.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0]

def distEclud(vecA, vecB):

    return (np.sum((vecA - vecB)**2.0))**0.5
#distEclud

def getBestKlusters(X,kn):

    rand_states = [13,77,44,9,119,129,512,256,300]

    best_labels = None
    best_center = None

    best_sum = 0.

    for state in range(55):

        kmeans = KMeans(n_clusters=kn, random_state=state).fit(X)
        labels = kmeans.labels_

        centers=kmeans.cluster_centers_

        dist_sum = 0.

        for idx in range(labels.shape[0]-1):
            cent = centers[ labels[idx] ]
            point = X[idx]
            dist_sum += distEclud(cent,point)

        if ( (-1./dist_sum) <=  best_sum):
            best_labels = labels
            best_center = centers

    return best_labels,best_center
#getBestKlusters

def rank_sub_df(sub_df):

    series_avg = []
    series_mov = []

    for idx in sub_df.columns.values:

        column = sub_df.loc[:,idx]

        if(np.sum(column.values) > 0 ):

            if( len(column[column != 0].values) >= float(len(column.index.values))/3.0  ):

                mov_avg = np.average(column[column != 0].values)

                series_mov.append(idx)
                series_avg.append(mov_avg)

    ranks= pd.Series(data= series_avg,index=series_mov).sort_values(ascending = False) # [:25]
    print(ranks)

    return 0

#Main
df = pd.read_csv("../java/testproj/reviewsTable_0_30.csv").set_index('custid').fillna(0.)
#print(df.head())

df2 = pd.DataFrame([me_rate], columns=df.columns.values,index=[0])

df = df.append(df2)

usr_val_list = []

for usr in df.index.values:
    usr_val_list.append(df.loc[usr].values)
    #print('---')

kluster_number = 55

best_labels,best_center=getBestKlusters(usr_val_list,kluster_number)

kluster_series = pd.Series(data = best_labels,index=df.index.values)

me_kluster = kluster_series.loc[0]
print('Cluster for user: ' + str(me_kluster) )

not_rated = df2.columns[df2.loc[0] == 0.]
print(not_rated)

for kn in range(kluster_number):
    sub_clust_series = kluster_series[ kluster_series == kn ]

    if(len(sub_clust_series.index.values) >2 and kn == me_kluster ):
        print("----------------------------------------------------")
        print('Kl :: '+str(kn))
        print("# Of Users")
        print(len(sub_clust_series.index.values))

        sub_df = df.loc[sub_clust_series.index.values]
        sub_df = sub_df[not_rated]

        rank_sub_df(sub_df)









#