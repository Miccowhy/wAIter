import numpy as np
import random
from .table import Table
from .tile import Tile
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT
from constants.movement import BANANA_COST


class Restaurant:
    def __init__(self, grid_length, grid_width):
        self.grid_length = grid_length
        self.grid_width = grid_width
        self.grid = self._generate_grid()
        self._assign_cords()
        self._randomize_costs()

    def _generate_grid(self):
        gw = self.grid_width
        gl = self.grid_length
        grid = np.array([
                            [
                                Tile(self, row, col, is_kitchen_entrance=True)
                                if self._should_tile_be_kitchen_entrance(row, col)
                                else
                                Tile(self, row, col)
                                if self._should_tile_be_empty(row, col)
                                else
                                Tile(self, row, col, Table(), cost=100)
                                for col in range(gw)
                            ]
                            for row in range(gl)
                        ],
                        dtype=object)
        return grid

    def _should_tile_be_empty(self, row, col):
        return (row % 2 == 0) or (col % 2 == 0)

    def _should_tile_be_kitchen_entrance(self, row, col):
        return row == 0 and col == int(self.grid_width / 2)

    def _assign_cords(self):
        x = np.arange(0, TILE_WIDTH * self.grid_width, TILE_WIDTH)
        y = np.arange(0, TILE_HEIGHT * self.grid_length, TILE_HEIGHT)
        for row in range(self.grid_width):
            for col in range(self.grid_length):
                tile = self.grid[row][col]
                tile.rect = tile.image.get_rect(topleft=(x[col], y[row]))
                if tile.occupation is not None:
                    tile.occupation.rect = tile.occupation.image.get_rect(topleft=(x[col], y[row]))

    def _randomize_costs(self):
        without_occupation = list(filter(lambda x: x.occupation is None and x.row_index != 0 and x.col_index != 0,
                                  self.grid.flatten()))
        random_tiles = random.choices(without_occupation, k=24)
        for tile in random_tiles:
            tile.cost = BANANA_COST
