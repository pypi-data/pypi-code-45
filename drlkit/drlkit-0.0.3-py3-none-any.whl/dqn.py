import gym
import numpy as np
import random
#import keras
#print(f"Keras: {keras.__version__}")
import sys
#from keras.layers import Dense, Dropout
#from keras.models import Sequential

from collections import deque

# Import local files
from experience_replay import Memory
import preprocess
from tf_dqn import TFDQN, PTQNetwork


class DQNAgent(object):
    def __init__(
            self, state_size, action_size, network=PTQNetwork, buffer_size=1_000_000, batch_size=32,
             eps_start=1.0, eps_min=0.01, eps_decay=0.995,
            lr=0.005, activation="relu", gamma=0.9, load=False
        ):
            self.state_size = state_size
            self.action_size = action_size
            self.Q_network = network(state_size, action_size, load)
            self.memory = Memory(buffer_size)
            self.gamma = gamma
            self.eps = eps_start
            self.eps_decay = eps_decay
            self.eps_min = eps_min
            self.batch_size = batch_size
    
    def get_action(self, state, eps=None):
        eps = self.eps if eps == None else eps
        greedy_action = np.argmax(self.Q_network.get_Q_state([state]))
        stochastic_action = np.random.randint(self.action_size)
        action = stochastic_action if random.random() < eps else greedy_action
        return action
        
    def play(self, state, action, reward, next_state, done):
        self.memory.save((state, action, reward, next_state, done))
        states, actions, rewards, next_states, dones = self.memory.sample(self.batch_size)

        next_actions = np.argmax(self.Q_network.get_Q_state(next_states), axis=1)
        print(f"Next actions: {next_actions}")
       
        Q_next_states = self.Q_network.get_Q_state(next_states, target_network=True)
        Q_next_states[dones] = np.zeros([self.action_size])
        Q_next_states_next_actions = Q_next_states[np.arange(next_actions.shape[0]), next_actions]
        Q_targets = rewards + self.gamma * Q_next_states_next_actions
        self.Q_network.optimize(states, actions, Q_targets)
             
        if done: self.eps = max(self.eps * self.eps_decay, self.eps_min)    





























#class Agent(object):
#    def __init__(
#            self, env, buffer_size=1_000_000, batch_size=64,
#            gamma=0.09, eps_start=1.0, eps_min=0.01, eps_decay=0.995,
#            lr=0.005, activation="relu"
#        ):
#        self.env     = env
#        self.memory  = deque(maxlen=2000)
#
#        self.gamma = gamma
#        self.epsilon = eps_start
#        self.epsilon_min = eps_min
#        self.epsilon_decay = eps_decay
#        self.learning_rate = lr
#        self.tau = .125
#        self.memory = Memory(buffer_size=buffer_size)
#        self.batch_size = batch_size
#
#        self.model        = self.create_model()
#        self.target_model = self.create_model()
#
#    def create_model(self):
#        model = Sequential()
#        state_shape  = self.env.observation_space.shape
#        model.add(Dense(24, input_dim=state_shape[0], activation="relu"))
#        model.add(Dense(48, activation="relu"))
#        model.add(Dense(24, activation="relu"))
#        model.add(Dense(self.env.action_space.n))
#        model.compile(loss="mean_squared_error",
#            optimizer=Adam(lr=self.learning_rate))
#        return model
#
#    def act(self, state):
#        self.epsilon *= self.epsilon_decay
#        self.epsilon = max(self.epsilon_min, self.epsilon)
#        if np.random.random() < self.epsilon:
#            return self.env.action_space.sample()
#        return np.argmax(self.model.predict(state)[0])
#
#    def remember(self, state, action, reward, new_state, done):
#        self.memory.save([state, action, reward, new_state, done])
#
#    def replay(self):
#        batch_size = self.batch_size
#        if self.memory.can_provide(batch_size):
#            samples = self.memory.sample(batch_size)
#            for sample in samples:
#                state, action, reward, new_state, done = sample
#                target = self.target_model.predict(state)
#                if done:
#                    target[0][action] = reward
#                else:
#                    Q_future = max(self.target_model.predict(new_state)[0])
#                    target[0][action] = reward + Q_future * self.gamma
#                self.model.fit(state, target, epochs=1, verbose=0)
#        else:
#            return
#
#
#    def target_train(self):
#        weights = self.model.get_weights()
#        target_weights = self.target_model.get_weights()
#        for i in range(len(target_weights)):
#            target_weights[i] = weights[i] * self.tau + target_weights[i] * (1 - self.tau)
#        self.target_model.set_weights(target_weights)
#
#    def save_model(self, fn):
#        self.model.save(fn)
