#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#creating cluster
def create_cluster(X, centroid_pts):
    cluster = {}
  # Calculating euclidean distance between current centrid and points for each cluster
  # Compare distance value for each point to their cluster centriod and taking the minimum value 
    for x in X:
        value = min([(i[0],np.linalg.norm(x - centroid_pts[i[0]]))for i in enumerate(centroid_pts)], key=lambda s:s[1])[0]
        #if get a valid value append in the cluster with key
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster

#Calculating new cluster centroids
def calculate_new_center(cluster):
    #Sorting the custer based on keys
    keys =sorted(cluster.keys())
    #Calculate new cluster centroids 
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    return newmu
#Comparing old and new centroids point
def matched(new_centroids, old_centroids):
    return (set([tuple(a)for a in new_centroids]) == set([tuple(a)for a in old_centroids]))
#Applyinh k-means technique
def Apply_Kmeans(X, K, N):
    # selecting random centroids from dataset and by number of clusters.
    old_centroids = np.random.randint(N, size = K)
    old_centroid_pts = np.array([X[i]for i in old_centroids])
    #Printing current centroids
    print("old :",old_centroids)
    print(old_centroid_pts)

    cluster_info = create_cluster(X, old_centroid_pts)
    #Printing current cluster
    print("Initial cluster information:")
    print(cluster_info)
    #Calculate new cluster centroids using function
    new_centroid_pts=calculate_new_center(cluster_info)
    print("new :", new_centroid_pts)
    itr = 0
    print("Graph after selecting initial clusters with initial centroids:")
    #Plotting old cluster according to old cluster centroids
    plot_cluster(old_centroid_pts,cluster_info,itr)
    #Continue the iteration unless old and new centroids match, if don't match calculate new cluster centroids
    while not matched(new_centroid_pts, old_centroid_pts):
        itr = itr + 1
        old_centroid_pts = new_centroid_pts
        cluster_info = create_cluster(X,new_centroid_pts)
        plot_cluster(new_centroid_pts, cluster_info,itr)
        new_centroid_pts = calculate_new_center(cluster_info)

    print("Results after final iteration:")
    plot_cluster(new_centroid_pts, cluster_info, itr)
    return

#Plot the present cluster with iteration number
def plot_cluster(mu,cluster, itr):
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()

#Declaring Variables
def Simulate_Clusters():
    print(".........Starting Cluster Simulation.........")
    N = 6 #number of points
    K = 2 #number of clusters
    
    data = pd.read_csv('ICP5_2.csv')
    print(data.shape)
    data.head()
    #Taking the values from the file
    p1 = data['X'].values
    p2 = data['Y'].values

    print (p1)
    print (p2)
    #Create a Array of the points
    X = np.array(list(zip(p1,p2)))
    print (X)
    #Plotting the points
    plt.scatter(p1,p2,c='black',s=7)
    plt.show()
    #Calling the K-means function to apply the K-mean theory
    temp = Apply_Kmeans(X, K, N)

if __name__ == '__main__':
    Simulate_Clusters()

