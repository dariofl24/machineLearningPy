from scipy.stats import multivariate_normal
import scipy.stats as stats
import numpy as np
import pandas as pd


def euclid_dist(p1, p2):

    dist = 0

    for x in range( len(p1) ):
        diff=p1[x] - p2[x]
        dist += (diff ** 2)

    return dist ** .5

def euclid_dist_sqrt(p1, p2):

    dist = 0

    for x in range( len(p1) ):
        diff=p1[x] - p2[x]
        dist += (diff ** 2)

    return float(dist)

def assign_clusters_k_means(points, clusters):
    """
    Determine the nearest cluster to each point, returning an array indicating the closest cluster

    Positional Arguments:
        points: a 2-d numpy array where each row is a different point, and each
            column indicates the location of that point in that dimension
        clusters: a 2-d numpy array where each row is a different centroid cluster;
            each column indicates the location of that centroid in that dimension

    Example:
        points = np.array([[0,1], [2,2], [5,4], [3,6], [4,2]])
        clusters = np.array([[0,1],[5,4]])
        cluster_weights = assign_clusters_k_means(points, clusters)

        print(cluster_weights) #--> np.array([[1, 0],
                                              [1, 0],
                                              [0, 1],
                                              [0, 1],
                                              [0, 1]])
    """

    weights = []

    for xx in range(points.shape[0]):

        min_dist = 0
        min_dist_index= -1

        for yy in range(clusters.shape[0]):
            dist = euclid_dist(points[xx],clusters[yy])
            print(dist)

            if ( dist <  min_dist or min_dist_index < 0):
                min_dist = dist
                min_dist_index = yy

        zro = np.zeros( (clusters.shape[0],) , dtype=int)
        zro[min_dist_index] = 1
        print(zro)

        weights.append(zro)


    cluster_weights = np.array(weights)
    return cluster_weights


def assign_clusters_soft_k_means(points, clusters, beta):

    """
    Return an array indicating the porportion of the point
        belonging to each cluster

    Positional Arguments:
        points: a 2-d numpy array where each row is a different point, and each
            column indicates the location of that point in that dimension
        clusters: a 2-d numpy array where each row is a different centroid cluster;
            each column indicates the location of that centroid in that dimension
        beta: a number indicating what distance can be considered "close"

    Example:
        points = np.array([[0,1], [2,2], [5,4], [3,6], [4,2]])
        clusters = np.array([[0,1],[5,4]])
        beta = 1
        cluster_weights = assign_clusters_soft_k_means(points, clusters, beta)

        print(cluster_weights) #--> np.array([[0.99707331, 0.00292669],
                                              [0.79729666, 0.20270334],
                                              [0.00292669, 0.99707331],
                                              [0.04731194, 0.95268806],
                                              [0.1315826 , 0.8684174 ]])
    """

    result_weights = []

    for xx in range(points.shape[0]):

        point = points[xx]

        j_sum = 0.

        res_partial = []

        for yy in range(clusters.shape[0]):

            kluster = clusters[yy]

            part = np.exp( (-1.0/float(beta)) * euclid_dist(point , kluster))
            res_partial.append(part)
            j_sum += part

        for ii in range( len(res_partial) ):
            res_partial[ii] = res_partial[ii]/j_sum

        result_weights.append(res_partial)


    cluster_weights = np.array(result_weights)

    return cluster_weights



def update_clusters_k_means(points, cluster_weights):

    """
    Update the cluster centroids via the k-means algorithm

    Positional Arguments --
        points: a 2-d numpy array where each row is a different point, and each
            column indicates the location of that point in that dimension
        cluster_weights: a 2-d numy array where each row corresponds to each row in "points"
            and the columns indicate which cluster the point "belongs" to - a "1" in the kth
            column indicates belonging to the kth cluster

    Example:

        points = np.array([[0,1], [2,2], [5,4], [3,6], [4,2]])
        cluster_weights = np.array([[1, 0],[1, 0],[0, 1],[0, 1],[0, 1]])

        new_cents = update_clusters_k_means(points, cluster_weights)

        print(new_cents) #--> np.array([[1. , 1.5],
                                        [4. , 4. ]])

    """
    new_clusts = np.array([])


    return new_clusts












#points = np.array([[0,1], [2,2], [5,4], [3,6], [4,2]])
#clusters = np.array([[0,1],[5,4]])
#beta = 1
#cluster_weights = assign_clusters_soft_k_means(points, clusters, beta)

#print(cluster_weights) #--> np.array([[0.99707331, 0.00292669],
                                      # [0.79729666, 0.20270334],
                                      # [0.00292669, 0.99707331],
                                      # [0.04731194, 0.95268806],
                                      # [0.1315826 , 0.8684174 ]])











#points = np.array([[0,1], [2,2], [5,4], [3,6], [4,2]])
#clusters = np.array([[0,1],[5,4]])
#cluster_weights = assign_clusters_k_means(points, clusters)

#print(cluster_weights) #--> np.array([[1, 0],
                                      #[1, 0],
                                      #[0, 1],
                                      #[0, 1],
                                      #[0, 1]])









#
