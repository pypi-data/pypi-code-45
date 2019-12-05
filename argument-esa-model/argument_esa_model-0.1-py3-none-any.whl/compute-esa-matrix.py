#!/usr/bin/env python3

import pickle

from matrix import ESAMatrix
from preprocessor import Preprocessor


def main():
	for corpus in ["strategic-intelligence", "debatepedia"]:
		corpus_path = "../../resources/" + corpus + ".csv"
		matrix_path = "../../resources/" + corpus + ".mat"
		p = Preprocessor()
		preprocessed = p.preprocess(corpus_path)
		concepts = tuple(preprocessed.keys())
		bows = tuple([preprocessed[bow] for bow in preprocessed])
		terms = tuple(set([word for bow in bows for word in bow]))
		mat = ESAMatrix(terms, concepts, bows)
		pickle.dump(mat, open(matrix_path, "wb"))


if __name__ == "__main__":
	main()