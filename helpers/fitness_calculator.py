import numpy as np
from environment.restaurant import Restaurant
from constants.desirability import WINDOW_VIEW, CLOSE_TABLES, ENTRANCE_BARRICADE, NEARBY_WALL
from constants.dimensions import TILE_HEIGHT, TILE_WIDTH

class Fitness:
    def __init__(self, env):
        for col in range(TILE_HEIGHT):
            for row in range(TILE_WIDTH):
                if env[col][row].occupation is None:
                    for element in env[col][row].quadrant():
                        if isinstance(element.occupation, Wall):
                            if element.occupation.is_window:
                                