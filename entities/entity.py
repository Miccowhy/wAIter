import numpy as np
from gui.drawable import Drawable
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT
from constants.movement import MIN_DISTANCE, MOVEMENT_SPEED


class Entity(Drawable):
    def __init__(self, current_tile, loaded_image=None, path=None):
        super().__init__(width=TILE_WIDTH, height=TILE_HEIGHT, loaded_image=loaded_image)
        self.current_tile = current_tile
        self.path = path

    def follow_path(self):
        if self.path:
            next_tile = self.path[0]
            self._move(next_tile)
            if self._is_within_min_distance(self.rect.center, next_tile.rect.center).all():
                prev_tile = self.current_tile
                self.current_tile = next_tile
                self.current_tile.occupation = self
                prev_tile.occupation = None
                self.path.pop(0)

    def _is_within_min_distance(self, a, b):
        return np.abs(np.subtract(a, b)) <= MIN_DISTANCE

    def _move(self, destination_tile):
        self.rect.center = self._move_towards(destination_tile)

    def _move_towards(self, destination_tile):
        cur_tile_cords = self.rect.center
        dest_tile_cords = destination_tile.rect.center
        return tuple(np.add(cur_tile_cords,
                     np.multiply(np.subtract(dest_tile_cords, cur_tile_cords), MOVEMENT_SPEED)))
