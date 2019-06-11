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
        self.grid = self._generate_grid()
        self._assign_cords()
        self._randomize_costs()

    def _generate_grid(self):
        gw = self.grid_width
        gl = self.grid_length
        grid = np.array([
                            [
                                Tile(self, row, col, is_restaurant_entrance=True)
                                if self._should_tile_be_restaurant_entrance(row, col)
                                else
                                #Tile(self, row, col)
                                #if self._should_tile_be_empty(row, col)
                                Tile(self, row, col, Table(), step_cost=100)
                                if self._should_tile_be_table(row, col)
                                else
                                Tile(self, row, col, Wall(), step_cost=100)
                                if self._should_tile_be_wall(row, col)
                                else
                                Tile(self, row, col, Window(), step_cost=100)
                                if self._should_tile_be_window(row, col)
                                else
                                Tile(self, row, col)
                                for col in range(gw)
                            ]
                            for row in range(gl)
                        ],
                        dtype=object)
        return grid

    #def _should_tile_be_empty(self, row, col):
    #    return (row % 2 == 0 and row != 0 and row != self.grid_width-1 and col != 0 and col != self.grid_length-1) or (col % 2 == 0 and col != 0 and col != self.grid_length-1 and row != 0 and row != self.grid_width-1)

    def _should_tile_be_window(self, row, col):
        return (col == 0 and row % 2 != 0) or (col == self.grid_length-1 and row % 2 != 0)

    def _should_tile_be_wall(self, row, col):
        return (row == 0 and col != int(self.grid_width / 2)) or row == self.grid_width-1 or (col == 0 and row % 2 == 0) or (col == self.grid_length-1 and row % 2 == 0)

    def _should_tile_be_restaurant_entrance(self, row, col):
        return row == 0 and col == int(self.grid_width / 2)

    def _should_tile_be_table(self, row, col):
        return row == 5 and col == 5

#    def arrange_tables(self, table_positions):
#        print('Table pos:', table_positions)
#        for row in range(self.grid_width):
#            for col in range(self.grid_length):
                #if [row, col] in table_positions:
                    #self.grid[row][col].occupation = Table()
                    #self.grid[row][col].step_cost = 100
                    #print(row, col)

    def _assign_cords(self):
        x = np.arange(0, TILE_WIDTH * self.grid_width, TILE_WIDTH)
        y = np.arange(0, TILE_HEIGHT * self.grid_length, TILE_HEIGHT)
        for row in range(self.grid_width):
            for col in range(self.grid_length):
                tile = self.grid[row][col]
                #tile = self.grid[col][row]
                tile.rect = tile.image.get_rect(topleft=(x[col], y[row]))
                #tile.rect = tile.image.get_rect(topleft=(x[row], y[col]))
                if tile.occupation is not None:
                    tile.occupation.rect = tile.occupation.image.get_rect(topleft=(x[col], y[row]))
                    #tile.occupation.rect = tile.occupation.image.get_rect(topleft=(x[row], y[col]))

    def _randomize_costs(self):
        without_occupation = list(filter(lambda x: x.occupation is None and x.row_index != 0 and x.col_index != 0,
                                  self.grid.flatten()))
        random_tiles = random.choices(without_occupation, k=BANANA_AMOUNT)
        for tile in random_tiles:
            tile.step_cost = BANANA_COST

