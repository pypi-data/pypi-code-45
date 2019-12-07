import numpy as np

from berenet.base_layer import BaseLayer

class Layer(BaseLayer):
	def __init__(self, inputs, outputs, is_output=False, bias=1, function=BaseLayer.FUNCTIONS[0]):
		assert function in super().FUNCTIONS, 'Invalid function, please make sure it\'s one of: ' + str(super().FUNCTIONS)

		self.S = None
		self.Z = None
		self.Fp = None
		self.W = None
		self.D = None

		if not is_output:
			if bias:
				self.W = np.random.normal(size=(inputs + bias, outputs), scale=1E-4)
			else:
				self.W = np.random.normal(size=(inputs, outputs), scale=1E-4)

		self.inputs = inputs
		self.outputs = outputs
		self.function = function
		self.is_output = is_output
		self.bias = bias

	def forward_pass(self, X):
		self.S = X

		self.Z, self.Fp = self._activate(self.S)

		if not self.is_output and self.bias:
			self.Z = np.append(self.Z, np.ones((self.Z.shape[0], self.bias)), axis=1)

		if self.is_output:
			return self.Z
		else:
			return self.Z.dot(self.W)

	@staticmethod
	def softmax(X):
		for i in xrange(X.shape[0]):
			total = np.sum(X[i])

			for j in xrange(X.shape[1]):
				X[i][j] = np.exp(X[i][j]) / np.exp(total)