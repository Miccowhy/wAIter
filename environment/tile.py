import numpy as np
from helpers.np_array_helper import sliding_window
from gui.drawable import Drawable
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT
from constants.images import FLOOR, ENTRANCE


class Tile(Drawable):
    def __init__(self, environment, row_index, col_index, occupation=None,
                 is_kitchen_entrance=False, color=None, loaded_image=FLOOR, step_cost=0):
        if is_kitchen_entrance:
            loaded_image = ENTRANCE
        super().__init__(width=TILE_WIDTH, height=TILE_HEIGHT, color=color,
                         loaded_image=loaded_image)
        self.environment = environment
        self.row_index = row_index
        self.col_index = col_index
        self.occupation = occupation
        self.is_kitchen_entrance = is_kitchen_entrance
        self.step_cost = step_cost

    # https://stackoverflow.com/questions/10996769/pixel-neighbors-in-2d-array-image-using-python
    def neighbors(self, distance=1):
        i = self.row_index
        j = self.col_index
        w = sliding_window(self.environment.grid, 2 * distance + 1)

        ix = np.clip(i - distance, 0, w.shape[0] - 1)
        jx = np.clip(j - distance, 0, w.shape[1] - 1)

        i0 = max(0, i - distance - ix)
        j0 = max(0, j - distance - jx)
        i1 = w.shape[2] - max(0, distance - i + ix)
        j1 = w.shape[3] - max(0, distance - j + jx)

        return w[ix, jx][i0:i1, j0:j1].ravel()
