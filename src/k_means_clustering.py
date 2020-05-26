import numpy as np
from scipy import spatial


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
        centers = np.array()
        if type(X) != np.array():
            raise Exception(TypeError)
        else:
            self.data = X
            means = self.get_distances(X)
            centers_index = np.argsort(means, axis=0)
            return self.data[centers_index[:self.k]]
        
    
    def get_distances(self)
    '''this little helper function builds out the 
    distances matrix of all the '''
        for x in self.data:
            y = spatial.distance_matrix(self.data, x.reshape(1,2))
            self.distances.append(np.squeeze(y))
        self.distances = np.array(self.distances)
        return self.distances.mean(0)