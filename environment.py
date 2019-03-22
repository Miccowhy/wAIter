import numpy as np
from numpy.lib.stride_tricks import as_strided


class Restaurant:
    def __init__(self, grid_length, grid_width):
        self.grid_length = grid_length
        self.grid_width = grid_width
        self.grid = self._generate_grid()

    def _generate_grid(self):
        gw = self.grid_width
        gl = self.grid_length
        grid = np.array([
                            [
                                Tile(i, j) if self._should_tile_be_empty(i, j, gl)
                                else Tile(i, j, Table())
                                for i in range(gw)
                            ]
                            for j in range(gl)
                        ],
                        dtype=object)
        grid[0][int(gl / 2)].is_kitchen_entrance = True
        return grid

    def _should_tile_be_empty(self, i, j, gl):
        return (i % 2 == 0) or (j == 0) or (j == gl - 1)

    # --- https://stackoverflow.com/questions/10996769/pixel-neighbors-in-2d-array-image-using-python ---
    def tile_neighbors(self, current_tile, distance=1):
        i = current_tile.row_index
        j = current_tile.col_index
        w = self._sliding_window(self.grid, 2 * distance + 1)

        ix = np.clip(i - distance, 0, w.shape[0] - 1)
        jx = np.clip(j - distance, 0, w.shape[1] - 1)

        i0 = max(0, i - distance - ix)
        j0 = max(0, j - distance - jx)
        i1 = w.shape[2] - max(0, distance - i + ix)
        j1 = w.shape[3] - max(0, distance - j + jx)

        return w[ix, jx][i0:i1, j0:j1].ravel()

    def _sliding_window(self, arr, window_size):
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
    # ---


class Tile:
    def __init__(self, row_index, col_index, table=None, is_occupied=False,
                 is_kitchen_entrance=False):
        self.row_index = row_index
        self.col_index = col_index
        self.table = table
        self.is_occupied = is_occupied
        self.is_kitchen_entrance = is_kitchen_entrance


class Table:
    def __init__(self, customers=[], is_dirty=False):
        self.customers = customers
        self.is_dirty = is_dirty
