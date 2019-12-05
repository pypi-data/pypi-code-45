from matplotlib import animation, rc
import matplotlib.pyplot as plt
import numpy as np

class Animation():
  def __init__(self, plots, lower_limit, upper_limit, labels=None):
    self.lower_limit = lower_limit
    self.upper_limit = upper_limit
    self.plots = plots
    # Transforms Probabilities in Colours
    self.labels = labels*100
    fig, ax = plt.subplots()
    self.fig = fig
    self.ax = ax
    self.ax.set(xlim=(lower_limit,upper_limit))
    self.scat = self.ax.scatter([], [])

  def animate(self, i):
    if self.labels != None:
      labels = self.labels[i]
      labels = labels.reshape(labels.shape[0])
      self.scat.set_array(labels)
    self.scat.set_offsets(self.plots[i])
    return self.scat,

  def draw_function(self,function):
    increment = 0.0001
    ll = self.lower_limit
    ul = self.upper_limit
    X = list(np.arange(ll,ul,increment))
    Y = [function(i) for i in X]
    self.ax.plot(X,Y)

  def show(self, fps):
    interval = 1000 / fps
    frames = len(self.plots)
    animate_function = self.animate
    fig = self.fig
    an = animation.FuncAnimation(fig, animate_function, frames=frames, interval=interval, blit=True)
    return an
