from abc import ABC, abstractmethod

class Dataset_Generator(ABC):
  def __init__(self):
    super().__init__()

  @abstractmethod
  def generate_real_samples(self,n):
    pass

  @abstractmethod
  def generate_fake_samples(self,n,generator):
    pass

  @abstractmethod
  def generate_dataset(self, n, generator):
    pass
