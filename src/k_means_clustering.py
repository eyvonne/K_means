import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt

class KMeansClustering():
    '''this implimentation is going to find the distances between 
    each point and every other point, then get the average distance, and use the minimums
    to cluster. As I'm writing this I'm realizing that this will just get the main center
    not all the centers. I am however curious to see what this produces.'''
    
    def __init__(self, k_means):
        self.k = k_means # the number of clusters to build
        self.data = None # will hold the raw data 
        self.distances = [] # will hold the distance matrix

    def fit(self, X):
        self.data = X.copy()
        self.distances, self.means = self.get_distances(X)
        self.centers_index = np.argsort(self.means, axis=0)
        self.search()
        
    def search(self):
        searching = True
        for i in range(50):
            centers = self.centers_index[:self.k]
            self.centers = self.data[centers]
            self.plot()
            self.data[centers] # the points that we need to get distances for
            dists, _ = self.get_distances(self.data[centers])
            sums = dists.sum(0)
            worst = sums.argmin()
            centers[worst] # index of the point to be eliminated
            self.centers_index = self.centers_index[self.centers_index != centers[worst]]
            
        
    def get_distances(self, X):
        '''this little helper function builds out the 
        distances matrix'''
        distances = []
        for x in X:
            y = spatial.distance_matrix(X, x.reshape(1,2))
            distances.append(np.squeeze(y))
        distances = np.array(distances)
        return distances, distances.mean(0)
    
    def plot(self):
        x, y = self.data.T
        cx, cy = self.centers.T
        plt.scatter(x, y)
        plt.scatter(cx, cy, c='red')
        plt.show()