from enum import Enum

MIN_DISTANCE = 6
MOVEMENT_SPEED = 0.15
MOVEMENT_ANIMATION_INTERVAL = 250


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    @classmethod
    def obtain_direction(self, start, end):
        if end.row_index < start.row_index:
            return Direction.UP
        elif end.row_index > start.row_index:
            return Direction.DOWN
        elif end.col_index < start.col_index:
            return Direction.LEFT
        elif end.col_index > start.col_index:
            return Direction.RIGHT
