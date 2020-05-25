import numpy as np
import scipy


class KNearestNeighbors():
    def __init__(self, neighbors):
        self.neighbors = neighbors

    def fit(self, data):
        self.data = data

    def predict(self, X):
        '''This is a rough and ugly implimentation. There is no optimiztion here yet
        its just a check to see if I can get it to work in the super base case'''
        matches = [-1] * self.neighbors
        buffer = []
        for i in range(len(matches)):
            dist = -1
            val = None
            for d in self.data:
                if dist == -1 or np.abs(X - d) < dist:
                    dist = np.abs(X - d)
                    val = d
                    buffer.append(d)
                    self.data.remove(d)
            matches[i] = val
        for b in buffer:
            self.data.append(b)
        return matches


if __name__ == '__main__':
    arr = [2, 4, 5, 6, 3, 7, 8, 9, 1, 0, 23, 43, 32, 23, 12, 21, 56, 76, 87, 54, 34, 78, 67, 65]
    neigh = KNearestNeighbors(2)
    neigh.fit(arr)
    print(neigh.predict(60))
