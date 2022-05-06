import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# points
p = np.array([[0.1,0.6], [0.15,0.71], [0.08,0.8], [0.16,0.85], [0.2,0.3], [0.25,0.5], [0.24, 0.1], [0.3,0.2]])

# centroids
centroids = np.array([[0.1,0.6], [0.3,0.2]])

KMClustering = KMeans(n_clusters = 2, init = centroids, n_init = 1 )
KMClustering.fit(p)

print("Labels : ",  KMClustering.labels_)

# a.)find p6 
print("P6 in cluster : ", KMClustering.labels_[5])

# b.)population around cluster 2
print("population of cluster around cluster 2(m2) : ", np.count_nonzero(KMClustering.labels_ == 1))

# c.)updated value of centroids
print("updated centroids (m1 and m2): ", KMClustering.cluster_centers_)

#plt.plot(p, "o")
#plt.show()

# Plot the data
plt.scatter(p[:,0],p[:,1])
# Plot the clusters 
plt.scatter(KMClustering.cluster_centers_[:, 0], KMClustering.cluster_centers_[:, 1], 
            s=200,                             # Set centroid size
            c='red')                           # Set centroid color
plt.show()
