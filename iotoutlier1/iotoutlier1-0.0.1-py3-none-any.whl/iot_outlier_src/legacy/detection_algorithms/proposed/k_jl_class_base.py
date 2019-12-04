""" Kernel JL

"""

# Authors: kun.bj@outlook.com
#
# License: xxx


import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_kernels
from sklearn.utils import shuffle, check_random_state

from legacy.detection_algorithms import BaseClass


def sampling_from_data(X, n_samples=10, sampling_method='random', random_state=42):
    if sampling_method == 'random':
        X_sampled = shuffle(X, n_samples=n_samples, random_state=random_state)

    return X_sampled


class K_JL_Class_Base(BaseClass):
    # def __init__(self,n_clusters=2, kernel='linear', max_iter=100, random_state= 42, verbose=True):
    def __init__(self, n_clusters=3, max_iter=50, tol=1e-3, random_state=None,
                 kernel="linear", gamma=None, degree=3, coef0=1,
                 kernel_params=None, verbose=0):
        super(K_JL_Class_Base, self).__init__()
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
        self.random_state = random_state
        self.kernel = kernel
        self.gamma = gamma
        self.degree = degree
        self.coef0 = coef0
        self.kernel_params = kernel_params
        self.verbose = verbose

    @property
    def _pairwise(self):
        return self.kernel == "precomputed"

    def _get_kernel(self, X, Y=None):
        if callable(self.kernel):
            params = self.kernel_params or {}
        else:
            params = {"gamma": self.gamma,
                      "degree": self.degree,
                      "coef0": self.coef0}
        return pairwise_kernels(X, Y, metric=self.kernel,
                                filter_params=True, **params)

    def _get_guassian_matrix(self, shape=(10, 2)):
        """
            refer to: Scalable Kernel K-Means Clustering with Nystr¨om Approximation: Relative-Error Bounds
        :param shape: (rows, cols)
        :return:

        https://scikit-learn.org/stable/modules/random_projection.html
        The sklearn.random_projection.GaussianRandomProjection reduces the dimensionality by projecting
        the original input space on a randomly generated matrix where components are drawn from the
        following distribution.

        """

        rows, cols = shape
        # for i in range(rows):
        #     for j in range(cols):
        #         mu =0
        #         sigma = 1
        #         num = 1
        #         np.random.normal(mu, sigma,1)
        mu = 0
        sigma = 1
        Z = np.random.normal(mu, sigma, size=rows * cols)

        return np.reshape(Z, shape=(rows, cols)) / np.sqrt(cols)

    def fit(self, X, y=None, sample_weight=None):
        X_train = X
        N = X_train.shape[0]
        self.n = max(200, int(N / 1))  # n = max(200, N/100). N is the total samples
        self.d = 10 * self.n_clusters  # d = 10k, k is the number of clusters.
        print(f'n: {self.n}, d: {self.d}')

        X_sampled = sampling_from_data(X_train, n_samples=self.n, sampling_method='random',
                                       random_state=self.random_state)
        # X_sampled = X_train[:self.n, :]
        self.K = self._get_kernel(X_sampled, X_sampled)  # K is the nxn gram matrix

        ###  n_components : int,Dimensionality of the target projection space., x ~ N(0, 1/ np.sqrt(d))
        ### n_features : int, Dimensionality of the original source space.
        # Z= gaussian_random_matrix(n_components= self.d, n_features=self.n, random_state=self.random_state)
        rng = check_random_state(random_state)
        n_components = self.d
        n_features = self.n
        Z = rng.normal(loc=0.0,
                       scale=1.0,
                       size=(n_components, n_features))
        print(f'Z.shape: {Z.shape}')
        self.ZK = Z.dot(self.K)  # ZK is dxn:  K is the nxn gram matrix of n random samples of N and Z is a dxn matrix.

        K_Nxn = self._get_kernel(X_train, X_sampled)  # kernel between X_N and X_sampled
        # X_new = 1/(self.n**(3/2)*np.sqrt(self.d))*(self.ZK.dot(self.K)).dot(K_Nxn.transpose())    # map X to X_d space (ZK*K_n*K_N), use the new X as input to KMeans
        X_new = 1 / (self.n ** (3 / 2) * np.sqrt(self.d)) * self.ZK.dot(
            K_Nxn.transpose())  # map X to X_d space (ZK*K_n*K_N), use the new X as input to KMeans

        X_new = X_new.transpose()

        self.kmeans = KMeans(self.n_clusters, random_state=self.random_state)
        self.kmeans.fit(X_new)

        self._mean = np.mean(X_sampled, axis=0)
        self.X_sampled = X_sampled - self._mean

        return self

        # self.kmeans.fit_predict(X_new)
        #
        # self.label_=self.kmeans.labels_

        # self.sample_weight_ = sample_weight if sample_weight else np.ones(n_samples)
        #
        # rs = check_random_state(self.random_state)
        # self.labels_ = rs.randint(self.n_clusters, size=n_samples)
        #
        # dist = np.zeros((n_samples, self.n_clusters))
        # self.within_distances_ = np.zeros(self.n_clusters)
        #
        # for it in range(self.max_iter):
        #     dist.fill(0)
        #     self._compute_dist(K, dist, self.within_distances_,
        #                        update_within=True)
        #     labels_old = self.labels_
        #     self.labels_ = dist.argmin(axis=1)
        #
        #     # Compute the number of samples whose cluster did not change
        #     # since last iteration.
        #     n_same = np.sum((self.labels_ - labels_old) == 0)
        #     if 1 - float(n_same) / n_samples < self.tol:
        #         if self.verbose:
        #             print("Converged at iteration", it + 1)
        #         break
        #
        # self.X_fit_ = X_sampled

    def predict(self, X, y=None):
        # K = self._get_kernel(X, self.X_fit_)  # kernel between X_test, and X_fit_
        # n_samples = X.shape[0]
        # dist = np.zeros((n_samples, self.n_clusters))
        # self._compute_dist(K, dist, self.within_distances_,
        #                    update_within=False)
        # return dist.argmin(axis=1)

        X_test = X
        X_test -= self._mean
        K_Mxn = self._get_kernel(X_test, self.X_sampled)  # kernel between X_M and X_sampled
        X_new = 1 / (self.n ** (3 / 2) * np.sqrt(self.d)) * self.ZK.dot(
            K_Mxn.transpose())  # map X to X_d space (ZK*K_n*K_N), use the new X as input to KMeans
        X_new = X_new.transpose()  # Mxd

        return self.kmeans.predict(X_new)

    def fit_predict(self, X):
        self.fit(X)
        self.predict(X)

        return self.predict(X)

    def predict_proba(self, X):
        pass
