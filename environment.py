import numpy as np

class Restaurant:
    def __init__(self, grid_length, grid_width):
        self.grid_length = grid_length
        self.grid_width = grid_width
        self.grid = self.__generate_grid()

    def __generate_grid(self):
        gw = self.grid_width
        gl = self.grid_length
        grid = np.array([
                            [ Tile() if self.__should_tile_be_empty(i, j, gl) else Tile(Table()) for i in range(gw) ]
                            for j in range(gl)
                        ],
                        dtype = object)
        grid[0][int(len(grid[0]) / 2)].is_kitchen_entrance = True
        return grid

    def __should_tile_be_empty(self, i, j, gl):
        return (i % 2 == 0) or (j == 0) or (j == gl - 1)


class Tile:
    def __init__(self, table = None, is_kitchen_entrance = False):
        self.table = table
        self.is_kitchen_entrance = is_kitchen_entrance


class Table:
    def __init__(self, customers = [], is_dirty = False):
        self.customers = customers
        self.is_dirty = is_dirty
