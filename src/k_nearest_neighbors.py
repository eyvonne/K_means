import numpy as np
import scipy
from scipy import spatial

class KNearestNeighbors():
    def __init__(self, neighbors):
        self.neighbors = neighbors

    def fit(self, data):
        self.data = data

    def predict(self, y):
        dist = spatial.distance_matrix(self.data, y)
        kmin_index = np.argsort(dist, axis=0)
        return self.data[kmin_index[:self.neighbors]], dist[kmin_index[:self.neighbors]]


if __name__ == '__main__':
    arr = [2, 4, 5, 6, 3, 7, 8, 9, 1, 0, 23, 43, 32, 23, 12, 21, 56, 76, 87, 54, 34, 78, 67, 65]
    neigh = KNearestNeighbors(2)
    neigh.fit(arr)
    print(neigh.predict(60))
