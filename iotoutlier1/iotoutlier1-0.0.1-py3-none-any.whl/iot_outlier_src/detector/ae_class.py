# Authors: kun.bj@outlook.com
#
# License: xxx
"""
    One-Class SVM (ocsvm) class

"""
from keras import optimizers
from pyod.models.auto_encoder import AutoEncoder
from sklearn.base import BaseEstimator
from sklearn.metrics import confusion_matrix, roc_auc_score

from detector.base.base_detector import BaseDetector


class AEDetector(BaseEstimator, BaseDetector):

    def __init__(self, gamma='auto', kernel='rbf', verbose=True, random_state=42):
        self.gamma = gamma
        self.kernel = kernel
        self.verbose = verbose

        self.random_state = random_state
        # print('')

    def fit(self, X_train, y_train):
        # default: [64, 32, 32, 64], however, it require np.min(hidden_neurons) > the input size,
        # so it adds '8' into hidden_neurons.
        # latent_num = 8
        # if len(X_train[0]) < latent_num:
        #     latent_num = len(X_train[0])
        # self.ae = AutoEncoder(hidden_neurons=[64, 32, latent_num, 32, 64],
        #                       hidden_activation='relu', output_activation=None,
        #                       optimizer='adam',
        #                       epochs=100, batch_size=8, dropout_rate=0,
        #                       l2_regularizer=0.1, validation_size=0.1, preprocessing=False,     # we have done nomarlization before fit()
        #                       verbose=1, random_state=self.random_state, contamination=0.01)

        latent_num = len(X_train[0])
        adam_opt = optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, amsgrad=False, decay=0.1)
        self.ae = AutoEncoder(hidden_neurons=[64, 32, latent_num, 32, 64],
                              hidden_activation='relu', output_activation=None,
                              optimizer=adam_opt,
                              epochs=100, batch_size=32, dropout_rate=0.2,
                              l2_regularizer=0.1, validation_size=0.1, preprocessing=False,
                              # we have done nomarlization before fit()
                              verbose=1, random_state=self.random_state, contamination=0.1)

        self.ae.fit(X=X_train)

        return self

    def test(self, X_test, y_test):
        """
            pyod.models.base.BaseDetector.labels_: The binary labels of the training data.
                                                0 stands for inliers and 1 for outliers/anomalies.
        :param X_test:
        :param y_test:
        :return:
        """
        # Predict if a particular sample is an outlier or not (0 is inlier and 1 for outlier).
        self.y_preds = self.ae.predict(X=X_test)
        print(f'thres: {self.ae.decision_scores_}')
        self.cm = confusion_matrix(y_true=y_test, y_pred=self.y_preds)  # labels=['anomaly':0, 'normal':1]
        print(f'ocsvm.cm: \n=> predicted 0 and 1 (0 stands for normals and 1 for anomalies)\n{self.cm}')
        # roc_curve(y_true, y_score, pos_label=None, sample_weight=None, drop_intermediate=True):
        #   1) Target scores, can either be probability estimates of the positive class, confidence values, or
        #       non-thresholded measure of decisions (as returned by "decision_function" on some classifiers).'
        #   2) When ``pos_label=None``, if y_true is in {-1, 1} or {0, 1}, ``pos_label`` is set to 1, otherwise an
        #       error will be raised.
        self.y_scores = self.ae.predict_proba(X_test)[:, 1]  # y_scores=positive_class, which is used for ROC
        #   1) Default pos_label = 1,  [:,1] means that the predict proba of X is predicted as 1 (anomaly) by the model.
        #   2) [[0.7, 0.3], [0.8, 0.2], ...],It means that pca predict a sample as label (0) with 0.7 prabability.

        # Compute Area Under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores (y_scores).
        self.auc = roc_auc_score(y_true=y_test, y_score=self.y_scores)
        print(f'auc: {self.auc}')