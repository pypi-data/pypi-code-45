""" Kernel K-means (KKMeans)

"""

# Authors: kun.bj@outlook.com
#
# License: xxx


from sklearn.metrics import confusion_matrix

from legacy.detection_algorithms.proposed.k_jl_class_base import K_JL_Class_Base


class K_JL_Class(K_JL_Class_Base):

    def __init__(self, n_clusters=2, kernel='linear', max_iter=100, random_state=42, verbose=True):
        super(K_JL_Class, self).__init__()
        self.max_iter = max_iter
        self.random_state = random_state

        # self.k_JL_kmeans= BaseKKMeans()
        self.k_JL_kmeans = K_JL_Class_Base(n_clusters=n_clusters, kernel=kernel, random_state=random_state)
        self.alg_name = 'K-JL'
        self.verbose = verbose

    def train(self, X, y=None, val_set_dict={}):
        self.k_JL_kmeans.fit(X)

        # self.predict(X)
        # return

    def test(self, X, y=None):
        """
            pyod.models.base.BaseDetector.labels_: The binary labels of the training data.
                                                0 stands for inliers and 1 for outliers/anomalies.
        :param X_test:
        :param y_test:
        :return:
        """
        X_test = X
        y_test = y
        print(f'y_test: {y}')
        # Predict if a particular sample is an outlier or not (0 is inlier and 1 for outlier).
        self.y_preds = self.k_JL_kmeans.predict(X=X_test)
        print(f'y_pred: {self.y_preds}')
        self.cm = confusion_matrix(y_true=y_test, y_pred=self.y_preds)  # labels=['anomaly':0, 'normal':1]
        print(f'cm: {self.cm}')
        # print(f'kkmeans.cm: \n=> predicted 0 and 1 (0 stands for normals and 1 for anomalies)\n{self.cm}')
        # # roc_curve(y_true, y_score, pos_label=None, sample_weight=None, drop_intermediate=True):
        # #   1) Target scores, can either be probability estimates of the positive class, confidence values, or
        # #       non-thresholded measure of decisions (as returned by "decision_function" on some classifiers).'
        # #   2) When ``pos_label=None``, if y_true is in {-1, 1} or {0, 1}, ``pos_label`` is set to 1, otherwise an
        # #       error will be raised.
        # self.y_scores = self.k_JL_kmeans.predict_proba(X_test)[:, 1]
        # #   1) Default pos_label = 1,  [:,1] means that the predict proba of X is predicted as 1 (anomaly) by the model.
        # #   2) [[0.7, 0.3], [0.8, 0.2], ...],It means that pca predict a sample as label (0) with 0.7 prabability.
        #
        # # Compute Area Under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores (y_scores).
        # self.auc = roc_auc_score(y_true=y_test, y_score=self.y_scores)

        return self.y_preds


if __name__ == '__main__':
    import pandas as pd
    import matplotlib.pyplot as plt

    random_state = 42
    from sklearn.datasets import make_blobs

    X, y = make_blobs(n_samples=1000, centers=5, random_state=random_state)
    print(f'X.shape: {X.shape}')
    plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap='viridis')
    plt.show()

    index = [i for i in range(X.shape[0])]
    columns = [i for i in range(X.shape[1])]
    data = pd.DataFrame(data=X, index=index, columns=columns)
    pd.set_option('display.max_columns', None)  # in order to display all columns in terminal
    print(data.describe())

    # km = KernelKMeans(n_clusters=5, max_iter=100, random_state=random_state, verbose=1)
    k_jl_kmeans = K_JL_Class(n_clusters=5, kernel='rbf', random_state=random_state, max_iter=100, verbose=1)
    k_jl_kmeans.train(X)

    k_jl_kmeans.test(X[:20], y[:20])
