import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


def distEclud(vecA, vecB):

    return (np.sum((vecA - vecB)**2.0))**0.5
#distEclud

def findSimilar_single(dff,baseIdx,limit=5):

    base_mov = dff.loc[baseIdx]

    nn_index = []
    nn_dist = []

    for idx in dff.index.values:

        if(idx != baseIdx):
            nn_index.append(idx)
            dist = distEclud(dff.loc[idx],base_mov)
            nn_dist.append( 1./(1.+dist) )

    return pd.Series(data=nn_dist,index= nn_index).sort_values(ascending = False)
#findSimilar_single

def getBestKlusters(X,kn):

    rand_states = [4,8,64,256,0,1,2,10]

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

# MAIN
df = pd.read_csv("../java/testproj/reviewsTable_0_30.csv").set_index('custid')

#print(df.head())

rate_pos_map =	{
  0.5: 0,
  1.0: 1,
  1.5: 2,
  2.0: 3,
  2.5: 4,
  3.0: 5,
  3.5: 6,
  4.0: 7,
  4.5: 8,
  5.0: 9
}

dim_vec_list = []

for col in df.columns:
    dim_vec = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]

    val_counts = df[col].value_counts().sort_index()
    summ = np.sum (val_counts.values)
    mov_vec = (val_counts/float(summ))*100.

    for idx in mov_vec.index.values:
        dim_vec[rate_pos_map[idx]] = mov_vec[idx]

    dim_vec_list.append(dim_vec)

df2 = pd.DataFrame(data=dim_vec_list,
columns=[0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0],
index=df.columns.values)

#print(df2.head)

#movie_usr ='Toy Story 3 (2010)'
#similar = findSimilar_single(df2,movie_usr)

kluster_number = 52

best_labels,best_center=getBestKlusters(dim_vec_list,kluster_number)

#print(best_labels)
#print(best_center)

labels_series = pd.Series(data=best_labels,index=df.columns.values)

for kidx in range(kluster_number):
    print("---")
    print(np.sum( (best_center[kidx]/100.) * np.array([.5,1.,1.5,2.,2.5,3.,3.5,4.,4.5,5.])))
    print(best_center[kidx])
    print(labels_series[labels_series == kidx])











#
