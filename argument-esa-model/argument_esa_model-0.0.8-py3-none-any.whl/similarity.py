#import gensim
import numpy as np
import sklearn.metrics.pairwise as sk
from scipy import sparse
from scipy.sparse.linalg import norm



class Similarity:


    def __init__(self, terms, similarity):
        self._terms = terms
        self._similarity = similarity


    def compute_similarity(self, x, y):
        if self._similarity == "cos":
            return self._cosine_similarity(x, y)
        elif self._similarity == "avg":
            return self._average_similarity(x, y)
        elif self._similarity == "max":
            return self._maximum_matching_similarity(x, y)
        else:
            raise ValueError


    def _cosine_similarity(self, x, y):
        return sk.cosine_similarity(x.transpose().todense(), y.transpose().todense())[0,0]


    def _average_similarity(self, x, y):
        '''
        x.eliminate_zeros()
        y.eliminate_zeros()
        similarity = 0.0
        for i in x.indices:
            for j in y.indices:
                similarity += (x[i] * y[j])[0, 0] * self.term_similarity(self._terms[i], self._terms[j], self.rbf_kernel)
        similarity /= len(x.indices) * len(y.indices) * norm(x) * norm(y)
        return similarity
        '''
        raise NotImplementedError


    def _maximum_matching_similarity(self, x, y):
        '''
        x.eliminate_zeros()
        y.eliminate_zeros()
        similarity = 0.0
        for i in x.indices:
            max_similarity = 0.0
            index = 0 
            for j in y.indices:
                current_similarity = self.term_similarity(self._terms[i], self._terms[j], self.cosine_sim)
                if current_similarity > max_similarity:
                    max_similarity = current_similarity
                    index = j
                if max_similarity >= 1.0:
                    break
                else:
                    continue
            similarity += (x[i] * y[index])[0, 0] * max_similarity
        similarity /= norm(x) * norm(y)
        return similarity
        '''
        raise NotImplementedError


'''
    def term_similarity(self, a, b, similarity):
        if a == b:
            return 1.0
        w2v_a = self.word2vec(a)
        w2v_b = self.word2vec(b)
        if w2v_a is None or w2v_b is None:
            return 0.0
        return similarity(w2v_a, w2v_b)


    def word2vec(self, w):
        try:
            word_vector = self._model[w]
            word_vector.shape = (-1, 300)
            return word_vector
        except:
            return None


    def cosine_sim(self, x, y):
        return sk.cosine_similarity(x, y)[0, 0]


    def rbf_kernel(self, x, y):
        return np.exp(-1.0 * (np.linalg.norm(x - y) * np.linalg.norm(x - y)) / \
                        (0.03 * np.linalg.norm(x) * np.linalg.norm(y)))
'''


'''
class TermSimilarityMatrix:

    def __init__(self, terms, matrix):
        self._terms = terms
        self._mat = matrix
      
    def __getitem__(self, term_1, term_2):
        try:
            i = self._terms.index(term_1)
            j = self._terms.index(term_2)
            try:
                return self._mat[i, j]
            except:
                return self._mat[j, i]
        except:
            raise KeyError
'''

