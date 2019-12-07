import numpy as np

from berenet.base_layer import BaseLayer
from copy import deepcopy

class RecurrentLayer(BaseLayer):
	def __init__(self, inputs, outputs, recurrent=True, is_output=False, bias=1, function=BaseLayer.FUNCTIONS[1]):
		assert function in super().FUNCTIONS, 'Invalid function, please make sure it\'s one of: ' + str(super().FUNCTIONS)

		self.Fp = list()
		self.Y = list()

		self.D = list()

		self.inputs = inputs
		self.outputs = outputs
		self.is_output = is_output
		self.recurrent = recurrent
		self.function = function
		self.bias = bias

		if not is_output:
			if bias:
				self.W = np.random.normal(size=(inputs + bias, outputs), scale=1E-4)
			else:
				self.W = np.random.normal(size=(inputs, outputs), scale=1E-4)
		else:
			self.bias = False

		if recurrent:
			self.RW = np.random.normal(size=(1, inputs), scale=1E-4)
			self.recurrentD = list()

	def forward_pass(self, X):
		if len(self.Y) > 0 and self.recurrent:
			if self.bias:
				X += self.RW * self.Y[-1][:,:-self.bias]
			else:
				X += self.RW * self.Y[-1]

		activation = self._activate(X)
		activated_output = activation[0]

		if self.bias:
			activated_output = np.ones(shape=(activation[0].shape[0], activation[0].shape[1] + self.bias))
			activated_output[:,:-self.bias] = activation[0]

		self.Y.append(activated_output)
		self.Fp.append(activation[1])

		if self.is_output:
			return activation[0]

		return np.dot(activated_output, self.W)

	def reset(self):
		del self.Fp[:]
		del self.Y[:]

		self.clear_deltas()

	def clear_deltas(self):
		del self.D[:]

		if self.recurrent:
			del self.recurrentD[:]

	@staticmethod
	def softmax(X):		
		for i in range(X.shape[0]):
			e_x = np.exp(X[i] - np.max(X[i]))
			X[i] = e_x / e_x.sum()