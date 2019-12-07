import numpy as np

from itertools import product
from ..utils import dataset, distances


class DB(dataset.DataSet):
    def __init__(self, X, y):
        super().__init__(X, y)
        self.unique_labels = sorted(np.unique(self.labels))
        self.K = len(self.unique_labels)
        self.kmu, self.ksigma = self.compute_kmu_ksigma()
        self.db = None
        self.fit()

    def fit(self):
        S = [
            distances.mean_mahalanobis(self.X[self.labels == k],
                                       self.kmu[k],
                                       self.ksigma[k])
            for k in self.unique_labels
        ]

        M = np.zeros((self.K, self.K))
        for i, j in product(range(self.K), range(self.K)):
            M[i, j] = (i != j) and distances.mean_mahalanobis(self.kmu[j], self.kmu[i], self.ksigma[i])

        R = np.zeros((self.K, self.K))
        for i, j in product(range(self.K), range(self.K)):
            R[i, j] = (i != j) and (S[i] + S[j]) / M[i, j]

        self.db = (1/self.K) * R.max(axis=1, initial=0).sum()

    def compute_kmu_ksigma(self):
        mu = [np.mean(self.X[self.labels == k], axis=0) for k in self.unique_labels]
        sigma = [np.cov(self.X[self.labels == k], rowvar=False) for k in self.unique_labels]

        return mu, sigma
