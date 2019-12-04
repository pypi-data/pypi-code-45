# Authors: kun.bj@outlook.com
#
# License: xxx
""" Base GMM class is based on sklearn and pyod

"""

import numpy as np
from pyod.models.base import BaseDetector
from pyod.utils import invert_order
from scipy.special import logsumexp
from sklearn.mixture.base import _check_X
from sklearn.mixture.gaussian_mixture import GaussianMixture
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import check_array
from sklearn.utils.validation import check_is_fitted


class GMM(BaseDetector, GaussianMixture):
    def __init__(self, n_components=1, covariance_type='full', tol=1e-3,
                 reg_covar=1e-6, max_iter=100, n_init=1, init_params='kmeans',
                 weights_init=None, means_init=None, precisions_init=None,
                 random_state=None, warm_start=False,
                 verbose=0, verbose_interval=10, contamination=0.1, quantile=0.9):
        super(GMM, self).__init__(contamination=contamination)
        self.n_components = n_components
        self.covariance_type = covariance_type
        self.tol = tol
        self.reg_covar = reg_covar
        self.max_iter = max_iter
        self.n_init = n_init
        self.init_params = init_params
        self.weights_init = weights_init
        self.means_init = means_init
        self.precisions_init = precisions_init
        self.random_state = random_state
        self.warm_start = warm_start
        self.verbose = verbose
        self.verbose_interval = verbose_interval
        self.quantile = quantile  # for detecction threshold

        self._classes = 2  # default as binary classification

    def fit(self, X, y=None):
        """Fit detector. y is optional for unsupervised methods.

        Parameters
        ----------
        X : numpy array of shape (n_samples, n_features)
            The input samples.

        y : numpy array of shape (n_samples,), optional (default=None)
            The ground truth of the input samples (labels).
        """
        # validate inputs X and y (optional)
        X = _check_X(X)
        self._set_n_classes(y)

        self.detector_ = GaussianMixture(n_components=self.n_components,
                                         covariance_type=self.covariance_type,
                                         tol=self.tol,
                                         reg_covar=self.reg_covar,
                                         max_iter=self.max_iter,
                                         n_init=self.n_init,
                                         init_params=self.init_params,
                                         weights_init=self.weights_init,
                                         means_init=self.means_init,
                                         precisions_init=self.precisions_init,
                                         random_state=self.random_state,
                                         warm_start=self.warm_start,
                                         verbose=self.verbose,
                                         verbose_interval=self.verbose_interval)
        self.detector_.fit(X=X, y=y)

        # log_prob_norm = logsumexp(self.detector_._estimate_weighted_log_prob(X), axis=1)
        # self.decision_scores_ = log_prob_norm  # log(sum(pi* normal()))

        # invert decision_scores_. Outliers comes with higher outlier scores
        self.decision_scores_ = invert_order(logsumexp(self.detector_._estimate_weighted_log_prob(X), axis=1))

        print(f'quantile: {self.quantile}')
        # stat_data(self.decision_scores_.reshape(-1, 1))
        self.threshold_ = np.quantile(a=self.decision_scores_,
                                      q=self.quantile)  # np.percentile will sort the input
        print(f'threshold_: {self.threshold_}')
        # idx = int(self.quantile * self.decision_scores_.shape[0])
        # self.threshold_ = sorted(self.decision_scores_, reverse=False)[idx]
        # # # self.gmm.detect_thres = get_thres(self.decision_scores_, percent=self.quantile)
        # print(f'threshold_: {self.threshold_}')

        # self.labels_ = (self.decision_scores_ < self.threshold_).astype('int').ravel()    # False=0, True = 1, so it should be '<'. normal=0, anomaly = 1
        self.labels_ = np.zeros(X.shape[0])
        self.labels_[self.decision_scores_ > self.threshold_] = 1  # 0 is normal, 1 is abnormal

        # self._process_decision_scores()   # get self.threshold_

        return self

    def decision_function(self, X):
        """Predict raw anomaly scores of X using the fitted detector.

        The anomaly score of an input sample is computed based on the fitted
        detector. For consistency, outliers are assigned with
        larger anomaly scores. so use invert_order

        After invert_order(): the higher score, the more probability of x that is predicted as abnormal

        Parameters
        ----------
        X : numpy array of shape (n_samples, n_features)
            The input samples. Sparse matrices are accepted only
            if they are supported by the base estimator.

        Returns
        -------
        anomaly_scores : numpy array of shape (n_samples,)
            The anomaly score of the input samples.
        """
        check_is_fitted(self, ['decision_scores_', 'threshold_', 'labels_'])
        return invert_order(logsumexp(self.detector_._estimate_weighted_log_prob(X), axis=1))

    def predict(self, X='X_test', y=None):
        """Predict if a particular sample is an outlier or not.

        Parameters
        ----------
        X : numpy array of shape (n_samples, n_features)
            The input samples.

        Returns
        -------
        outlier_labels : numpy array of shape (n_samples,)
            For each observation, tells whether or not
            it should be considered as an outlier according to the
            fitted model. 0 stands for inliers and 1 for outliers.
        """
        # # y_pred = self._estimate_weighted_log_prob(X_test).argmax(axis=1)  # predict the x belongs to which component.
        # y_pred = np.zeros(X_test.shape[0])
        # y_pred[self.predict_proba(X_test) < self.detect_thres] = 1  # 0 is normal, 1 is abnormal

        X = check_array(X)
        check_is_fitted(self, ['decision_scores_', 'threshold_', 'labels_'])

        pred_score = self.decision_function(X)
        y_pred = np.zeros(X.shape[0])
        y_pred[pred_score > self.threshold_] = 1  # 0 is normal, 1 is abnormal

        return y_pred

    def predict_proba(self, X, method='linear'):
        """Predict the probability of a sample being outlier. Two approaches
        are possible:

        1. simply use Min-max conversion to linearly transform the outlier
           scores into the range of [0,1]. The model must be
           fitted first.
        2. use unifying scores, see :cite:`kriegel2011interpreting`.

        Parameters
        ----------
        X : numpy array of shape (n_samples, n_features)
            The input samples.

        method : str, optional (default='linear')
            probability conversion method. It must be one of
            'linear' or 'unify'.

        Returns
        -------
        outlier_labels : numpy array of shape (n_samples,)
            For each observation, tells whether or not
            it should be considered as an outlier according to the
            fitted model. Return the outlier probability, ranging
            in [0,1].
        """
        X = check_array(X)
        check_is_fitted(self, ['decision_scores_', 'threshold_', 'labels_'])
        train_scores = self.decision_scores_

        test_scores = self.decision_function(
            X)  # the probability density (not probability) of x is predicted as anomaly

        probs = np.zeros([X.shape[0], int(self._classes)])
        if method == 'linear':
            scaler = MinMaxScaler().fit(train_scores.reshape(-1, 1))
            probs[:, 1] = scaler.transform(
                test_scores.reshape(-1, 1)).ravel().clip(0, 1)
            probs[:, 0] = 1 - probs[:, 1]
            return probs
        else:
            raise ValueError(method,
                             'is not a valid probability conversion method')
    #
    # def _estimate_log_gaussian_prob(self, X, means, precisions_chol, covariance_type):
    #     """Estimate the log Gaussian probability.
    #
    #     Parameters
    #     ----------
    #     X : array-like, shape (n_samples, n_features)
    #
    #     means : array-like, shape (n_components, n_features)
    #
    #     precisions_chol : array-like
    #         Cholesky decompositions of the precision matrices.
    #         'full' : shape of (n_components, n_features, n_features)
    #         'tied' : shape of (n_features, n_features)
    #         'diag' : shape of (n_components, n_features)
    #         'spherical' : shape of (n_components,)
    #
    #     covariance_type : {'full', 'tied', 'diag', 'spherical'}
    #
    #     Returns
    #     -------
    #     log_prob : array, shape (n_samples, n_components)
    #     """
    #     n_samples, n_features = X.shape
    #     n_components, _ = means.shape
    #     # det(precision_chol) is half of det(precision)
    #     log_det = _compute_log_det_cholesky(
    #         precisions_chol, covariance_type, n_features)
    #
    #     if covariance_type == 'full':
    #         log_prob = np.empty((n_samples, n_components))
    #         for k, (mu, prec_chol) in enumerate(zip(means, precisions_chol)):
    #             y = np.dot(X, prec_chol) - np.dot(mu, prec_chol)
    #             log_prob[:, k] = np.sum(np.square(y), axis=1)
    #
    #     elif covariance_type == 'tied':
    #         log_prob = np.empty((n_samples, n_components))
    #         for k, mu in enumerate(means):
    #             y = np.dot(X, precisions_chol) - np.dot(mu, precisions_chol)
    #             log_prob[:, k] = np.sum(np.square(y), axis=1)
    #
    #     elif covariance_type == 'diag':
    #         precisions = precisions_chol ** 2
    #         log_prob = (np.sum((means ** 2 * precisions), 1) -
    #                     2. * np.dot(X, (means * precisions).T) +
    #                     np.dot(X ** 2, precisions.T))
    #
    #     elif covariance_type == 'spherical':
    #         precisions = precisions_chol ** 2
    #         log_prob = (np.sum(means ** 2, 1) * precisions -
    #                     2 * np.dot(X, means.T * precisions) +
    #                     np.outer(row_norms(X, squared=True), precisions))
    #     return -.5 * (n_features * np.log(2 * np.pi) + log_prob) + log_det
    #
    # def __initialize_model(self, X, resp=0):
    #     """Initialization of the Gaussian mixture parameters.
    #
    #         Parameters
    #         ----------
    #         X : array-like, shape (n_samples, n_features)
    #
    #         resp : array-like, shape (n_samples, n_components)
    #     """
    #     n_samples, _ = X.shape
    #
    #     random_state = check_random_state(self.random_state)
    #     resp = random_state.rand(n_samples, self.n_components)
    #     resp /= resp.sum(axis=1)[:, np.newaxis]  # responsibilities
    #
    #     weights, means, covariances = _estimate_gaussian_parameters(
    #         X, resp, self.reg_covar,
    #         self.covariance_type)  # weights = nk: the number of data samples in the current component.
    #     weights /= n_samples  # (weights/n)  means pi_k: mixing coefficients
    #
    #     # self.weights_ = (weights if self.weights_init is None
    #     #                  else self.weights_init)
    #     # self.means_ = means if self.means_init is None else self.means_init
    #
    #     self.weights_ = weights
    #     self.means_ = means
    #     self.precisions_init = None
    #
    #     if self.precisions_init is None:
    #         self.covariances_ = covariances
    #         self.precisions_cholesky_ = _compute_precision_cholesky(
    #             covariances, self.covariance_type)
    #     elif self.covariance_type == 'full':
    #         self.precisions_cholesky_ = np.array(
    #             [linalg.cholesky(prec_init, lower=True)
    #              for prec_init in self.precisions_init])
    #     elif self.covariance_type == 'tied':
    #         self.precisions_cholesky_ = linalg.cholesky(self.precisions_init,
    #                                                     lower=True)
    #     else:
    #         self.precisions_cholesky_ = self.precisions_init
    #

    # def _e_step(self, X):
    #     """E step.
    #
    #     Parameters
    #     ----------
    #     X : array-like, shape (n_samples, n_features)
    #
    #     Returns
    #     -------
    #     log_prob_norm : float
    #         Mean of the logarithms of the probabilities of each sample in X
    #
    #     log_responsibility : array, shape (n_samples, n_components)
    #         Logarithm of the posterior probabilities (or responsibilities) of
    #         the point of each sample in X.
    #     """
    #     log_prob_norm, log_resp = self._estimate_log_prob_resp(X)
    #     return np.mean(log_prob_norm), log_resp
    #
    # def _m_step(self, X, log_resp):
    #     """M step.
    #
    #     Parameters
    #     ----------
    #     X : array-like, shape (n_samples, n_features)
    #
    #     log_resp : array-like, shape (n_samples, n_components)
    #         Logarithm of the posterior probabilities (or responsibilities) of
    #         the point of each sample in X.
    #     """
    #     n_samples, _ = X.shape
    #     self.weights_, self.means_, self.covariances_ = (
    #         _estimate_gaussian_parameters(X, np.exp(log_resp), self.reg_covar,
    #                                       self.covariance_type))
    #     self.weights_ /= n_samples
    #     self.precisions_cholesky_ = _compute_precision_cholesky(
    #         self.covariances_, self.covariance_type)
    #
    # def _estimate_log_prob_resp(self, X):
    #     """Estimate log probabilities and responsibilities for each sample.
    #
    #     Compute the log probabilities, weighted log probabilities per
    #     component and responsibilities for each sample in X with respect to
    #     the current state of the model.
    #
    #     Parameters
    #     ----------
    #     X : array-like, shape (n_samples, n_features)
    #
    #     Returns
    #     -------
    #     log_prob_norm : array, shape (n_samples,)
    #         log p(X)
    #
    #     log_responsibilities : array, shape (n_samples, n_components)
    #         logarithm of the responsibilities
    #     """
    #     weighted_log_prob = self._estimate_weighted_log_prob(X)
    #     log_prob_norm = logsumexp(weighted_log_prob, axis=1)
    #     with np.errstate(under='ignore'):
    #         # ignore underflow
    #         log_resp = weighted_log_prob - log_prob_norm[:, np.newaxis]
    #     return log_prob_norm, log_resp
    #
    # def _estimate_weighted_log_prob(self, X):
    #     """Estimate the weighted log-probabilities, log P(X | Z) + log weights.
    #
    #     Parameters
    #     ----------
    #     X : array-like, shape (n_samples, n_features)
    #
    #     Returns
    #     -------
    #     weighted_log_prob : array, shape (n_samples, n_component)
    #     """
    #     return self._estimate_log_prob(X) + self._estimate_log_weights()
    #
    # def _estimate_log_prob(self, X):
    #
    #     log_prob = self._estimate_log_gaussian_prob(
    #         X, self.means_, self.precisions_cholesky_, self.covariance_type)
    #     return log_prob
    #
    #     # # if train_flg:  # normalize to [0,1]
    #     # #     self.prob_min = np.min(np.exp(log_prob), axis=0)
    #     # #     self.prob_max = np.max(np.exp(log_prob), axis=0)
    #     # v= (np.exp(log_prob) - self.prob_min) / (self.prob_max-self.prob_min)  # (x-min) / (max-min)
    #
    #     # return np.log(v)
    #
    # def _estimate_log_weights(self):
    #     return np.log(self.weights_)
    #
    # def _compute_lower_bound(self, _, log_prob_norm):
    #     return log_prob_norm
    #
    # # def test(self, X_test, y_test):
    # #     y_pred = self.predict(X_test=X_test)
    # #
    # #     cm = confusion_matrix(y_true=y_test, y_pred=y_pred)
