import numpy as np
from .table import Table
from .tile import Tile


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
                                Tile(self, j, i) if self._should_tile_be_empty(i, j, gl)
                                else Tile(self, j, i, Table())
                                for i in range(gw)
                            ]
                            for j in range(gl)
                        ],
                        dtype=object)
        grid[0][int(gl / 2)].is_kitchen_entrance = True
        return grid

    def _should_tile_be_empty(self, i, j, gl):
        return (i % 2 == 0) or (j % 2 == 0)
