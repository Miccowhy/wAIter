import numpy as np
import random
from gui.drawable import Drawable
from gui.animator import Animator
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT
from constants.movement import MIN_DISTANCE, MOVEMENT_SPEED, Direction
from constants.sounds import STEPS
from ai.pathfinding import Action
from copy import deepcopy


class Entity(Drawable):
    def __init__(self, current_tile, loaded_image=None, actions=None, direction=Direction.DOWN):
        super().__init__(width=TILE_WIDTH, height=TILE_HEIGHT, loaded_image=loaded_image)
        self.current_tile = current_tile
        self.rect = deepcopy(self.current_tile.rect)
        self.actions = actions
        self.direction = direction
        self.animator = Animator(self, self.loaded_image)


    def follow_actions(self):
        self.animator.fix_standing_position()
        if self.actions:
            next_action = self.actions[0]
            if next_action[0] is Action.MOVE:
                next_tile = next(neighbor['tile'] for neighbor
                                 in self.current_tile.unoccupied_neighbors_by_directions()
                                 if neighbor['direction'] == next_action[1])
                self._move(next_tile)
                if self._is_within_min_distance(self.rect.center, next_tile.rect.center):
                    random.choice(STEPS).play()
                    self._change_occupation(next_tile)
            elif next_action[0] is Action.ROTATE:
                self.animator.change_direction(next_action[1])
                self.actions.pop(0)

    def _change_occupation(self, next_tile):
        prev_tile = self.current_tile
        self.current_tile = next_tile
        self.current_tile.occupation = self
        prev_tile.occupation = None
        self.actions.pop(0)

    def _is_within_min_distance(self, a, b):
        return (np.abs(np.subtract(a, b)) <= MIN_DISTANCE).all()

    def _move(self, destination):
        self.animator.change_direction(Direction.obtain_direction(self.current_tile, destination))
        self.animator.animate_movement()
        self.rect.center = self._move_towards(destination)

    def _move_towards(self, destination_tile):
        cur_tile_cords = self.rect.center
        dest_tile_cords = destination_tile.rect.center
        return tuple(np.add(cur_tile_cords,
                     np.multiply(np.subtract(dest_tile_cords, cur_tile_cords), MOVEMENT_SPEED)))
