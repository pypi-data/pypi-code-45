"""lambdata - a collection os data science heper functions"""

import pandas as pd
import numpy as np

#sample code

#sample datasets
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(10))

#sample functions
def increment(x):
  return (x + 1)

