import pygame
from .tile_grid import TileGrid
from entities.waiter_agent import WaiterAgent
from environment.table import Table
from constants.colors import BROWN, GREEN, YELLOW, WHITE
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT, TILE_MARGIN
from constants.images import WAITER, TABLE, ENTRANCE, FLOOR

def draw_grid(environment, screen):
    for row in range(environment.grid_width):
        for column in range(environment.grid_length):
            tile = environment.grid[row][column]

            if type(tile.occupation) is Table:
                color = BROWN
                #tile = Tile(width=24, height=24, color=color, loadedimage=TABLE)
            elif type(tile.occupation) is WaiterAgent:
                color = GREEN
                #tile = Tile(width=24, height=24, color=color, loadedimage=AGENT)
            elif tile.is_kitchen_entrance:
                color = YELLOW
                #tile = Tile(width=24, height=24, color=color, loadedimage=ENTRANCE)
            else:
                color = WHITE
                #tile = Tile(width=24, height=24, color=color, loadedimage=FLOOR)
            pygame.draw.rect(screen,
                             color,
                             [(TILE_MARGIN + TILE_WIDTH) * column + TILE_MARGIN,
                              (TILE_MARGIN + TILE_HEIGHT) * row + TILE_MARGIN,
                              TILE_WIDTH,
                              TILE_HEIGHT])
            #pygame.screen.blit() goes here instead of pygame.draw.rect()
