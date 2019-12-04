import numpy as np
import warnings


warnings.warn(
    ("function is outdated since tournament 168 "
     "and will be removed."),
    DeprecationWarning, stacklevel=2)


# scale_to_30_70(Y_probs)
def scale_to_30_70(x):
    c = x - .5
    m = np.max(np.abs(c))
    return c * .2 / m + .5
