import pandas as pd
import re
import math
from collections import Counter
from scipy import sparse
import numpy as np

class Preprocessor:


	def __init__(self):
		pass

	def preprocess(self, input):
		df = pd.read_csv(input)
		preprocessed = {}
		for i, r in df.iterrows():
			preprocessed[r["concept"]] = self.to_bow(r["text"])
		return preprocessed


	def tokenize(self, text):
		text = text.lower()
		text = text.replace("\n", " ").replace("\r", " ")
		text = re.sub(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", " ", text)
		text = re.sub("[^A-Za-z]+", " ", text).replace("  ", " ")
		return [word.strip() for word in text.split(" ") if not len(word) < 3]


	def to_bow(self, text):
		return dict(Counter(self.tokenize(text)))