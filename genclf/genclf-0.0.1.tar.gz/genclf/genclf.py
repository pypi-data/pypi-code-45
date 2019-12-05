# Core Pkgs

import os,joblib
import warnings
warnings.filterwarnings('ignore')

PACKAGE_DIR = os.path.dirname(__file__)

class GenderClassifier(object):
	"""GenderClassifier"""
	def __init__(self, name=None):
		super(GenderClassifier, self).__init__()
		self.name = name

	def __repr__(self):
		return 'GenderClassifier(name={})'.format(self.name)

	def predict(self):
		# Load Vectorizer
		gender_vectorizer = open(os.path.join(PACKAGE_DIR,"models/gender_vectorizer.pkl"),"rb")
		gender_cv = joblib.load(gender_vectorizer)

		# Load Models
		gender_nb_model = open(os.path.join(PACKAGE_DIR,"models/gender_nv_model.pkl"),"rb")
		gender_clf = joblib.load(gender_nb_model)
		# Vectorization

		vectorized_data = gender_cv.transform([self.name]).toarray()
		prediction = gender_clf.predict(vectorized_data)

		if prediction[0] == 0:
			result = 'female'
		elif prediction[0] == 1:
			result = 'male'

		return result

	def load(self,model_type):
		if model_type == 'nb':
			# Load Models
			gender_nb_model = open(os.path.join(PACKAGE_DIR,"models/gender_nv_model.pkl"),"rb")
			gender_clf = joblib.load(gender_nb_model)
		elif model_type == 'logit':
			gender_logit_model = open(os.path.join(PACKAGE_DIR,"models/gender_logit_model.pkl"),"rb")
			gender_clf = joblib.load(gender_logit_model)

		else:
			print("Please Choice A Model [nb:naive bayes,logit:logisticRegression")

		return gender_clf

	def classify(self,new_name):
		self.name = new_name
		result = self.predict()
		return result

	def is_female(self,new_name):
		self.name = new_name
		result = self.predict()
		return result == 'female'

	def is_male(self,new_name):
		self.name = new_name
		result = self.predict()
		return result == 'male'
			