"""
    GMM class

"""
from sklearn.metrics import roc_auc_score

# from sklearn.mixture import GaussianMixture
from detector.base.gmm_base import GMM, stat_data


class GMM_Class():

    def __init__(self, n_components=5, verbose=True):
        """

        :param n_components: represents the number of clusters (i.e., k in k-means), also represents the number of gaussian distributions is used to form GMM.
                             In anomaly detection, we just use normal data to train our model ( no anomaly data is used),
                             Use pdf of GMM as the measure function to determine normal and anomaly.
        """
        self.gmm = GMM(n_components=n_components, verbose=verbose)
        self.verbose = verbose
        self.quantile = 0.9  # Use the q-th percent of pdf as detection threshold

    def train(self, X_train):
        """
            Using train set to find the parameters of GMM (such as mean, covariance and weight of each cluster)
        :param X_train:
        :return:
        """
        self.gmm.fit(X=X_train)
        # y_scores1 = np.sum(np.exp(self.gmm._estimate_weighted_log_prob(X_train)), axis=1)  # should be in [0,1]
        # log_prob_norm, log_resp= self.gmm._estimate_log_prob_resp(X_train)

        train_flg = True
        # log_prob = self.gmm._estimate_log_gaussian_prob(
        #     X_train, self.gmm.means_, self.gmm.precisions_cholesky_, self.gmm.covariance_type)
        # if train_flg:  # normalize the value of pdf of normal samples to [0,1]
        #     self.prob_min = np.min(np.exp(log_prob), axis=0)
        #     self.prob_max = np.max(np.exp(log_prob), axis=0)
        #     self.prob_range =  (self.prob_max-self.prob_min)
        # try:
        #     log_v= (np.exp(log_prob) - self.prob_min) / self.prob_range # (x-min) / (max-min)
        # except :
        #     print(f'prob_range: {self.prob_range}')
        # v[v==0] = 10e-8
        # log_prob_norm = np.sum(v + self.gmm._estimate_log_weights(), axis=1)  # sum( log p(x) + log(pi))

        log_prob, log_resp = self.gmm._estimate_log_prob_resp(X_train)
        if train_flg:  # normalize the value of pdf of normal samples to [0,1]
            self.prob_min = np.min(np.exp(log_prob))
            self.prob_max = np.max(np.exp(log_prob))
            self.prob_range = (self.prob_max - self.prob_min)
        try:
            y_scores = (np.exp(log_prob) - self.prob_min) / self.prob_range  # (x-min) / (max-min)
        except:
            print(f'prob_range: {self.prob_range}')
        # self.gmm.thres = get_mixture_quantile_by_sampling(y_scores, quantile=self.quantile)

        # self.gmm.thres = get_thres(y_scores, percent= 0.95)

        percent = self.quantile * 100
        print(f'percent: {percent}')
        stat_data(y_scores.reshape(-1, 1))
        # self.gmm.detect_thres = np.percentile(a=sorted(y_scores, reverse=False), q=100 - percent)
        self.gmm.detect_thres = get_thres(y_scores, percent=self.quantile)
        print(f'detect_thres: {self.gmm.detect_thres}')

    def test(self, X_test, y_test):
        """
            pyod.models.base.BaseDetector.labels_: The binary labels of the training data.
                                                0 stands for inliers and 1 for outliers/anomalies.
        :param X_test:
        :param y_test:
        :return:
        """
        # Predict if a particular sample is an outlier or not (0 is inlier and 1 for outlier).
        # self.y_preds = self.gmm.predict(X=X_test)
        # self.cm = confusion_matrix(y_true=y_test, y_pred=self.y_preds)  # labels=['anomaly':0, 'normal':1]
        # print(f'gmm.cm: \n=> predicted 0 and 1 (0 stands for normals and 1 for anomalies)\n{self.cm}')
        # roc_curve(y_true, y_score, pos_label=None, sample_weight=None, drop_intermediate=True):
        #   1) Target scores, can either be probability estimates of the positive class, confidence values, or
        #       non-thresholded measure of decisions (as returned by "decision_function" on some classifiers).'
        #   2) When ``pos_label=None``, if y_true is in {-1, 1} or {0, 1}, ``pos_label`` is set to 1, otherwise an
        #       error will be raised.
        # self.y_scores = self.gmm.predict_proba(X_test)[:, 1]  # use n_component =1, it won't get [:,1]
        # self.y_scores = 1 - self.gmm.predict_proba(X_test)[:, 0]
        # self.y_scores = np.sum(np.exp(self.gmm._estimate_weighted_log_prob(X_test, train_flg=False)), axis=1)
        # log_prob = self.gmm._estimate_log_gaussian_prob(
        #     X_test, self.gmm.means_, self.gmm.precisions_cholesky_, self.gmm.covariance_type)
        # v = (np.exp(log_prob) - self.prob_min) / self.prob_range  # (x-min) / (max-min)  # normalize pdf
        #
        # log_prob_norm = np.sum(np.log(v) + self.gmm._estimate_log_weights(), axis=1)  # sum( log p(x) + log(pi))

        log_prob, log_resp = self.gmm._estimate_log_prob_resp(X_test)
        self.y_scores = (np.exp(log_prob) - self.prob_min) / self.prob_range  # (x-min) / (max-min)  # normalize pdf

        self.y_preds = np.zeros((len(y_test), 1))

        self.y_preds[self.y_scores < self.gmm.detect_thres] = 1
        self.cm = confusion_matrix(y_true=y_test, y_pred=self.y_preds)  # labels=['anomaly':0, 'normal':1]
        print(f'gmm.cm: \n=> predicted 0 and 1 (0 stands for normals and 1 for anomalies)\n{self.cm}')
        #   1) Default pos_label = 1,  [:,1] means that the predict proba of X is predicted as 1 (anomaly) by the model.
        #   2) [[0.7, 0.3], [0.8, 0.2], ...],It means that pca predict a sample as label (0) with 0.7 prabability.

        # Compute Area Under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores (y_scores).
        self.auc = roc_auc_score(y_true=y_test, y_score=self.y_scores)


