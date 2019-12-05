import numpy as np
from pygans.dataset_generator import Dataset_Generator
from abc import ABC

class Dataset_Generator_2D(Dataset_Generator):
  def __init__(self, function, lower_limit, upper_limit):
    super().__init__()
    self.lower_limit = lower_limit
    self.upper_limit = upper_limit
    self.width = upper_limit - lower_limit
    self.function = function

  def generate_real_samples(self,n):
    X_generated = self.width * np.random.rand(n) + self.lower_limit
    Y_generated = [ self.function(i) for i in X_generated ]
    X = np.asarray(X_generated).reshape(n, 1)
    Y = np.asarray(Y_generated).reshape(n, 1)
    samples = np.hstack((X, Y))
    labels = np.ones((n,1))
    return samples, labels

  def generate_fake_samples(self, n, generator):
    X,Y = generator.generate(n)
    return X, Y

  def generate_dataset(self, n, generator):
    assert n % 2 == 0, "Batch size must be even (One Half is Fake and One Half is Real)"
    input_real, labels_real = self.generate_real_samples(n//2)
    input_fake, labels_fake = self.generate_fake_samples(n//2, generator)

    inputs = np.concatenate((input_real,input_fake))
    labels = np.concatenate((labels_real,labels_fake))
    permutation = np.random.permutation(n)
    # Shuffle values
    inputs = inputs[permutation]
    labels = labels[permutation]

    return inputs,labels
    
