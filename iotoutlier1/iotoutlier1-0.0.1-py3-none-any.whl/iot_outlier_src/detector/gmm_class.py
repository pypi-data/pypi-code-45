# Authors: kun.bj@outlook.com
#
# License: xxx
"""GMM class for anomaly detection

    labels=['normal':0, 'anomaly':1]
    invert

"""
from sklearn.base import BaseEstimator
from sklearn.metrics import confusion_matrix, roc_auc_score

from detector.base.base_detector import BaseDetector
from detector.base.gmm_base import GMM


class GMMDetector(BaseEstimator, BaseDetector):

    def __init__(self, n_components=5, covariance_type='full', quantile=0.9, means_init=None, random_state=42,
                 verbose=True):
        """

        :param n_components: represents the number of clusters (i.e., k in k-means), also represents the number of gaussian distributions is used to form GMM.
                             In anomaly detection, we just use normal data to train our model ( no anomaly data is used),
                             Use pdf of GMM as the measure function to determine normal and anomaly.
        :param quantile: for choose the threshold : Use the q-th percent of pdf as detection threshold: quantile =[0,1], percentile = [0,100]
        """
        # print(f'n_components: {n_components}, covariance_type: {covariance_type}')
        self.n_components = n_components
        self.covariance_type = covariance_type
        self.quantile = quantile
        self.verbose = verbose
        self.means_init = means_init
        self.random_state = random_state
        self.verbose = verbose

    def fit(self, X_train, y):
        """
            Using train set to find the parameters of GMM (such as mean, covariance and weight of each cluster)
        :param X_train:
        :return:
        """
        self.gmm = GMM(n_components=self.n_components, covariance_type=self.covariance_type, quantile=self.quantile,
                       means_init=self.means_init,
                       verbose=self.verbose, random_state=self.random_state)
        self.gmm.fit(X=X_train)

        return self

    # def predict(self, X):
    #     return self.gmm.predict(X)

    def test(self, X_test, y_test):
        """
            pyod.models.base.BaseDetector.labels_: The binary labels of the training data.
                                                0 stands for inliers and 1 for outliers/anomalies.
        :param X_test:
        :param y_test:
        :return:
        """

        # Predict if a particular sample is an outlier or not (0 is inlier and 1 for outlier).
        self.y_pred = self.gmm.predict(X=X_test)
        self.cm = confusion_matrix(y_true=y_test, y_pred=self.y_pred)
        if self.verbose:
            print(f'gmm.cm: \n=> predicted 0 and 1 (0 stands for normals and 1 for anomalies)\n{self.cm}')
        # roc_curve(y_true, y_score, pos_label=None, sample_weight=None, drop_intermediate=True):
        #   1) Target scores, can either be probability estimates of the positive class, confidence values, or
        #       non-thresholded measure of decisions (as returned by "decision_function" on some classifiers).'
        #   2) When ``pos_label=None``, if y_true is in {-1, 1} or {0, 1}, ``pos_label`` is set to 1 (default),
        #       otherwise an error will be raised.
        self.y_scores = self.gmm.predict_proba(X_test)[:, 1]  # y_scores=positive_class, which is used for ROC
        #   1) Default pos_label = 1,  [:,1] means that the predict proba of X is predicted as 1 (anomaly) by the model.
        #   2) [[0.7, 0.3], [0.8, 0.2], ...],It means that the model predicts a sample as label (0) with 0.7 prabability.

        # Compute Area Under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores (y_scores).
        self.auc = roc_auc_score(y_true=y_test, y_score=self.y_scores)
        print(f'auc: {self.auc}')

    # def score(self, X, y=None):
    #     """Compute the per-sample average log-likelihood of the given data X.
    #
    #     Parameters
    #     ----------
    #     X : array-like, shape (n_samples, n_dimensions)
    #         List of n_features-dimensional data points. Each row
    #         corresponds to a single data point.
    #
    #     Returns
    #     -------
    #     log_likelihood : float
    #         Log likelihood of the Gaussian mixture given X.
    #     """
    #     return self.score_samples(X).mean()

    # def get_params(self, deep=True):
    #     return {"n_components": self.n_components, "covariance_type": self.covariance_type, "quantile": self.quantile,
    #             "verbose": self.verbose}
    #
    # def set_params(self, **parameters):
    #     for parameter, value in parameters.items():
    #         setattr(self, parameter, value)
    #     return self
