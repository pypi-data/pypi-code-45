import numpy as np

from berecurrenet import BerecurreNet

def test_1():
	X = np.array((
		(
			(1, 0, 0, 0),
		),
		(
			(0, 1, 0, 0),
		),
		(
			(0, 0, 1, 0),
		),
		(
			(0, 0, 1, 0),
		)
	), dtype=np.float64)

	targets = np.array((
		((0, 1, 0, 0)),
		((0, 0, 1, 0)),
		((0, 0, 1, 0)),
		((0, 0, 0, 1)),
	), dtype=np.float64)

	rnn = BerecurreNet([4, 10, 4])

	rnn.train(X, targets, 1, 1000, track_error=10, summarize=True)

	prediction = rnn.predict(X, reset=True, round_digits=1)

	print(prediction)

def test_2():
	X = np.array((
		(
			(0.1),
		),
		(
			(0.2),
		),
		(
			(0.3),
		),
		(
			(0.4),
		)
	), dtype=np.float64).reshape(4, 1, 1)

	targets = np.array((
		((0.2),),
		((0.3),),
		((0.3),),
		((0.5),),
	), dtype=np.float64).reshape(4, 1, 1)

	rnn = BerecurreNet([1, 4, 1], biases=[2])

	rnn.train(X, targets, 1, 10000, track_error=10, minibatch_size=1)

	prediction = rnn.predict(X, reset=True, round_digits=1, softmax_output=False)

	print(prediction)

def test_3():
	X = np.array((
		(
			(0.1,),
			(0.2,),
			(0.3,)
		),
		(
			(0.2,),
			(0.3,),
			(0.4,)
		),
		(
			(0.3,),
			(0.4,),
			(0.5,)
		),
		(
			(0.4,),
			(0.5,),
			(0.6,)
		)
	), dtype=np.float64)

	targets = np.array((
		((0.2,), (0.3,), (0.4,)),
		((0.3,), (0.4,), (0.5,)),
		((0.3,), (0.4,), (0.5,)),
		((0.5,), (0.6,), (0.7,)),
	), dtype=np.float64)

	rnn = BerecurreNet([1, 5, 5, 1], biases=[1, 2, 1])

	rnn.train(X, targets, 1.01, 10000, track_error=10, summarize=True, momentum=0.9, annealing_schedule=100000000000000, minibatch_size=1)

	prediction = rnn.predict(X, reset=True, round_digits=1, softmax_output=False)

	print(prediction)

def test_4():
	X = np.array((
		(
			(0.1),
		),
		(
			(0.2),
		),
		(
			(0.3),
		),
		(
			(0.4),
		)
	), dtype=np.float64)

	targets = np.array((
		((0.2),),
		((0.3),),
		((0.4),),
		((0.5),),
	), dtype=np.float64)

	# run a few times, may producde no results what so ever (usually), but will end up getting a good initialization of weights at some point and to really well

	rnn = BerecurreNet([1, 10, 1], functions=['relu'], biases=[1])

	rnn.train(X, targets, 1, 10000, track_error=10, summarize=True)

	prediction = rnn.predict(X, reset=True, round_digits=None, softmax_output=False)

	print(prediction)

test_1()
# test_2()
# test_3()
# test_4()

def or_gate():
	training_data = np.array((
		(
			(1, 0),
			(1, 1),
			(0, 1),
			(0, 0)
		),
	), dtype=np.float64)

	targets = np.array((
		(
			(1,),
			(1,),
			(1,),
			(0,)
		),
	), dtype=np.float64)

	rnn = BerecurreNet([2, 2, 1], biases=[1], functions=['identity', 'logistic', 'logistic'])

	rnn.train(training_data, targets, 1, 10000, track_error=10, summarize=True, momentum=0)

	print(rnn.predict(training_data))

# or_gate()