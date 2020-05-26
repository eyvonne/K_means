import numpy as np
import scipy
from scipy import spatial


class KNearestNeighbors():
    ''' This meets MVP but took me all of two seconds to build. I'm going to work on 
    k-means clustering now because it'll be moderately more challenging then come back
    and specialize this k-neighbors for quake '''

    def __init__(self, neighbors):
        self.neighbors = neighbors

    def fit(self, data):
        self.data = data

    def predict(self, y):
        dist = spatial.distance_matrix(self.data, y)
        kmin_index = np.argsort(dist, axis=0)
        return self.data[kmin_index[:self.neighbors]], dist[kmin_index[:self.neighbors]]
