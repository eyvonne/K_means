import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt


class KMeansClustering():
    '''this implimentation is going to find the distances between
    each point and every other point, then get the average distance, and use the minimums
    to cluster. As I'm writing this I'm realizing that this will just get the main center
    not all the centers. I am however curious to see what this produces.'''

    def __init__(self, k_means):
        self.k = k_means  # the number of clusters to build
        self.data = None  # will hold the raw data
        self.distances = []  # will hold the distance matrix

    def fit(self, X):
        self.data = X.copy()
        c_ids = np.random.randint(self.data.shape[0], size=self.k)
        self.centers = self.data[c_ids]
        previous = np.random.rand(self.k, 2)

        while np.all(previous != self.centers):
            # set previous to know when to stop
            previous = self.centers.copy()
            # get distances from the centers
            distances = spatial.distance_matrix(self.data, self.centers)
            # assign all observations to a center
            self.assignments = np.argmin(distances, axis=1)
            # calulate means based on clusters
            for i in range(self.k):
                _, means = self.get_distances(self.data[self.assignments == i])
                # update the center with the new mean
                self.centers[i] = self.data[self.assignments == i][np.argmin(means)]

    def predict(self, y):
        if type(self.data) == None:
            raise AttributeError('Please Call Fit before Predict')
        dists = spatial.distance_matrix(self.centers, y)
        cent = np.argmin(dists)
        return cent

    def get_distances(self, X):
        '''this little helper function builds out the
        distances matrix'''
        distances = []
        for x in X:
            y = spatial.distance_matrix(X, x.reshape(1, 2))
            distances.append(np.squeeze(y))
        distances = np.array(distances)
        return distances, distances.mean(0)

    def plot(self):
        x, y = self.data.T
        cx, cy = self.centers.T
        plt.scatter(x, y, c=self.assignments)
        plt.scatter(cx, cy, c='red')
        plt.savefig('graph.png')


if __name__ == '__main__':
    X = np.random.rand(500, 2)*100
    y = np.random.rand(1, 2) * 100
    clusters = KMeansClustering(4)
    clusters.fit(X)
    print(clusters.predict(y))
    clusters.plot()