#
# def get_mixture_quantile(p='', component_distributions, ps):
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


def get_thres(y_score, percent=0.95):
    values = sorted(y_score, reverse=True)
    cumsum = 0.0
    for v in values:
        cumsum += v
        if cumsum >= percent:
            print(f'cumsum: {cumsum}, thres: {v}')
            break

    return v


#
#
# def get_mixture_quantile_by_sampling(samples, quantile=0.75):
#     """   Now let 's calculate the same thing by sampling.
#
#     :return:
#     """
#     import numpy as np
#
#     #
#     # N = 200000
#     # # Determine how many of our samples are from the normal distribution,
#     # # and how many from the exponential distribution, based on a fair coin flip
#     # num_normal = np.random.binomial(N, 0.5)
#     # num_exponential = N - num_normal
#     #
#     # # Gather our normal and exponential samples
#     # normal_samples = np.random.normal(size=num_normal)
#     # expon_samples = np.random.exponential(size=num_exponential)
#     #
#     # # Pool the samples
#     # samples = np.hstack((normal_samples, expon_samples))
#
#     sample_quantile = np.percentile(samples, quantile * 100)
#     print(f"Quantile from sample for quantile = {quantile}: {sample_quantile}")
#
#     return sample_quantile


from collections import OrderedDict

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy import linalg
from scipy.special import logsumexp
from sklearn import mixture
from sklearn.metrics import confusion_matrix
from sklearn.mixture.gaussian_mixture import _compute_precision_cholesky, _estimate_gaussian_parameters, \
    _estimate_log_gaussian_prob, _compute_log_det_cholesky
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import check_random_state
import pandas as pd
from sklearn.utils.extmath import row_norms

from _config import *
from legacy.utils import load_and_split_data, select_features_from_list
from legacy.utils.visualization import plot_auc_and_strength_of_outiler
from collections import Counter


def stat_data(data=None):
    #
    # import inspect
    # a= inspect.signature(stat_data)
    columns = ['col_' + str(i) for i in range(data.shape[1])]
    dataset = pd.DataFrame(data=data, index=range(data.shape[0]), columns=columns)
    print(f'data.shape: {data.shape}')
    print(dataset.describe())


