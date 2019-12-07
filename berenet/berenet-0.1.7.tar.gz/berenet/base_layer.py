import numpy as np

class BaseLayer(object):
	FUNCTIONS = (		# range of functions
		'identity',		# (-inf, inf)
		'logistic',		# [0, 1]
		'tanh',			# (-1, 1)
		'arctan',		# (-pi/2, pi/2)
		'softsign',		# (-1, 1)
		'relu',			# [0, inf)
	)

	def _activate(self, X):
		if self.function == self.FUNCTIONS[0]:
			return self._identity(X)
		elif self.function == self.FUNCTIONS[1]:
			return self._logistic(X)
		elif self.function == self.FUNCTIONS[2]:
			return self._tanh(X)
		elif self.function == self.FUNCTIONS[3]:
			return self._arctan(X)
		elif self.function == self.FUNCTIONS[4]:
			return self._softsign(X)
		elif self.function == self.FUNCTIONS[5]:
			return self._relu(X)

	def _relu(self, X):
		X[X < 0] = 0
		derivative_values = X > 0

		activated = X
		derivative = np.copy(X)
		derivative[derivative_values] = 1

		return activated, derivative

	def _softsign(self, X):
		activated = X / (1 + np.absolute(X))
		derivative = 1 / ((1 + np.absolute(X)) ** 2)

		return activated, derivative

	def _arctan(self, X):
		activated = np.arctan(X)
		derivative = 1 / (X ** 2 + 1)

		return activated, derivative

	def _tanh(self, X):
		activated = 2 / (1 + np.exp(-2 * X)) - 1
		derivative = 1 - activated ** 2

		return activated, derivative

	def _logistic(self, X):
		activated = 1 / (1 + np.exp(-X))
		derivative = activated * (1 - activated)

		return activated, derivative

	# Doesn't work for gradient descent so its not used
	def _binary_step(self, X):
		X[X >= 0] = 1.
		X[X < 0] = 0

		activated = X
		derivative = np.zeros(X.shape)

		return activated, derivative

	def _identity(self, X):
		activated = X
		derivative = np.ones(X.shape)

		return activated, derivative