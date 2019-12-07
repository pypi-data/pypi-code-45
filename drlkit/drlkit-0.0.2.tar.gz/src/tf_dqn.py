import os
import tensorflow as tf
print(f"TF Version: {tf.__version__}")
from tensorflow.keras.layers import Dense
import numpy as np
print(tf.__version__)
tf.keras.backend.set_floatx('float64')

class TFModel(tf.keras.Model):
	"""
	
	HIDDEN_SIZE = 800             # Specifies the number of nodes in each layer of the network
	LEARNING_RATE = 0.00002       # Sets how much we want to update the network weights at each training step
	REGULARIZER_LAMBDA = 1e-6     # Penalty multiplier to apply for the size of the network weights
	TARGET_UPDATE_RATE = 0.0004   # How frequently we want to copy the local network to the target network (for double DQNs)
	
	"""
	def __init__(self, state_size, action_size, hidden_layer_size=600, lmbda=1e-6):
		super().__init__()
		# First hidden layer
		self.hidden1 = Dense(hidden_layer_size, activation=tf.nn.relu, kernel_initializer=tf.initializers.glorot_normal())
		
		# Second hidden hidden layer
		self.hidden2 = Dense(hidden_layer_size, activation=tf.nn.relu, kernel_initializer=tf.initializers.glorot_normal(), kernel_regularizer=tf.keras.regularizers.l2(l=lmbda))
		
		# Output layer
		self.Q_state = Dense(action_size, activation=None, kernel_initializer=tf.initializers.glorot_normal())
		
		
	def call(self, state):
		hidden_layer_1 = self.hidden1(state)
		hidden_layer_2 = self.hidden2(hidden_layer_1) + hidden_layer_1
		output = self.Q_state(hidden_layer_2)
#		print("OUUUUUUUUUUUUTTTTT\n\n\n")
#		print(output)
		return output

class TFDQN(object):
	def __init__(self, state_size, action_size, load=False, lr=0.00002, tau=0.0004):
		self.tau = tau
		# Policy model
		self.policy_model = TFModel(state_size, action_size)
		# Target Model
		self.target_model = TFModel(state_size, action_size)
		self.optimizer = tf.optimizers.SGD(learning_rate=0.1)
		self.action_size = action_size
		if load: self.load_model()
		
	# Get Q value for state
	def get_Q_state(self, state, target_network=False):
		model = self.policy_model if not target_network else self.target_model
#		print(f"get_Q_state: {model(np.array(state)).numpy()}")
		return model(np.array(state)).numpy()
		
	# Calculate loss	
	def get_loss(self, states, actions, Q_targets):
		actions_o_h = tf.one_hot(actions, depth=self.action_size)
		Q_states = tf.cast(self.policy_model(states), tf.float32)
		Q_states_actions = tf.reduce_sum(tf.multiply(Q_states, actions_o_h), axis=1)
		loss = tf.reduce_sum(tf.square(Q_states_actions - Q_targets))
		return loss
		
	def optimize(self, states, actions, Q_targets):
		loss = lambda: self.get_loss(states, actions, Q_targets)
		print(f'trainable weights: {self.policy_model.trainable_weights}')
		self.optimizer.minimize(loss=loss, var_list=self.policy_model.trainable_weights)
		self.soft_copy(self.policy_model, self.target_model)
	
	def soft_copy(self, policy, target):
		new_target_vars = [t + self.tau*(1-t) for l,t in zip(policy.get_weights(), target.get_weights())]
		self.target_model.set_weights(new_target_vars)
		
	def save_model(self, filepath="./saved_models/tensorflow/model.tf"):
		os.makedirs(os.path.dirname(filepath), exist_ok=True)
		self.policy_model.save_weights(filepath)
		
	def load_model(self, filepath="./saved_models/tensorflow2/model.tf"):
		if os.path.exists(filepath + ".index"):
			self.policy_model.load_weights(filepath)
			self.target_model.load_weights(filepath)
			



import torch
print("PyTorch:", torch.__version__)

HIDDEN_SIZE = 800             # Specifies the number of nodes in each layer of the network
LEARNING_RATE = 0.00002       # Sets how much we want to update the network weights at each training step
REGULARIZER_LAMBDA = 1e-6     # Penalty multiplier to apply for the size of the network weights
TARGET_UPDATE_RATE = 0.0004   # How frequently we want to copy the local network to the target network (for double DQNs)

class PTModel(torch.nn.Module):
	def __init__(self, state_size, action_size):
		super().__init__()
		self.hidden1 = torch.nn.Linear(state_size, HIDDEN_SIZE)
		self.hidden2 = torch.nn.Linear(HIDDEN_SIZE, HIDDEN_SIZE)
		self.Q_state = torch.nn.Linear(HIDDEN_SIZE, action_size)
		torch.nn.init.xavier_normal_(self.hidden1.weight)
		torch.nn.init.xavier_normal_(self.hidden2.weight)
		torch.nn.init.xavier_normal_(self.Q_state.weight)

	def forward(self, state):
		hidden1 = torch.nn.functional.relu(self.hidden1(state))
		hidden2 = torch.nn.functional.relu(self.hidden2(hidden1)) + hidden1
		Q_state = self.Q_state(hidden2)
		return Q_state

class PTQNetwork():
	def __init__(self, state_size, action_size, load=False):
		self.model_local = PTModel(state_size, action_size)
		self.model_target = PTModel(state_size, action_size)
		self.optimizer = torch.optim.Adam(self.model_local.parameters(), lr=LEARNING_RATE, weight_decay=REGULARIZER_LAMBDA)
		if load: self.load_model()

	def get_Q_state(self, state, use_target=False):
		model = self.model_local if not use_target else self.model_target
		state = torch.from_numpy(np.array(state)).float()
		return model(state).detach().numpy()
	
	def get_loss(self, states, actions, Q_targets):
		states = torch.from_numpy(np.vstack(states)).float()
		actions = torch.from_numpy(np.vstack(actions)).long()
		Q_targets = torch.from_numpy(np.vstack(Q_targets)).float()
		Q_states_actions = self.model_local(states).gather(1, actions)
		loss = (Q_states_actions - Q_targets)**2
		return loss.mean()
	
	def optimize(self, states, actions, Q_targets):
		loss = self.get_loss(states, actions, Q_targets)
		self.optimizer.zero_grad()
		loss.backward()
		self.optimizer.step()
		self.soft_copy(self.model_local, self.model_target)
		
	def soft_copy(self, local, target, tau=TARGET_UPDATE_RATE):
		for l,t in zip(local.parameters(), target.parameters()):
			t.data.copy_(t.data + tau*(l.data - t.data))
		
	def save_model(self, filepath="./saved_models/pytorch/checkpoint.pth"):
		os.makedirs(os.path.dirname(filepath), exist_ok=True)
		torch.save(self.model_local.state_dict(), filepath)
		
	def load_model(self, filepath="./saved_models/pytorch/checkpoint.pth"):
		if os.path.exists(filepath):
			self.model_local.load_state_dict(torch.load(filepath))
			self.model_target.load_state_dict(torch.load(filepath))