from keras.models import Sequential
from keras.layers import Dense

def default_2d(latent_dims=5):
  disc = default_disc_2d()
  gen = default_gen_2d(latent_dims)
  return disc, gen

def default_gen_2d(latent_dims, outputs=2):
  model = Sequential()
  model.add(Dense(15, activation="relu", input_dim=latent_dims))
  model.add(Dense(8, activation="relu"))
  model.add(Dense(6, activation="relu"))
  model.add(Dense(outputs, activation="linear"))
  return model

def default_disc_2d(inputs=2):
  model = Sequential()
  model.add(Dense(25, activation = "relu", input_dim=inputs, name="Input_Layer"))
  model.add(Dense(25, activation = "relu"))
  model.add(Dense(25, activation = "relu"))
  model.add(Dense(1, activation = "sigmoid", name="Output_Layer"))
  model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
  return model