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
                tile = TileGrid(width=45, height=45, color=BROWN, loadedimage=TABLE)
            elif type(tile.occupation) is WaiterAgent:
                color = GREEN
                tile = TileGrid(width=45, height=45, color=GREEN, loadedimage=WAITER)
            elif tile.is_kitchen_entrance:
                color = YELLOW
                tile = TileGrid(width=45, height=45, color=YELLOW, loadedimage=ENTRANCE)
            else:
                color = WHITE
                tile = TileGrid(width=45, height=45, color=WHITE, loadedimage=FLOOR)
            # comment below in future, but dont delete
            """
            pygame.draw.rect(screen,
                             color,
                             [(TILE_MARGIN + TILE_WIDTH) * column + TILE_MARGIN,
                              (TILE_MARGIN + TILE_HEIGHT) * row + TILE_MARGIN,
                              TILE_WIDTH,
                              TILE_HEIGHT])
            """
            #screen.blit() goes here instead of pygame.draw.rect()
            screen.blit(tile, [(TILE_MARGIN + TILE_WIDTH) * column + TILE_MARGIN,
                              (TILE_MARGIN + TILE_HEIGHT) * row + TILE_MARGIN,
                              TILE_WIDTH,
                              TILE_HEIGHT])
            #displays none for now, dont have any idea, Szymon might know <3
            
