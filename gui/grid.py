import pygame
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT, TILE_MARGIN
from constants.images import ENTRANCE
from constants.images import BORDER_IMAGES


def draw_grid(environment, screen):
    for row in range(environment.grid_width):
        for column in range(environment.grid_length):
            tile = environment.grid[row][column]
            if tile.is_kitchen_entrance:
                _draw_on_tile(screen, tile, image=ENTRANCE)
            else:
                _draw_on_tile(screen, tile)
            if tile.occupation is not None:
                _draw_on_tile(screen, tile.occupation)


def _draw_on_tile(screen, obj, image=None):
    if image is None:
        image = obj.image
    screen.blit(image, obj.rect.topleft)


"""
def _draw_border(environment, screen):
    screen.blit(BORDER_IMAGES()[0], [190, 135, 50, 50])
    for x in range(environment.grid_width - 2):
        screen.blit(BORDER_IMAGES()[1], [200 + TILE_WIDTH * (x + 1), 135, 50, 50])
    screen.blit(BORDER_IMAGES()[2], [200 + TILE_WIDTH * (environment.grid_width - 1), 150, 50, 50])
    for y in range(environment.grid_length - 2):
        screen.blit(BORDER_IMAGES()[3], [190, 150 + TILE_HEIGHT * (y + 1), 50, 50])
        screen.blit(BORDER_IMAGES()[3], [190 + TILE_WIDTH * (environment.grid_width - 1),
                    150 + TILE_HEIGHT * (y + 1), 50, 50])
"""

"""
def _scale_image(image):
    return pygame.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT))
"""

"""
def _draw_object(screen, column, row, image):
    screen.blit(image, [200 +(TILE_MARGIN + TILE_WIDTH) * column + TILE_MARGIN,
                        150 +(TILE_MARGIN + TILE_HEIGHT) * row + TILE_MARGIN,
                        TILE_WIDTH, TILE_HEIGHT])
"""
