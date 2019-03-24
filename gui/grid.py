import pygame
from entities.waiter_agent import WaiterAgent
from environment.table import Table
from constants.colors import BROWN, GREEN, YELLOW, WHITE
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT, TILE_MARGIN


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
