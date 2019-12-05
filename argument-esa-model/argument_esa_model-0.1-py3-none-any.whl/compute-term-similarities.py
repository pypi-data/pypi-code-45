#!/usr/bin/env python3
'''
import pickle
import gensim
import numpy as np
from scipy import sparse


from similarity import TermSimilarityMatrix
from preprocessor import Preprocessor


def main():
	model_path = "../../resources/GoogleNews-vectors-negative300.bin"
	model = gensim.models.keyedvectors.KeyedVectors.load_word2vec_format(model_path, binary = True)

	for corpus in ["debatepedia", "strategic-intelligence"]:
		corpus_path = "../../resources/" + corpus + ".csv"
		similarities_path = "../../resources/" + corpus + ".sim"

		p = Preprocessor()
		preprocessed = p.preprocess(corpus_path)
		bows = tuple([preprocessed[bow] for bow in preprocessed])
		terms = tuple(set([word for bow in bows for word in bow]))

		#compute terms in model
		terms_in_model = []
		for term in terms:
			try:
				model.get_vector(term)
				terms_in_model.append(term)
			except:
				pass
		terms_in_model = tuple(terms_in_model)

		#compute similarities
		matrix = sparse.lil_matrix(np.zeros((len(terms_in_model), len(terms_in_model))), dtype = np.single)
		sim = model.similarity
		for i in range(0, len(terms_in_model)):
			term_1 = terms_in_model[i]
			for j in range(0, len(terms_in_model) - i):
				term_2 = terms_in_model[j]
				matrix[i, j] = sim(term_1, term_2)
			print(i)
		matrix.eliminate_zeros()
		matrix = matrix.to_dok()

		mat = TermSimilarityMatrix(terms_in_model, matrix)
		pickle.dump(mat, open(matrix_path, "wb"))
'''

if __name__ == "__main__":
	pass
	#main()