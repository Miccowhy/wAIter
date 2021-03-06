import numpy as np
import random
from .table import Table
from .tile import Tile
from .wall import Wall, Window
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT
from constants.bananas import BANANA_COST, BANANA_AMOUNT


class Restaurant:
    def __init__(self, grid_width, grid_length):
        self.grid_length = grid_length
        self.grid_width = grid_width

    def push_grid_positions(self, positions):
        self._should_be_wall, self._should_be_window, self._should_be_restaurant_entrance, \
            self._should_be_empty, self._should_be_table = positions
        self.grid = self._generate_grid()
        self._assign_cords()
        self._randomize_costs()

    def _generate_grid(self):
        gw = self.grid_width
        gl = self.grid_length
        grid = np.array([
                            [
                                Tile(self, row, col, Wall(), step_cost=100)
                                if (row, col) in self._should_be_wall
                                else
                                Tile(self, row, col, Window(), step_cost=100)
                                if (row, col) in self._should_be_window
                                else
                                Tile(self, row, col, is_restaurant_entrance=True)
                                if (row, col) in self._should_be_restaurant_entrance
                                else
                                Tile(self, row, col)
                                if (row, col) in self._should_be_empty
                                else
                                Tile(self, row, col, Table(), step_cost=100)
                                for col in range(gw)
                            ]
                            for row in range(gl)
                        ],
                        dtype=object)
        return grid

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
        without_occupation = [tile for tile in self.grid.flatten()
                              if tile.occupation is None
                              and tile.row_index != 0
                              and tile.col_index != 0]
        random_tiles = random.choices(without_occupation, k=BANANA_AMOUNT)
        for tile in random_tiles:
            tile.step_cost = BANANA_COST
