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

    
class QuakeNearestNeighbors():
    def __init__(self, neighbors):
        self.neighbors = neighbors

    def fit(self, data):
        self.data = data
        self.matching = data[['lat', 'lon', 'mag']].values

    def predict(self, y):
        match = y[['lat','lon','mag']].values
        dist = spatial.distance_matrix(self.matching, [match])
        kmin_index = np.argsort(dist, axis=0)
        return kmin_index[:self.neighbors], dist[kmin_index[:self.neighbors]]
    
    def pair_quakes(self, df):
        '''this is a reusable function after fit has been run. It takes in 
        a dataframe and then returns a list of tuples with ID's of matching 
        quakes''' 
        preds = []
        for i, row in df.iterrows():
            neighbor_index, dist = near.predict(row)
            pred = emsc_df.iloc[neighbor_index.squeeze()]
            if dist < 1:
                preds.append((pred['id'], row['id']))
        return preds