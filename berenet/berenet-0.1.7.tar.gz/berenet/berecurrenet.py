from berenet.base import Base, np, shuffle, warnings, logging
from berenet.recurrent_layer import RecurrentLayer

class BerecurreNet(Base):
	def __init__(self, layers, functions=[Base.LOGISTIC], recurrent_layers=[], biases=[1]):
		super().__init__(layers)

		assert len(recurrent_layers) == 0 or len(recurrent_layers) == len(layers), 'Must specify recurrence for each layer'
		assert len(functions) == 1 or len(functions) == len(layers), 'Must specify one activation function (to apply to all layers), or one function for each layer'
		assert len(biases) == 0 or len(biases) == 1 or len(biases) == len(layers) or len(biases) == len(layers) - 1, 'Biases list must either be empty (for default), 1 integer long (to apply to all layers), or 1 value for each layer (output does not take a bias)'

		if len(functions) == 1:
			functions = functions * len(layers)
			functions[0] = BerecurreNet.IDENTITY

		if len(recurrent_layers) == 0:
			recurrent_layers = [True] * len(layers)
			recurrent_layers[0] = False
			recurrent_layers[-1] = False

		if len(biases) == 0:
			biases = [0] * (len(layers) - 1)
		elif len(biases) == 1:
			biases = biases * (len(layers) - 1)

		self._layers = list()

		input_layer = RecurrentLayer(layers[0], layers[1], recurrent=recurrent_layers[0], bias=biases[0], function=functions[0])

		self._layers.append(input_layer)

		for i in range(1, len(layers) - 1):
			layer = RecurrentLayer(layers[i], layers[i+1], recurrent=recurrent_layers[i], bias=biases[i], function=functions[i])
			self._layers.append(layer)

		output_layer = RecurrentLayer(layers[-1], None, recurrent=recurrent_layers[-1], is_output=True, function=functions[-1])

		self._layers.append(output_layer)

	def predict(self, data, reset=False, softmax_output=False, round_digits=None):
		if reset:
			for layer in self._layers:
				layer.reset()

		time_steps = data.shape[0]

		data = data.astype(np.float64)

		predictions = list()

		for time_step in range(time_steps):
			X = data[time_step]
			
			if len(X.shape) == 1:
				X = X.reshape(1, X.shape[0])
			else:
				X = data[time_step]

			for layer in self._layers:
				X = layer.forward_pass(X)

			if softmax_output:
				RecurrentLayer.softmax(X)

			if round_digits is not None:
				X = np.around(X, decimals=round_digits)

			predictions.append(X)

		return np.array(predictions)

	def _forward_pass(self, data, reset=False):
		if reset:
			for layer in self._layers:
				layer.reset()

		time_steps = data.shape[0]

		data = data.astype(np.float64)

		for time_step in range(time_steps):
			X = data[time_step]
			
			if len(X.shape) == 1:
				X = X.reshape(1, X.shape[0])
			else:
				X = data[time_step]

			for layer in self._layers:
				X = layer.forward_pass(X)

	def _back_propogate_through_time_exp(self, epochs, training_data, targets, learning_rate, print_error=False):
		targets = targets.astype(np.float64)

		num_layers = len(self._layers)
		time_steps = targets.shape[0]

		for epoch in range(epochs):
			update_matrices = list()

			self._forward_pass(training_data, reset=True)

			for layer in self._layers:
				layer.clear_deltas()

			for layer in self._layers:
				weights = {}

				if layer.recurrent:
					weights['RW'] = np.zeros(layer.RW.shape)

				if not layer.output:
					weights['W'] = np.zeros(layer.W.shape)

				update_matrices.append(weights)

			error1 = 0

			for time_step in range(time_steps):
				delta = 0

				for layer_index in range(num_layers - 1, -1, -1):
					if self._layers[layer_index].output:
						if len(targets[time_step].shape) == 1:	
							reshaped_targets = targets[time_step].reshape(targets[time_step].shape[0], 1)
						else:
							reshaped_targets = targets[time_step].T

						output = self._layers[layer_index].Y[time_step].reshape(reshaped_targets.shape)

						dE_dout = output - reshaped_targets
						dout_din = self._layers[layer_index].Fp[time_step].T

						dE_din = dE_dout * dout_din

						delta = dE_din

						error1 += 0.5 * dE_dout**2
					else:
						dE_dW = delta.dot(self._layers[layer_index].Y[time_step]).T

						update_matrices[layer_index]['W'] += dE_dW

						dE_dout = self._layers[layer_index].W.dot(delta).T

						if self._layers[layer_index].bias:
							dE_dout = dE_dout[:,:-self._layers[layer_index].bias]

						delta = (dE_dout * self._layers[layer_index].Fp[time_step]).T

					if time_step > 0 and self._layers[layer_index].recurrent:
						recurrent_delta = np.copy(delta.T)

						for i in range(time_step, 0, -1):
							if self._layers[layer_index].bias:
								dE_dRW = recurrent_delta * self._layers[layer_index].Y[i - 1][:,:-self._layers[layer_index].bias]
							else:
								dE_dRW = recurrent_delta * self._layers[layer_index].Y[i - 1]						

							update_matrices[layer_index]['RW'] += dE_dRW.sum(axis=0)

							recurrent_delta *= self._layers[layer_index].RW * self._layers[layer_index].Fp[i - 1]

			for layer_index in range(num_layers):
				if not self._layers[layer_index].output:
					self._layers[layer_index].W -= learning_rate * update_matrices[layer_index]['W']

				if self._layers[layer_index].recurrent:
					self._layers[layer_index].RW -= learning_rate * update_matrices[layer_index]['RW']

			self._forward_pass(training_data, reset=True)

			error = 0

			for time_step in range(time_steps):
				delta = 0

				if self._layers[-1].output:
					if len(targets[time_step].shape) == 1:	
						reshaped_targets = targets[time_step].reshape(targets[time_step].shape[0], 1)
					else:
						reshaped_targets = targets[time_step].T

					output = self._layers[-1].Y[time_step].reshape(reshaped_targets.shape)

					error += 0.5 * (output - reshaped_targets)**2

			prev_mul = 2
			mul = 0

			diff_greater_than = None

			count = 0
			max_count = 10

			for layer_index in range(num_layers):
				if not self._layers[layer_index].output:
					self._layers[layer_index].W += learning_rate * update_matrices[layer_index]['W']

				if self._layers[layer_index].recurrent:
					self._layers[layer_index].RW += learning_rate * update_matrices[layer_index]['RW']

				if not self._layers[layer_index].output:
					self._layers[layer_index].W -= (prev_mul * learning_rate) * update_matrices[layer_index]['W']

				if self._layers[layer_index].recurrent:
					self._layers[layer_index].RW -= (prev_mul * learning_rate) * update_matrices[layer_index]['RW']

			while count < max_count:
				self._forward_pass(training_data, reset=True)

				error2 = 0

				for time_step in range(time_steps):
					delta = 0

					if self._layers[-1].output:
						if len(targets[time_step].shape) == 1:	
							reshaped_targets = targets[time_step].reshape(targets[time_step].shape[0], 1)
						else:
							reshaped_targets = targets[time_step].T

						output = self._layers[-1].Y[time_step].reshape(reshaped_targets.shape)

						error2 += 0.5 * (output - reshaped_targets)**2

				for layer_index in range(num_layers):
					if not self._layers[layer_index].output:
						self._layers[layer_index].W += (prev_mul * learning_rate) * update_matrices[layer_index]['W']

					if self._layers[layer_index].recurrent:
						self._layers[layer_index].RW += (prev_mul * learning_rate) * update_matrices[layer_index]['RW']

				if count < max_count - 1:
					diff = np.linalg.norm(error) - np.linalg.norm(error2)

					# print(diff)

					if abs(diff) <= 1E-5 or mul == 1 or mul == prev_mul or prev_mul <= 1E-5:
						break
					elif diff > 0:
						# if top == 2:
						# 	mul += 0.1
						# top = 1
						# prev_mul *= (2-mul)

						prev_mul *= 2
					else:
						# if top == 1:
						# 	mul += 1
						# top = 2
						# prev_mul /= (2-mul)

						prev_mul /= 1.8

					for layer_index in range(num_layers):
						if not self._layers[layer_index].output:
							self._layers[layer_index].W -= (prev_mul * learning_rate) * update_matrices[layer_index]['W']

						if self._layers[layer_index].recurrent:
							self._layers[layer_index].RW -= (prev_mul * learning_rate) * update_matrices[layer_index]['RW']

				count += 1

			for layer_index in range(num_layers):
				if not self._layers[layer_index].output:
					self._layers[layer_index].W -= ((learning_rate * update_matrices[layer_index]['W']) + (prev_mul * learning_rate * update_matrices[layer_index]['W'])) / 2.

				if self._layers[layer_index].recurrent:
					self._layers[layer_index].RW -= ((learning_rate * update_matrices[layer_index]['RW']) + (prev_mul * learning_rate * update_matrices[layer_index]['RW'])) / 2.

			self._forward_pass(training_data, reset=True)
			error2 = 0

			for time_step in range(time_steps):
				delta = 0

				if self._layers[-1].output:
					if len(targets[time_step].shape) == 1:	
						reshaped_targets = targets[time_step].reshape(targets[time_step].shape[0], 1)
					else:
						reshaped_targets = targets[time_step].T

					output = self._layers[-1].Y[time_step].reshape(reshaped_targets.shape)

					error2 += 0.5 * (output - reshaped_targets)**2

			if np.linalg.norm(error) < np.linalg.norm(error2):
				for layer_index in range(num_layers):
					if not self._layers[layer_index].output:
						self._layers[layer_index].W += ((learning_rate * update_matrices[layer_index]['W']) + (prev_mul * learning_rate * update_matrices[layer_index]['W'])) / 2.

					if self._layers[layer_index].recurrent:
						self._layers[layer_index].RW += ((learning_rate * update_matrices[layer_index]['RW']) + (prev_mul * learning_rate * update_matrices[layer_index]['RW'])) / 2.

				for layer_index in range(num_layers):
					if not self._layers[layer_index].output:
						self._layers[layer_index].W -= learning_rate * update_matrices[layer_index]['W']

					if self._layers[layer_index].recurrent:
						self._layers[layer_index].RW -= learning_rate * update_matrices[layer_index]['RW']

			if print_error and epoch % print_error == 0:
				logging.info('MSE: {}'.format(np.linalg.norm(error)))

	def _back_propogate_through_time(self, targets, learning_rate, momentum, print_error=False):
		targets = targets.astype(np.float64)
		update_matrices = list()

		num_layers = len(self._layers)
		time_steps = targets.shape[0]

		for layer in self._layers:
			layer.clear_deltas()

		for layer in self._layers:
			weights = {}

			if layer.recurrent:
				weights['RW'] = np.zeros(layer.RW.shape)

			if not layer.is_output:
				weights['W'] = np.zeros(layer.W.shape)

			update_matrices.append(weights)

		error = 0

		for time_step in range(time_steps):
			delta = 0

			for layer_index in range(num_layers - 1, -1, -1):
				if self._layers[layer_index].is_output:
					if len(targets[time_step].shape) == 1:	
						reshaped_targets = targets[time_step].reshape(targets[time_step].shape[0], 1)
					else:
						reshaped_targets = targets[time_step].T

					output = self._layers[layer_index].Y[time_step].reshape(reshaped_targets.shape)

					error += 0.5 * (output - reshaped_targets)**2

					dE_dout = output - reshaped_targets
					dout_din = self._layers[layer_index].Fp[time_step].T

					dE_din = dE_dout * dout_din

					delta = dE_din
				else:
					dE_dW = delta.dot(self._layers[layer_index].Y[time_step]).T

					update_matrices[layer_index]['W'] += dE_dW

					dE_dout = self._layers[layer_index].W.dot(delta).T

					if self._layers[layer_index].bias:
						dE_dout = dE_dout[:,:-self._layers[layer_index].bias]

					delta = (dE_dout * self._layers[layer_index].Fp[time_step]).T

				if time_step > 0 and self._layers[layer_index].recurrent:
					recurrent_delta = np.copy(delta.T)

					for i in range(time_step, 0, -1):
						if self._layers[layer_index].bias:
							dE_dRW = recurrent_delta * self._layers[layer_index].Y[i - 1][:,:-self._layers[layer_index].bias]
						else:
							dE_dRW = recurrent_delta * self._layers[layer_index].Y[i - 1]						

						update_matrices[layer_index]['RW'] += dE_dRW.sum(axis=0)

						recurrent_delta *= self._layers[layer_index].RW * self._layers[layer_index].Fp[i - 1]

		for layer_index in range(num_layers):
			if not self._layers[layer_index].is_output:
				update_matrices[layer_index]['W'] *= learning_rate

				if momentum and len(self._previous_gradients) > 0:
					update_matrices[layer_index]['W'] += momentum * self._previous_gradients[layer_index]['W']

				self._layers[layer_index].W -= update_matrices[layer_index]['W']

			if self._layers[layer_index].recurrent:
				update_matrices[layer_index]['RW'] *= learning_rate

				if momentum and len(self._previous_gradients) > 0:
					update_matrices[layer_index]['RW'] += momentum * self._previous_gradients[layer_index]['RW']

				self._layers[layer_index].RW -= update_matrices[layer_index]['RW']

		if momentum:
			self._previous_gradients = deepcopy(update_matrices)

		if print_error:
			logging.info('MSE: {}'.format(np.linalg.norm(error)))

	def train(self, training_data, training_targets, learning_rate, epochs, track_error=None, summarize=False, momentum=0, annealing_schedule=0, minibatch_size=1):
		data_divided, targets_divided = self._divide_data(training_data, training_targets, minibatch_size)

		if track_error:
			assert epochs >= track_error, 'track_error must be less than epochs'
			show_error_mod_value = epochs // track_error

		if summarize:
			self.print_summary(training_data, learning_rate, epochs)

		# self._back_propogate_through_time_exp(epochs, training_data, training_targets, learning_rate, print_error=show_error_mod_value)

		num_samples = len(data_divided)

		indices = list(range(num_samples))

		for i in range(epochs):
			shuffle(indices)

			for index in indices:
				self._forward_pass(data_divided[index], reset=True)

				if track_error and i % show_error_mod_value == 0:
					self._back_propogate_through_time(targets_divided[index], learning_rate, momentum, print_error=True)
				else:
					self._back_propogate_through_time(targets_divided[index], learning_rate, momentum)

			if annealing_schedule != 0:
				learning_rate = learning_rate / (1 + i / float(annealing_schedule))