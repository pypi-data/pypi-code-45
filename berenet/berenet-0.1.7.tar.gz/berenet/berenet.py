import pickle as pickle

from berenet.base import Base, Layer, np, shuffle, warnings, logging

class BereNet(Base):
	def __init__(self, layers, functions=[Base.LOGISTIC], biases=[1]):
		super().__init__(layers)

		assert len(functions) > 0, 'Must specify at least one activation function'
		assert len(biases) == 0 or len(biases) == 1 or len(biases) == len(layers) or len(biases) == len(layers) - 1, 'Biases list must either be empty (for default), 1 integer long (to apply to all layers), or 1 value for each layer (output does not take a bias)'

		if len(functions) == 1:
			functions = functions * len(layers)
			functions[0] = Base.IDENTITY
		else:
			assert len(functions) == len(layers), 'Must have a function for every layer'

		if len(biases) == 0:
			biases = [0] * (len(layers) - 1)
		elif len(biases) == 1:
			biases = biases * (len(layers) - 1)

		input_layer = Layer(layers[0], layers[1], function=functions[0], bias=biases[0])

		self._layers.append(input_layer)

		for i in range(1, len(layers) - 1):
			layer = Layer(layers[i], layers[i+1], function=functions[i], bias=biases[i])
			self._layers.append(layer)

		output_layer = Layer(layers[-2], layers[-1], is_output=True, function=functions[-1])

		self._layers.append(output_layer)

	def predict(self, X, softmax_output=False, round=None):
		for i in range(0, len(self._layers) - 1):
			X = self._layers[i].forward_pass(X)

		output = self._layers[-1].forward_pass(X)

		if softmax_output:
			Layer.softmax(output)

		if round is not None:
			output = np.around(output, decimals=round)

		return output

	def _back_propogate(self, output, target, learning_rate, momentum, l2_regularizer):
		self._layers[-1].D = ((output - target) * self._layers[-1].Fp).T

		for i in range(len(self._layers) - 2, 0, -1):
			if self._layers[i].bias:
				W_nobias = self._layers[i].W[:-self._layers[i].bias]
			else:
				W_nobias = self._layers[i].W

			self._layers[i].D = W_nobias.dot(self._layers[i+1].D) * self._layers[i].Fp.T

		self._update_weights(learning_rate, momentum, l2_regularizer)

	def _update_weights(self, eta, momentum, l2_regularizer):
		for i in range(0, len(self._layers) - 1):
			gradient = eta * (self._layers[i+1].D.dot(self._layers[i].Z)).T

			if momentum != 0:
				if len(self._previous_gradients) <= i:
					self._previous_gradients.append(gradient)
				else:
					gradient += momentum * self._previous_gradients[i]
					self._previous_gradients[i] = gradient

			if l2_regularizer != 0:
				l2_regularization = self._layers[i].W * l2_regularizer
				bias_row = l2_regularization.shape[0] - self._layers[i].bias
				l2_regularization[bias_row, :] = 0.

				gradient += l2_regularization

			self._layers[i].W -= gradient

			prev_gradient = gradient

	def _mean_squared_error(self, output, target):
		return ((target - output) ** 2) / 2

	def train(self, training_data, training_targets, learning_rate, epochs,
		validation_data=None, validation_targets=None, minibatch_size=1, momentum=0, bold_driver=False,
		annealing_schedule=0, l2_regularizer=0, summarize=False):
		data_divided, targets_divided = self._divide_data(training_data, training_targets, minibatch_size)

		num_samples = len(data_divided)

		indices = list(range(num_samples))

		del self._previous_gradients[:]

		if bold_driver and num_samples > 1:
			warnings.warn('Bold driver is an adaptation technique for the learning rate designed for full-batch learning.\
				It is not recommended to use it for mini-batch learning as it will likely confuse the algorithm,\
				resulting in poor performance')

		prev_mse = None

		if validation_data is not None and validation_targets is not None:
			mse_measure_data_small = validation_data[:100]
			mse_measure_targets_small = validation_targets[:100]
			mse_measure_data = validation_data
			mse_measure_targets = validation_targets
		else:
			mse_measure_data_small = training_data[:100]
			mse_measure_targets_small = training_targets[:100]
			mse_measure_data = training_data
			mse_measure_targets = training_targets

		if summarize:
			self.print_summary(training_data, learning_rate, epochs)

		for i in range(epochs):
			if 'e' in self.verbosity: logging.info('Epoch: {}'.format(i))

			shuffle(indices)

			for index in range(num_samples):
				if 'n' in self.verbosity: logging.info('Minibatch: {} out of {}'.format(index, num_samples))

				random_index = indices[index]

				output = self.predict(data_divided[random_index])
				self._back_propogate(output, targets_divided[random_index], learning_rate, momentum, l2_regularizer)

			if 'm' in self.verbosity:
				self._update_mse(mse_measure_data_small, mse_measure_targets_small)
				self._m()

			if bold_driver:
				if not 'm' in self.verbosity:
					self._update_mse(mse_measure_data_small, mse_measure_targets_small)

				if prev_mse is None:
					prev_mse = self.mse
				else:
					if self.mse < prev_mse:
						learning_rate *= 1.03
					elif self.mse - prev_mse >= (10 ** -10):
						learning_rate *= 0.5

			if annealing_schedule != 0:
				learning_rate = learning_rate / (1 + i / float(annealing_schedule))

		self._update_mse(mse_measure_data, mse_measure_targets)

		if 'm' in self.verbosity: self._m()

	def _update_mse(self, validation_data, validation_targets):
		prediction = self.predict(validation_data)
		mean_squared_error = self._mean_squared_error(prediction, validation_targets)
		self.mse = np.linalg.norm(mean_squared_error)