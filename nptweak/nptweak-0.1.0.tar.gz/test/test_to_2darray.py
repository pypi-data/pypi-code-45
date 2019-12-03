from nptweak import to_2darray
import numpy as np
import numpy.testing as npt


def test1():
    x = np.array([1, 2, 3])
    y = to_2darray(x)  # flip=False, trans=False
    target = np.array([[1], [2], [3]])
    npt.assert_array_equal(y, target)


def test2():
    x = np.array([1, 2, 3])
    y = to_2darray(x, flip=True)  # trans=False
    target = np.array([[3], [2], [1]])
    npt.assert_array_equal(y, target)


def test3():
    x = np.array([1, 2, 3])
    y = to_2darray(x, trans=True)  # flip=False
    target = np.array([[1, 2, 3]])
    npt.assert_array_equal(y, target)


def test4():
    x = np.array([1, 2, 3])
    y = to_2darray(x, trans=True, flip=True)
    target = np.array([[1, 2, 3]])
    npt.assert_array_equal(y, target)


def test5():
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = to_2darray(x, flip=True)  # trans=False
    target = np.array([[4, 5, 6], [1, 2, 3]])
    npt.assert_array_equal(y, target)


def test6():
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = to_2darray(x, trans=True)  # flip=False
    target = np.array([[1, 4], [2, 5], [3, 6]])
    npt.assert_array_equal(y, target)


def test7():
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = to_2darray(x, trans=True, flip=True)
    target = np.array([[3, 6], [2, 5], [1, 4]])
    npt.assert_array_equal(y, target)
