import numpy as np
from .table import Table
from .tile import Tile
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT


class Restaurant:
    def __init__(self, grid_length, grid_width):
        self.grid_length = grid_length
        self.grid_width = grid_width
        self.grid = self._generate_grid()
        self._assign_cords()

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

    def _assign_cords(self):
        x = np.arange(0, TILE_WIDTH * self.grid_width, TILE_WIDTH)
        y = np.arange(0, TILE_HEIGHT * self.grid_length, TILE_HEIGHT)
        for row in range(self.grid_width):
            for col in range(self.grid_length):
                tile = self.grid[row][col]
                tile.rect = tile.image.get_rect(topleft=(x[col], y[row]))
                if tile.occupation is not None:
                    tile.occupation.rect = tile.occupation.image.get_rect(topleft=(x[col], y[row]))
