import numpy as np


def to_2darray(x: np.array, copy: bool = True, trans: bool = False,
               flip: bool = False) -> np.array:
    """
    Assumption:
    -----------
    x is assumed to be numpy 2D array or matrix.
    (please convert x accordingly). For example,

          x = nptweak.to_2darray(x)

    The newest or most recent observation is the
    last row. The oldest observation is stored in
    the first row. For example,

          x = nptweak.to_2darray(x, flip=True)
    """
    if copy:
        y = x.copy()
    else:
        y = x
    # convert to 1D to 2D array
    if len(y.shape) == 1:
        y = y.reshape(-1, 1)
    # transpose the matrix
    if trans:
        y = y.T
    # flip matrix upside down
    if flip:
        y = np.flipud(y)
    # done
    return y
