import numpy as np
import random
from gui.drawable import Drawable
from gui.animator import Animator
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT
from constants.movement import MIN_DISTANCE, MOVEMENT_SPEED, Direction
from constants.sounds import STEPS
from constants.colors import YELLOW


class Entity(Drawable):
    def __init__(self, current_tile, loaded_image=None, path=None, direction=Direction.DOWN):
        super().__init__(width=TILE_WIDTH, height=TILE_HEIGHT, loaded_image=loaded_image)
        self.current_tile = current_tile
        self.path = path
        self.animator = Animator(self, self.loaded_image)
        self.direction = Direction.DOWN

    def follow_path(self):
        self.animator.fix_standing_position()
        if self.path:
            next_tile = self.path[0]
            self._move(next_tile)
            self.current_tile.color_surface(YELLOW)
            if self._is_within_min_distance(self.rect.center, next_tile.rect.center):
                random.choice(STEPS).play()
                prev_tile = self.current_tile
                self.current_tile = next_tile
                self.current_tile.occupation = self
                prev_tile.occupation = None
                self.path.pop(0)

    def _is_within_min_distance(self, a, b):
        return (np.abs(np.subtract(a, b)) <= MIN_DISTANCE).all()

    def _move(self, destination_tile):
        self._check_direction(destination_tile)
        self.animator.animate_movement()
        self.rect.center = self._move_towards(destination_tile)

    def _check_direction(self, destination_tile):
        if destination_tile.row_index < self.current_tile.row_index:
            self.animator.change_direction(Direction.UP)
        elif destination_tile.row_index > self.current_tile.row_index:
            self.animator.change_direction(Direction.DOWN)
        elif destination_tile.col_index < self.current_tile.col_index:
            self.animator.change_direction(Direction.LEFT)
        elif destination_tile.col_index > self.current_tile.col_index:
            self.animator.change_direction(Direction.RIGHT)

    def _move_towards(self, destination_tile):
        cur_tile_cords = self.rect.center
        dest_tile_cords = destination_tile.rect.center
        return tuple(np.add(cur_tile_cords,
                     np.multiply(np.subtract(dest_tile_cords, cur_tile_cords), MOVEMENT_SPEED)))
