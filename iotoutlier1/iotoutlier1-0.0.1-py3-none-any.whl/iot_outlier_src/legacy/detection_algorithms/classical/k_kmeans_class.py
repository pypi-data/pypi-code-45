# Authors: kun.bj@outlook.com
#
# License: xxx

""" Kernel K-means (KKMeans)

"""
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix

from legacy.detection_algorithms import BaseClass


class BaseKKMeans(BaseClass):
    def __init__(self):
        super(BaseKKMeans, self).__init__()
        pass

    def fit(self, X):
        pass

    def predict(self, X):
        pass

    def predict_proba(self, X):
        pass


class KKMeans_Class(BaseKKMeans):

    def __init__(self, n_clusters=2, kernel='', verbose=True):
        super(KKMeans_Class, self).__init__()

        self.kkmeans = KMeans()
        # self.kkmeans = KernelKMeans(n_clusters=n_clusters, kernel=kernel)
        self.alg_name = 'Kernel KMeans'
        self.verbose = verbose

    def train(self, X, y=None, val_set_dict={}):
        self.kkmeans.fit(X)

    def test(self, X, y):
        """
            pyod.models.base.BaseDetector.labels_: The binary labels of the training data.
                                                0 stands for inliers and 1 for outliers/anomalies.
        :param X_test:
        :param y_test:
        :return:
        """
        X_test = X
        y_test = y
        # Predict if a particular sample is an outlier or not (0 is inlier and 1 for outlier).
        self.y_preds = self.kkmeans.predict(X=X_test)
        self.cm = confusion_matrix(y_true=y_test, y_pred=self.y_preds)  # labels=['anomaly':0, 'normal':1]
        print(f'kkmeans.cm: \n=> predicted 0 and 1 (0 stands for normals and 1 for anomalies)\n{self.cm}')
        # roc_curve(y_true, y_score, pos_label=None, sample_weight=None, drop_intermediate=True):
        #   1) Target scores, can either be probability estimates of the positive class, confidence values, or
        #       non-thresholded measure of decisions (as returned by "decision_function" on some classifiers).'
        #   2) When ``pos_label=None``, if y_true is in {-1, 1} or {0, 1}, ``pos_label`` is set to 1, otherwise an
        #       error will be raised.
        # self.y_scores = self.kkmeans.predict_proba(X_test)[:, 1]
        #   1) Default pos_label = 1,  [:,1] means that the predict proba of X is predicted as 1 (anomaly) by the model.
        #   2) [[0.7, 0.3], [0.8, 0.2], ...],It means that pca predict a sample as label (0) with 0.7 prabability.

        # Compute Area Under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores (y_scores).
        # self.auc = roc_auc_score(y_true=y_test, y_score=self.y_scores)
