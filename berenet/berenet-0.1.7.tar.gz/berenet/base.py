import warnings

from berenet.layer import Layer, np
from math import ceil
from random import shuffle
from berenet.recurrent_layer import RecurrentLayer
import pickle
import logging

class Base:
	IDENTITY = Layer.FUNCTIONS[0]
	LOGISTIC = Layer.FUNCTIONS[1]
	TANH = Layer.FUNCTIONS[2]
	ARCTAN = Layer.FUNCTIONS[3]
	SOFTSIGN = Layer.FUNCTIONS[4]
	RELU = Layer.FUNCTIONS[5]

	def __init__(self, layers):
		assert len(layers) >= 2, 'Must have at least 2 layers'

		logging.basicConfig(level=logging.INFO)

		self._layers = []
		self.verbosity = 'e'

		self._previous_gradients = []

	def predict(self, X, round=False):
		raise NotImplementedError('ayy')

	def train(self, training_data, training_targets, learning_rate, epochs, validation_data=None, validation_targets=None, minibatch_size=None, momentum=0, annealing_schedule=0, l2_regularizer=0, summarize=False):
		raise NotImplementedError('angry reacts only')

	def _divide_data(self, data, targets, minibatch_size):
		assert minibatch_size > 0, 'Minibatch size must be positive'

		assert data.shape[0] == targets.shape[0], 'Data and targets must have the same amount of samples'

		data_divided = None
		targets_divided = None

		if minibatch_size == 1:
			warnings.warn('Setting minibatch size to 1 will update the weights after every training case')

		axis = 0

		if len(data.shape) == 3:
			axis = 1

		num_samples = data.shape[axis]

		if num_samples > minibatch_size:
			amount = int(ceil(float(num_samples) / minibatch_size))
			data_divided = np.array_split(data, amount, axis=axis)
			targets_divided = np.array_split(targets, amount, axis=axis)
		else:
			if num_samples < minibatch_size:
				warnings.warn('You have less samples than your minibatch size, this is likely to affect perfomance of your model.')
			elif num_samples == minibatch_size:
				warnings.warn('You have the same amount of samples as your minibatch size, this is the same as performing full-batch learning.')
			
			data_divided = [data]
			targets_divided = [targets]

		if 's' in self.verbosity:
			logging.info('Num. of samples:', num_samples)
			logging.info('Num. of minibatches:', len(data_divided))
			logging.info('Minibatch size:', minibatch_size)

			if data_divided[-1].shape[0] != minibatch_size:
				logging.info('Size of last minibatch:', data_divided[-1].shape[0])

		return data_divided, targets_divided

	def print_summary(self, training_data, learning_rate, epochs):
		recurrent_layers = 0
		ff_layers = 0
		total_neurons = 0
		total_weights = 0

		prev_outputs = 0

		is_recurrent = False

		for layer in self._layers:
			if isinstance(layer , RecurrentLayer):
				is_recurrent = True
				
				if layer.recurrent:
					recurrent_layers += 1
					total_weights += layer.inputs

			if not layer.is_output:
				total_weights += layer.inputs * layer.W.shape[1]
				
				total_neurons += layer.inputs
				prev_outputs = layer.outputs
			else:
				total_neurons += prev_outputs

		if recurrent_layers > 0:
			logging.info('Type: {}'.format('Recurrent'))
		else:
			logging.info('Type: {}'.format('Feed Forward'))

		logging.info('\tLayers: {}'.format(len(self._layers)))

		if recurrent_layers > 0:
			logging.info('\tRecurrent Layers: {}'.format(recurrent_layers))
			logging.info('\tFeed Forward Layers: {}'.format(len(self._layers) - recurrent_layers))
		
		logging.info('\tTotal Neurons: {}'.format(total_neurons))
		logging.info('\tTotal Weights: {}'.format(total_weights))

		logging.info('Data')

		if is_recurrent:
			logging.info('\tTime Steps: {}'.format(training_data.shape[0]))
			logging.info('\tInstances per time step: {}'.format(training_data.shape[1]))		
			logging.info('\tTotal Instances: {}'.format(training_data.shape[1] * training_data.shape[0]))
		else:
			logging.info('\tTotal Instances: {}'.format(training_data.shape[0]))
		
		logging.info('\tData Shape: {}'.format(training_data.shape))

		logging.info('Parameters')
		logging.info('\tLearning Rate: {}'.format(learning_rate))
		logging.info('\tEpochs: {}'.format(epochs))

	def save(self, file_name):
		file = open(file_name, 'wb')
		pickle.dump(self, file)
		file.close()

	@staticmethod
	def load(file_name):
		file = open(file_name, 'rb')
		nn = pickle.load(file)
		file.close()

		return nn

	def show_verbosity_legend(self):
		logging.info('Verbosity Legend:')

		logging.info('m is to show mean squared error everytime it changes')
		logging.info('s is to show sample metrics')
		logging.info('e is to show epochs')
		logging.info('n is to show minibatch number with every epoch')

	def _m(self):
		logging.info('MSE:', self.mse)