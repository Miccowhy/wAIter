import numpy as np
from numpy.lib.stride_tricks import as_strided


# https://stackoverflow.com/questions/10996769/pixel-neighbors-in-2d-array-image-using-python
def sliding_window(arr, window_size):
    arr = np.asarray(arr)
    window_size = int(window_size)
    if arr.ndim != 2:
        raise ValueError("need 2-D input")
    if not (window_size > 0):
        raise ValueError("need a positive window size")
    shape = (arr.shape[0] - window_size + 1,
             arr.shape[1] - window_size + 1,
             window_size, window_size)
    if shape[0] <= 0:
        shape = (1, shape[1], arr.shape[0], shape[3])
    if shape[1] <= 0:
        shape = (shape[0], 1, shape[2], arr.shape[1])
    strides = (arr.shape[1] * arr.itemsize, arr.itemsize,
               arr.shape[1] * arr.itemsize, arr.itemsize)
    return as_strided(arr, shape=shape, strides=strides)