def gmm_demo():
    n_samples = 300

    # generate random sample, two components
    np.random.seed(0)

    # generate spherical data centered on (20, 20)
    shifted_gaussian = np.random.randn(n_samples, 2) + np.array([20, 20])

    # generate zero centered stretched Gaussian data
    C = np.array([[0., -0.7], [3.5, .7]])
    stretched_gaussian = np.dot(np.random.randn(n_samples, 2), C)

    # concatenate the two datasets into the final training set
    X_train = np.vstack([shifted_gaussian, stretched_gaussian])

    # fit a Gaussian Mixture Model with two components
    clf = mixture.GaussianMixture(n_components=2, covariance_type='full')
    clf.fit(X_train)

    # display predicted scores by the model as a contour plot
    x = np.linspace(-20., 30.)
    y = np.linspace(-20., 40.)
    X, Y = np.meshgrid(x, y)
    XX = np.array([X.ravel(), Y.ravel()]).T
    Z = -clf.score_samples(XX)
    Z = Z.reshape(X.shape)

    CS = plt.contour(X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0),
                     levels=np.logspace(0, 3, 10))
    CB = plt.colorbar(CS, shrink=0.8, extend='both')
    plt.scatter(X_train[:, 0], X_train[:, 1], .8)

    plt.title('Negative log-likelihood predicted by a GMM')
    plt.axis('tight')
    plt.show()


