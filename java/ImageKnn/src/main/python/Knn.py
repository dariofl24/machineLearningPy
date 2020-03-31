import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

def getBestKlusters(X,kn):

    kmeans = KMeans(n_clusters=kn, random_state=2).fit(X)
    labels = kmeans.labels_

    centers=kmeans.cluster_centers_

    return labels,centers
#getBestKlusters

def getKlustersFromCSV(inputFile,outputFile,kluster_number):

    df = pd.read_csv(inputFile)
    print(df.head())

    usr_val_list = []
    for usr in df.index.values:
        usr_val_list.append(df.loc[usr].values)

    best_labels,best_center=getBestKlusters(usr_val_list,kluster_number)

    kluster_series = pd.Series(data = best_labels,index=df.index.values)

    print ("Labels::")
    print (best_labels)
    print ("+++++++++++++++++++++++")
    print ("kluster_series::")
    print(kluster_series)

    f= open(outputFile,"w+")

    for ii in range(best_labels.size):
        f.write(str(ii) +","+ str(best_labels[ii]) +"\n")

    f.close()

    return

#Main

getKlustersFromCSV("/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/colors.csv",
                   "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/colors_klusters.txt",
                   12)

# getKlustersFromCSV("/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/points.csv",
#                    "/Users/dflores/dariofl24/machinelearn/machineLearningPy/java/ImageKnn/results/points_klusters.txt",
#                    30)


#