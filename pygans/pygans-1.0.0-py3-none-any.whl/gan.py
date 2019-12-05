from keras.models import Sequential
import numpy as np

class GAN:
  def create_model(self, loss="binary_crossentropy", optimizer="adam"):
    discriminator_model = self.discriminator.model
    discriminator_model.trainable = False
    model = Sequential()
    model.add(self.generator.model)
    model.add(discriminator_model)
    model.compile(loss=loss, optimizer=optimizer)
    return model

  def __init__(self, discriminator, generator, latent_dims=5):
    self.discriminator = discriminator
    self.generator = generator
    self.model = self.create_model()

  def train_gan(self, epochs, batch_size, verbose=0):
    x = self.generator.generate_latent_points(batch_size)
    y = np.ones((batch_size,1))
    history = self.model.fit(x, y, epochs=epochs, batch_size=batch_size, verbose=verbose)
    return history

  def train(self, dataset_generator, iterations, batch_size, verbose=0, freq_generation=0):
    generations = []
    discriminations = []
    for i in range(1,iterations+1):
      x, y = dataset_generator.generate_dataset(batch_size, self.generator)
      train_samples = x.shape[0]
      self.discriminator.train(x, y, 1, batch_size, verbose=verbose)
      self.train_gan(1, train_samples, verbose)
      if i % freq_generation == 0 or i == 0:
        if verbose == 0:
          print("Epoch",i)
        g,_ = self.generator.generate(batch_size)
        d = self.discriminator.predict(g)
        generations.append(g)
        discriminations.append(d)
    return generations, discriminations

  def evaluate(self, test_discriminator, n_fake_samples=100):
    x_test_discriminator, y_test_discriminator = test_discriminator
    x_fake, y_fake = self.generator.generate(n_fake_samples)
    
    _, acc_disc = self.discriminator.evaluate(x_test_discriminator, y_test_discriminator)
    _, acc_fake_samples = self.discriminator.evaluate(x_fake, y_fake)
  
    print("Accuracy Discriminator:",acc_disc*100//1,"%")
    print("Percentage of Fake Samples detected:",acc_fake_samples*100//1,"%")
