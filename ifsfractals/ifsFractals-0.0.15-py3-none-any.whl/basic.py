from externals import *

## Built-In Transformations
def Scale(s):
    return np.array([[s, 0, 0],[0, s, 0],[0, 0, 1]], dtype=np.float64)
def Translate(a, b):
    return np.array([[1, 0, a],[0, 1, b],[0, 0, 1]], dtype=np.float64)
def Rotate(theta):
    return np.array([[np.cos(theta), -np.sin(theta), 0],[np.sin(theta), np.cos(theta), 0],[0, 0, 1]], dtype=np.float64)
def ShearX(t):
    return np.array([[1, t, 0],[0,1, 0],[0, 0, 1]], dtype=np.float64)
def ShearY(t):
    return np.array([[1, 0, 0],[t,1, 0],[0, 0, 1]], dtype=np.float64)
def ScaleX(s):
    return np.array([[s, 0, 0],[0, 1, 0],[0, 0, 1]], dtype=np.float64)
def ScaleY(s):
    return np.array([[1, 0, 0],[0, s, 0],[0, 0, 1]], dtype=np.float64)
def ScaleXY(s, t):
    return np.array([[s, 0, 0],[0,t, 0],[0, 0, 1]], dtype=np.float64)


## Built-In Figures
Box = np.array([ [0., 0., 1.], [1., 0., 1.], [1., 1., 1.], [0., 1., 1.], [0., 0., 1.], [1/8, 1/8, 1.], [1/8-1/16, 1/8+1/16, 1.] ]).T
def rect(n):
    return ScaleY(1/n) @ Box
Line = np.array([ [0., 0., 1.], [1., 0., 1.] ]).T

XBox = np.array([ [0., 0., 1.], [1., 0., 1.], [1., 1., 1.], [0., 1., 1.], [0., 0., 1.], [0.5, 0., 1.], [0.5, 1., 1.], [1., 1., 1.], [1., 0.5, 1.], [0., 0.5, 1.], [0., 0., 1.], [1/8, 1/8, 1.], [1/8-1/16, 1/8+1/16, 1.]]).T