#     # #     print(f'{cm}')
#     #
#
#
# def get_percentile(pdf, percent=0.95):
#     cusum = 0.0
#     for v in sorted(pdf, reverse=True):
#
#         cusum += v
#         if cusum / sum(pdf) > percent:
#             value = v
#             break
#
#     return value
#
#
# def get_thres(y_score, percent=0.95):
#     values = sorted(y_score, reverse=True)
#     cumsum = 0.0
#     for v in values:
#         cumsum += v
#         if cumsum >= percent:
#             print(f'cumsum: {cumsum}, thres: {v}')
#             break
#
#     return v
#
#
# def measure(y_test_orig, y_test_proba):
#     print('Classification report')
#     print(classification_report(y_test_orig, y_test_proba))
#     print('Test AUCPR = ' + str(average_precision_score(y_test_orig, y_test_proba)))
#
#     precision, recall, _ = precision_recall_curve(y_test_orig, y_test_proba)
#     plt.step(recall, precision, color='b', alpha=0.2, where='post')
#     plt.fill_between(recall, precision, step='post', alpha=0.2, color='b')
#     plt.xlabel('Recall')
#     plt.ylabel('Precision')
#     plt.ylim([0.0, 1.05])
#     plt.xlim([0.0, 1.0])
#     plt.title('2-class Precision-Recall curve: AUC={0:0.2f}'.format(average_precision_score(y_test_orig, y_test_proba)))
#
#
# def plot_contour():
#     X, Y = np.meshgrid(np.linspace(-1, 6), np.linspace(-1, 6))
#     XX = np.array([X.ravel(), Y.ravel()]).T
#     Z = gmm.score_samples(XX)
#     Z = Z.reshape((50, 50))
#
#     plt.contour(X, Y, Z)
#     plt.scatter(X_train[:, 0], X_train[:, 1])
#
#     plt.show()
#
# #
# # def get_mixture_quantile(p='', component_distributions, ps):
#     """
#
#     :param p:
#     :param component_distributions:
#     :param ps:
#     :return:
#     """
#     # Return the pth quantile of the mixture distribution given by the component distributions and their probabilities
#
#     # Return the function that is the cdf of the mixture distribution
#     def get_mixture_cdf(component_distributions, ps='p_mixture'):
#         return lambda x: sum(component_dist.cdf(x) * p for component_dist, p in zip(component_distributions, ps))
#
#     # Return the smallest value x between lo and hi such that f(x) >= v
#     def continuous_bisect_fun_left(f, v, lo, hi):
#         val_range = [lo, hi]
#         k = 0.5 * sum(val_range)
#         for i in range(32):
#             val_range[int(f(k) > v)] = k
#             next_k = 0.5 * sum(val_range)
#             if next_k == k:
#                 break
#             k = next_k
#         return k
#
#     mixture_cdf = get_mixture_cdf(component_distributions, ps)
#
#     # We can probably be a bit smarter about how we pick the limits
#     lo = np.min([dist.ppf(p) for dist in component_distributions])
#     hi = np.max([dist.ppf(p) for dist in component_distributions])
#
#     return continuous_bisect_fun_left(mixture_cdf, p, lo, hi)
