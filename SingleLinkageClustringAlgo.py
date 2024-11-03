import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist,squareform
from scipy.cluster.hierarchy import linkage,dendrogram
import matplotlib.pyplot as plt

points = np.array([18,22,25,27,42,43])
full_distances = np.abs(points[:,None]-points)
condensed_distance = squareform(full_distances)
labels = ['18','22','25','27','42','43']

def print_matrix(matrix,step,labels):
    df = pd.DataFrame(matrix,columns=labels,index=labels)
    print(f"Distance Matrix at step {step} :\n ",df)
def single_linkage_clustering(dist_matrix):
    global labels
    step =1
    n =6
    current_matrix = dist_matrix.copy()
    while n > 1 :
        min_dist = np.inf
        for i in range(len(current_matrix)):
            for j in range(i+1,len(current_matrix)):
                if current_matrix[i,j] < min_dist:
                    min_dist = current_matrix[i,j]
                    cluster_a,cluster_b = i,j

        print_matrix(current_matrix,step,labels)
        new_cluster = np.minimum(current_matrix[cluster_a],current_matrix[cluster_b])
        indices = [x for x in range(len(current_matrix)) if x != cluster_a and x !=cluster_b]

        new_matrix = np.zeros((n-1,n-1))
        new_matrix[:-1,:-1] = current_matrix[np.ix_(indices,indices)]
        new_matrix[-1,:-1] = new_matrix[:-1,-1] = new_cluster[indices]

        current_matrix = new_matrix

        new_label = f"({labels[cluster_a]},{labels[cluster_b]})"
        labels = [labels[i] for i in indices] + [new_label]

        n -=1
        step +=1              
    print_matrix(current_matrix,step,labels)
        
single_linkage_clustering(full_distances)        

z = linkage(condensed_distance,method='single')

dendrogram(z,labels = ['18','22','25','27','42','43'])
plt.title('Single Linkage Dendrogram')
plt.xlabel('Cluster')
plt.ylabel('Distance')
plt.show()