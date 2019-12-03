# Load External packages
import numpy as np                                      # for wicked fast arrays                                  MORE INFORMATION: https://docs.scipy.org/doc/
from numpy import *                                     # for ease of math function use
from numpy.linalg import *                              # for ease of linalg function use
from numba import njit                                  # for compiling functions into C, so they run faster.     MORE INFORMATION: http://numba.pydata.org/
from numba import jit
import matplotlib.pyplot as plt                         # for simple plotting
from matplotlib import collections as mc                # for simple plotting
import random as rd                                     # for random numbers
import time                                             # for timing
from termcolor import colored                           # for colored print statements
import os                                               # for deep file manipulation
import imageio                                          # for gif making
from matplotlib.ticker import FormatStrFormatter        # for FormatStrFormatter
from typing import List                                 # for specification of types
from PIL import Image                                   # for faster images
import math                                             # for math
from scipy.stats import linregress                      # for linear regressions


# this should only be temporary
from numba.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning, NumbaPerformanceWarning
import warnings
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPerformanceWarning)