class GMM():

    def __init__(self, n_components, max_iter=100, tol=1e-4, covariance_type='full', random_state=42, verbose=True):

        self.n_components = n_components

        self.max_iter = max_iter
        self.random_state = random_state
        self.tol = tol

        self.reg_covar = 1e-6
        self.covariance_type = covariance_type

    def _estimate_log_gaussian_prob(self, X, means, precisions_chol, covariance_type):
        """Estimate the log Gaussian probability.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)

        means : array-like, shape (n_components, n_features)

        precisions_chol : array-like
            Cholesky decompositions of the precision matrices.
            'full' : shape of (n_components, n_features, n_features)
            'tied' : shape of (n_features, n_features)
            'diag' : shape of (n_components, n_features)
            'spherical' : shape of (n_components,)

        covariance_type : {'full', 'tied', 'diag', 'spherical'}

        Returns
        -------
        log_prob : array, shape (n_samples, n_components)
        """
        n_samples, n_features = X.shape
        n_components, _ = means.shape
        # det(precision_chol) is half of det(precision)
        log_det = _compute_log_det_cholesky(
            precisions_chol, covariance_type, n_features)

        if covariance_type == 'full':
            log_prob = np.empty((n_samples, n_components))
            for k, (mu, prec_chol) in enumerate(zip(means, precisions_chol)):
                y = np.dot(X, prec_chol) - np.dot(mu, prec_chol)
                log_prob[:, k] = np.sum(np.square(y), axis=1)

        elif covariance_type == 'tied':
            log_prob = np.empty((n_samples, n_components))
            for k, mu in enumerate(means):
                y = np.dot(X, precisions_chol) - np.dot(mu, precisions_chol)
                log_prob[:, k] = np.sum(np.square(y), axis=1)

        elif covariance_type == 'diag':
            precisions = precisions_chol ** 2
            log_prob = (np.sum((means ** 2 * precisions), 1) -
                        2. * np.dot(X, (means * precisions).T) +
                        np.dot(X ** 2, precisions.T))

        elif covariance_type == 'spherical':
            precisions = precisions_chol ** 2
            log_prob = (np.sum(means ** 2, 1) * precisions -
                        2 * np.dot(X, means.T * precisions) +
                        np.outer(row_norms(X, squared=True), precisions))
        return -.5 * (n_features * np.log(2 * np.pi) + log_prob) + log_det

    def __initialize_model(self, X, resp=0):
        """Initialization of the Gaussian mixture parameters.

            Parameters
            ----------
            X : array-like, shape (n_samples, n_features)

            resp : array-like, shape (n_samples, n_components)
        """
        n_samples, _ = X.shape

        random_state = check_random_state(self.random_state)
        resp = random_state.rand(n_samples, self.n_components)
        resp /= resp.sum(axis=1)[:, np.newaxis]  # responsibilities

        weights, means, covariances = _estimate_gaussian_parameters(
            X, resp, self.reg_covar,
            self.covariance_type)  # weights = nk: the number of data samples in the current component.
        weights /= n_samples  # (weights/n)  means pi_k: mixing coefficients

        # self.weights_ = (weights if self.weights_init is None
        #                  else self.weights_init)
        # self.means_ = means if self.means_init is None else self.means_init

        self.weights_ = weights
        self.means_ = means
        self.precisions_init = None

        if self.precisions_init is None:
            self.covariances_ = covariances
            self.precisions_cholesky_ = _compute_precision_cholesky(
                covariances, self.covariance_type)
        elif self.covariance_type == 'full':
            self.precisions_cholesky_ = np.array(
                [linalg.cholesky(prec_init, lower=True)
                 for prec_init in self.precisions_init])
        elif self.covariance_type == 'tied':
            self.precisions_cholesky_ = linalg.cholesky(self.precisions_init,
                                                        lower=True)
        else:
            self.precisions_cholesky_ = self.precisions_init

    def fit(self, X='X_train', y_train=None):

        X_train = X
        self.__initialize_model(X_train)

        do_init = True
        lower_bound = (-np.infty if do_init else self.lower_bound_)

        for n_iter in range(1, self.max_iter + 1):
            prev_lower_bound = lower_bound

            log_prob_norm, log_resp = self._e_step(X_train)  # calculate resp
            self._m_step(X_train, log_resp)  # calculate parameters (pi, mu, sigma)
            lower_bound = self._compute_lower_bound(
                log_resp, log_prob_norm)

            change = lower_bound - prev_lower_bound
            # GaussianMixture(verbose=2)._print_verbose_msg_iter_end(n_iter, change)

            if abs(change) < self.tol:
                self.converged_ = True
                break

    def _e_step(self, X):
        """E step.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)

        Returns
        -------
        log_prob_norm : float
            Mean of the logarithms of the probabilities of each sample in X

        log_responsibility : array, shape (n_samples, n_components)
            Logarithm of the posterior probabilities (or responsibilities) of
            the point of each sample in X.
        """
        log_prob_norm, log_resp = self._estimate_log_prob_resp(X)
        return np.mean(log_prob_norm), log_resp

    def _m_step(self, X, log_resp):
        """M step.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)

        log_resp : array-like, shape (n_samples, n_components)
            Logarithm of the posterior probabilities (or responsibilities) of
            the point of each sample in X.
        """
        n_samples, _ = X.shape
        self.weights_, self.means_, self.covariances_ = (
            _estimate_gaussian_parameters(X, np.exp(log_resp), self.reg_covar,
                                          self.covariance_type))
        self.weights_ /= n_samples
        self.precisions_cholesky_ = _compute_precision_cholesky(
            self.covariances_, self.covariance_type)

    def _estimate_log_prob_resp(self, X):
        """Estimate log probabilities and responsibilities for each sample.

        Compute the log probabilities, weighted log probabilities per
        component and responsibilities for each sample in X with respect to
        the current state of the model.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)

        Returns
        -------
        log_prob_norm : array, shape (n_samples,)
            log p(X)

        log_responsibilities : array, shape (n_samples, n_components)
            logarithm of the responsibilities
        """
        weighted_log_prob = self._estimate_weighted_log_prob(X)
        log_prob_norm = logsumexp(weighted_log_prob, axis=1)
        with np.errstate(under='ignore'):
            # ignore underflow
            log_resp = weighted_log_prob - log_prob_norm[:, np.newaxis]
        return log_prob_norm, log_resp

    def _estimate_weighted_log_prob(self, X):
        """Estimate the weighted log-probabilities, log P(X | Z) + log weights.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)

        Returns
        -------
        weighted_log_prob : array, shape (n_samples, n_component)
        """
        return self._estimate_log_prob(X) + self._estimate_log_weights()

    def _estimate_log_prob(self, X):

        log_prob = _estimate_log_gaussian_prob(
            X, self.means_, self.precisions_cholesky_, self.covariance_type)
        return log_prob

        # # if train_flg:  # normalize to [0,1]
        # #     self.prob_min = np.min(np.exp(log_prob), axis=0)
        # #     self.prob_max = np.max(np.exp(log_prob), axis=0)
        # v= (np.exp(log_prob) - self.prob_min) / (self.prob_max-self.prob_min)  # (x-min) / (max-min)

        # return np.log(v)

    def _estimate_log_weights(self):
        return np.log(self.weights_)

    def _compute_lower_bound(self, _, log_prob_norm):
        return log_prob_norm

    def predict(self, X_test):
        # y_pred = self._estimate_weighted_log_prob(X_test).argmax(axis=1)  # predict the x belongs to which component.
        y_pred = np.zeros(X_test.shape[0])
        y_pred[self.predict_proba(X_test) < self.detect_thres] = 1  # 0 is normal, 1 is abnormal

        return y_pred

    def predict_proba(self, X_test):
        # Predict posterior probability of each component given the data.

        # _, log_resp = self._estimate_log_prob_resp(X_test) # predict the responsibility of the x
        # return np.exp(log_resp)

        ### calculate pdf of each samples _estimate_log_gaussian_prob

        log_guassian_pdf = self._estimate_weighted_log_prob(X_test)
        pdf = np.sum(np.exp(log_guassian_pdf), axis=1)
        stat_data(pdf.reshape(-1, 1))

        # self.detect_thres = get_percentile(pdf, percent=0.9)
        # print(f'detect_thres: {self.detect_thres}')
        percent = 0.9 * 100
        self.detect_thres = np.percentile(a=sorted(pdf, reverse=False), q=100 - percent)
        print(f'detect_thres: {self.detect_thres}')

        return pdf

    def test(self, X_test, y_test):
        y_pred = self.predict(X_test=X_test)

        cm = confusion_matrix(y_true=y_test, y_pred=y_pred)
        print(f'{cm}')


