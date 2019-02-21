import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


def distEclud(vecA, vecB):

    return (np.sum((vecA - vecB)**2.0))**0.5
#distEclud

def getBestKlusters(X,kn):

    rand_states = [4,8,64,256,0,1,2,10,3,12,24]

    best_labels = None
    best_center = None

    best_sum = 0.

    for state in rand_states:

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

            if( len(column[column != 0].values) >= float(len(column.index.values))/9.  ):

                mov_avg = np.average(column[column != 0].values)

                series_mov.append(idx)
                series_avg.append(mov_avg)

                #print(idx)
                #print( mov_avg )
                #print('-')

    ranks= pd.Series(data= series_avg,index=series_mov).sort_values(ascending = False)[:15]
    print(ranks)

    return 0

#Main
df = pd.read_csv("../java/testproj/reviewsTable_0_30.csv").set_index('custid').fillna(0.)
#print(df.head())

usr_val_list = []

for usr in df.index.values:
    usr_val_list.append(df.loc[usr].values)
    #print('---')

kluster_number = 60

best_labels,best_center=getBestKlusters(usr_val_list,kluster_number)

#print(best_labels)
#print(best_center)

kluster_series = pd.Series(data = best_labels,index=df.index.values)

for kn in range(kluster_number):
    sub_clust_series = kluster_series[ kluster_series == kn ]

    if(len(sub_clust_series.index.values) >2):
        print("----------------------------------------------------")
        print(kn)
        print("# Of Users")
        print(len(sub_clust_series.index.values))
        sub_df = df.loc[sub_clust_series.index.values]
        #print(sub_df)

        rank_sub_df(sub_df)









#
