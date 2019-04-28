from enum import Enum

MIN_DISTANCE = 6
MOVEMENT_SPEED = 0.15
MOVEMENT_ANIMATION_INTERVAL = 250


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
