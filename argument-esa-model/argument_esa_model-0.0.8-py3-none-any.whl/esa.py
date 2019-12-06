import pickle
import numpy as np
from scipy import sparse
import sys
from argument_esa_model.similarity import Similarity
from argument_esa_model.preprocessor import Preprocessor
import argument_esa_model.matrix
sys.modules['matrix'] = argument_esa_model.matrix

class ESA:

	def __init__(self, matrix_path, similarity = "cos"):
		self._pre = Preprocessor()
		self._mat = pickle.load(open(matrix_path, "rb"))
		self._sim = Similarity(self._mat.get_terms(), similarity)


	def process(self, document, word_level = False):
		if not word_level:
			return self._process_document(document)
		else:
			return self._process_words(document)


	def _process_document(self, document):
		document_vec = self._to_vector(document)
		result = {}
		for concept in self._mat.get_concepts():
			result[concept] = self._sim.compute_similarity(document_vec, self._mat[concept])
		return result


	def _process_words(self, document):
		results = {}
		terms = self._mat.get_terms()
		for word in self._pre.to_bow(document):
			if word in terms:
				vec = sparse.lil_matrix(np.zeros((len(terms), 1), dtype = np.longdouble))
				vec[terms.index(word), 0] = 1.0
				vec = sparse.csc_matrix(vec)
				vec.eliminate_zeros()
				intermediate = {}
				for concept in self._mat.get_concepts():
					intermediate[concept] = self._sim.compute_similarity(vec, self._mat[concept])
				intermediate = sorted(intermediate.items(), key = lambda x : x[1], reverse = True)
				results[word] = intermediate[0][0]
		return results


	def _to_vector(self, document):
		bow = self._pre.to_bow(document)
		terms = self._mat.get_terms()
		length = sum(bow.values())
		vec = sparse.lil_matrix(np.zeros((len(terms), 1), dtype = np.longdouble))
		for term in bow:
			if term in terms:
				vec[terms.index(term), 0] = bow[term] / length
		vec = sparse.csc_matrix(vec)
		vec.eliminate_zeros()
		return vec