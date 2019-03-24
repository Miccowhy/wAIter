import pygame
from entities.waiter_agent import WaiterAgent
from environment.table import Table


BLACK = (0, 0, 0)
BROWN = (222, 184, 135)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

TILE_WIDTH = 45
TILE_HEIGHT = 45
TILE_MARGIN = 5


def draw_grid(environment, screen):
    for row in range(environment.grid_width):
        for column in range(environment.grid_length):
            tile = environment.grid[row][column]

            if type(tile.occupation) is Table:
                color = BROWN
            elif type(tile.occupation) is WaiterAgent:
                color = GREEN
            elif tile.is_kitchen_entrance:
                color = YELLOW
            else:
                color = WHITE

            pygame.draw.rect(screen,
                             color,
                             [(TILE_MARGIN + TILE_WIDTH) * column + TILE_MARGIN,
                              (TILE_MARGIN + TILE_HEIGHT) * row + TILE_MARGIN,
                              TILE_WIDTH,
                              TILE_HEIGHT])