def get_percentile(pdf, percent=0.95):
    cusum = 0.0
    for v in sorted(pdf, reverse=True):

        cusum += v
        if cusum / sum(pdf) > percent:
            value = v
            break

    return value


def load_data(n_samples=300):
    # generate random sample, two components
    np.random.seed(0)

    # generate spherical data centered on (20, 20)
    shifted_gaussian = np.random.randn(n_samples, 2) + np.array([20, 20])

    # generate zero centered stretched Gaussian data
    C = np.array([[0., -0.7], [3.5, .7]])
    stretched_gaussian = np.dot(np.random.randn(n_samples, 2), C)

    # concatenate the two datasets into the final training set
    X = np.vstack([shifted_gaussian, stretched_gaussian])

    y = np.vstack([np.ones(n_samples) * 0, np.ones(n_samples)]).reshape(-1, )

    return X, y


#
# if __name__ == '__main__':
#     X_train, y_train = load_data(n_samples=300)
#
#     gmm = GMM(n_components=2)
#     gmm.train(X_train=X_train)
#
#     X_test, y_test = load_data(n_samples=200)
#     y_pred = gmm.predict(X_test=X_test)
#
#     cm = confusion_matrix(y_true=y_test, y_pred=y_pred)
#     print(f'{cm}')


def main_for_each_feature_set(norm_file='', anomaly_file='', test_size=0.3, random_state=42):
    """

    :param norm_file:
    :param anomaly_file:
    :param test_size:
    :param random_state:
    :return:
    """
    print('1) load data and split it to train set and test set with ratio: 7:3')
    X_train, y_train, X_test, y_test = load_and_split_data(norm_file=norm_file, anomaly_file=anomaly_file,
                                                           test_size=test_size, random_state=random_state)
    print(f'--- train set and test set --'
          f'\nX_train:{X_train.shape}, y_train:{Counter(y_train)}'
          f'\nX_test :{X_test.shape}, y_test :{Counter(y_test)}, in which, 0: normals and 1: anomalies.')

    if norm_flg:
        print('2) normalization (minmaxscaler)')
        train_scaler = MinMaxScaler()
        train_scaler.fit(X_train)
        X_train = train_scaler.transform(X_train)
        X_test = train_scaler.transform(X_test)

    print('3) train and test the best detection algorithm.')
    roc_dict = {}
    auc_dict = {}

    # ocsvm = OCSVM_Class()
    # ocsvm.train(X_train)
    # # dump(ocsvm, 'output_data/models_dumping/ocsvm_' + case + '.joblib')
    # # model = load('output_data/models_dumping/ocsvm_' + case + '.joblib')
    # ocsvm.test(X_test, y_test)
    #
    # roc_dict['ocsvm'] = {'y_true': y_test, 'y_scores': ocsvm.y_scores}
    # auc_dict['ocsvm'] = ocsvm.auc

    gmm = GMM(n_components=2)
    gmm.train(X_train)
    # dump(gmm, 'output_data/models_dumping/gmm_' + case + '.joblib')
    # model = load('output_data/models_dumping/gmm_' + case + '.joblib')
    gmm.test(X_test, y_test)

    roc_dict['gmm'] = {'y_true': y_test, 'y_scores': gmm.y_scores}
    auc_dict['gmm'] = gmm.auc

    return roc_dict, auc_dict


