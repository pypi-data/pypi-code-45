import numpy as np

from berenet import BereNet

def mattmazur():
	nn = BereNet([2, 2, 2])

	X = np.array((0.05, 0.1)).reshape(1, 2)

	nn._layers[0].W = np.array(((0.15, 0.25), (0.2, 0.3), (0.35, 0.35)))
	nn._layers[1].W = np.array(((0.4, 0.5), (0.45, 0.55), (0.6, 0.6)))

	target = np.array((0.01, 0.99)).reshape(1, 2)

	nn.train(X, target, 0.5, 10000, minibatch_size=1, summarize=True)

	print(nn.mse)

	print(nn.predict(X))

def deep():
	nn = BereNet([3, 30, 20, 10, 1])

	X = np.array((
		(0, 0, 0),
		(1, 1, 1),
		(1, 0, 1),
		(0, 1, 0),
		(1, 1, 0),
		(0, 1, 1),
		(1, 0, 0),
		(0, 0, 1)
	), dtype=np.float64)

	targets = np.array((
		(0),
		(0),
		(1),
		(0),
		(1),
		(1),
		(0),
		(0)
	)).reshape(8, 1)

	nn.train(X, targets, 1, 30000, minibatch_size=1)
	nn.train(X, targets, 0.011, 10000, minibatch_size=1)

	print(nn.predict(X))

def stress_test():
	nn = BereNet([200, 5000, 100, 150])

	X = np.ones((38, 200), dtype=np.float64)

	target = np.zeros((38, 150), dtype=np.float64)

	nn.train(X, target, 0.5, 10)

	print(nn.predict(X))

def or_gate():
	training_data = np.array((
		(1, 0),
		(1, 1),
		(0, 1),
		(0, 0)
	), dtype=np.float64)

	targets = np.array((
		(1,),
		(1,),
		(1,),
		(0,)
	), dtype=np.float64)

	nn = BereNet([2, 2, 1], biases=[2])

	nn.verbosity = ''
	nn.train(training_data, targets, 1, 10000, minibatch_size=4, momentum=0.9, summarize=True)

# mattmazur()
# deep()
# stress_test()
# or_gate()

# Import BereNet and numpy
from berenet import BereNet
import numpy as np

# Initialize the training data as a numpy array
# Here the rows are examples, while the columns are inputs to the network
# There must be the same number of columns as input neurons
training_data = np.array((
		(1, 0),
		(1, 1),
		(0, 1),
		(0, 0)
), dtype=np.float64)

# Initialize the target outputs for the neural network
# There must be the same number of rows here as in training_data
# There must also be the same number of columns as output neurons for the network
targets = np.array((
  (1,),
  (1,),
  (1,),
  (0,)
), dtype=np.float64)

# Create the neural network
# This network will have 2 input neurons, 2 hidden neurons, and 1 output neuron
nn = BereNet([2, 2, 1])

# Train the network
# First argument is the training data (will be split into 4 arrays with 1 minibatch each, as specified above)
# Second argument is self-explanatory
# Third argument is the learning rate
# Fourth argument is the number of epochs to train for
nn.train(training_data, targets, 0.1, 10000)

# Print out the prediction for all 4 examples we trained on
print(nn.predict(training_data))