import pandas as pd
import sys
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter

# method to read the data and cluster it into the different routes
def process_data(file):
    data = pd.read_csv(file)
    # data.plot.scatter(x='Distance', y='Duration')
    # plt.show()

    # scale the duration from minutes to seconds
    # this makes a closer scale to the distance in meters
    data['Duration'] = 60 * data['Duration']
    X = data.to_numpy()

    """
        Assumptions: the number of clusters equal number of known routes. 
        used the default n_init = 10, which wll run the kmeans clusterer 10 times.
        k-means implementation using scikit-learn should stop early
        if it converges before the maximum iteration (max_iter) is reached.
        Used the default max_iter value
    """
    clusterer = KMeans(n_clusters=3)
    # predict cluster each value in X belongs to
    y = clusterer.fit_predict(X)
    # plot a visual of the clusters
    plot_route_data(clusterer, X, y)
    print("\n The number of times each route is ran is: ", Counter(clusterer.labels_))

# method to view the different clusters and centroid points
def plot_route_data(clusterer, X, y_km):
    # plot the 3 clusters
    plt.scatter(
        X[y_km == 0, 0], X[y_km == 0, 1],
        s=50, c='lightgreen',
        marker='s', edgecolor='black',
        label='cluster 1'
    )

    plt.scatter(
        X[y_km == 1, 0], X[y_km == 1, 1],
        s=50, c='orange',
        marker='o', edgecolor='black',
        label='cluster 2'
    )

    plt.scatter(
        X[y_km == 2, 0], X[y_km == 2, 1],
        s=50, c='lightblue',
        marker='v', edgecolor='black',
        label='cluster 3'
    )

    # plot the centroids
    plt.scatter(
        clusterer.cluster_centers_[:, 0], clusterer.cluster_centers_[:, 1],
        s=250, marker='*',
        c='red', edgecolor='black',
        label='centroids'
    )
    plt.legend(scatterpoints=1)
    plt.xlabel('Duration (seconds)')
    plt.ylabel('Distance (meters)')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    try:
        file = sys.argv[1]
        process_data(file)
    except IndexError:
        print('Usage: %s DATA_FILE' % sys.argv[0])