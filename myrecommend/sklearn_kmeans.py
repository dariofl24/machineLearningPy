from sklearn.cluster import KMeans
import numpy as np

def distEclud(vecA, vecB):

    return (np.sum((vecA - vecB)**2.0))**0.5

def getBestKlusters(X):

    rand_states = [4,8,16,32,64,256,1,10]

    best_labels = None
    best_center = None

    best_sum = 0.

    for state in rand_states:

        kmeans = KMeans(n_clusters=2, random_state=state).fit(X)
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


X = np.array([[1, 2], [1, 4], [1, 0],[4, 2], [4, 4], [4, 0]])


best_l,best_c = getBestKlusters(X)

print('BEST')
print(best_l)
print(best_c)








#