def main_for_auc():
    """
       "test_size, random_state and so on", all of them come from _config.py.
    :return:
    """
    print(f"\nstep 1. obtain different strength datasets.")
    different_strength_datasets_dict = OrderedDict()
    # strength_lst = [0.1, 0.2, 0.4, 0.8, 1]  # strength of outlier: weaker strengths, smaller feature values.
    strength_lst = [0.1, 0.2, 0.4, 0.8, 1]  # strength of outlier: weaker strengths, smaller feature values.
    for idx, strength_value in enumerate(strength_lst):
        strength_key = strength_value

        demo_flg = True
        if demo_flg:
            idx_features_lst = [random.randint(5, 20) for i in range(4 + idx)]
            print(f'idx:{idx}, strength_key: {strength_key}, proposed feature set, idx_features_lst:{idx_features_lst}')
            select_features_from_list(input_file='input_data/demo_dataset/proposed_features/normal_demo_dataset.txt',
                                      output_file=f'input_data/demo_dataset/proposed_features/normal_demo_dataset_{strength_key}.txt',
                                      features_lst=idx_features_lst)
            select_features_from_list(input_file='input_data/demo_dataset/proposed_features/anomaly_demo_dataset.txt',
                                      output_file=f'input_data/demo_dataset/proposed_features/anomaly_demo_dataset_{strength_key}.txt',
                                      features_lst=idx_features_lst)
            idx_features_lst = [random.randint(5, 20) for i in range(2 + idx)]
            print(
                f'idx:{idx}, strength_key: {strength_key}, traditional feature set, idx_features_lst:{idx_features_lst}')
            select_features_from_list(input_file='input_data/demo_dataset/traditional_features/normal_demo_dataset.txt',
                                      output_file=f'input_data/demo_dataset/traditional_features/normal_demo_dataset_{strength_key}.txt',
                                      features_lst=idx_features_lst)
            select_features_from_list(
                input_file='input_data/demo_dataset/traditional_features/anomaly_demo_dataset.txt',
                output_file=f'input_data/demo_dataset/traditional_features/anomaly_demo_dataset_{strength_key}.txt',
                features_lst=idx_features_lst)

        values_dict = OrderedDict(
            {'prop_set': {
                'normal_file': f'input_data/demo_dataset/proposed_features/normal_demo_dataset_{strength_key}.txt',
                'anomaly_file': f'input_data/demo_dataset/proposed_features/anomaly_demo_dataset_{strength_key}.txt'},
                'trad_set': {
                    'normal_file': f'input_data/demo_dataset/traditional_features/normal_demo_dataset_{strength_key}.txt',
                    'anomaly_file': f'input_data/demo_dataset/traditional_features/anomaly_demo_dataset_{strength_key}.txt'}})

        different_strength_datasets_dict[strength_key] = values_dict

    print(f"\nstep 2. calculate auc under the corresponding strength data_process.")
    all_auc_dicts_lst = []
    for idx, (strength_key, values) in enumerate(different_strength_datasets_dict.items()):
        print(f"\n- strength of outiler: {strength_key}")
        input_files_dict = values
        # roc_dicts_lst = []
        auc_dicts_dict = OrderedDict()
        for ith, (feature_set_key, value_dict) in enumerate(input_files_dict.items()):
            """
                obtain roc_dict and auc_dict on different feature sets with the same (attack) strength of outiler.
            """
            print(
                f'\n-- ith:{ith}: evaluation on {feature_set_key} by the best detection algorithm under the same strength of outlier ({strength_key}).')
            roc_dict, auc_dict = main_for_each_feature_set(
                norm_file=value_dict['normal_file'],
                anomaly_file=value_dict['anomaly_file'],
                test_size=test_size, random_state=random_state)

            # roc_dicts_lst.append([key, roc_dict])
            auc_dicts_dict[feature_set_key] = auc_dict

        all_auc_dicts_lst.append([strength_key, auc_dicts_dict])

    print(f"\nstep 3. plot auc.")
    plot_auc_and_strength_of_outiler(all_auc_dicts_lst, out_file='output_data/figures/auc_on_different_strengths.pdf',
                                     title='AUC')


if __name__ == '__main__':
    main_for_auc()

#
