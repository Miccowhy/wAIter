import pygame
import os
import sys
from gui.spritesheet import Spritesheet
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT

# Using relative paths
root_path = os.path.dirname(sys.modules['__main__'].__file__)
graphics_path = os.path.join(root_path, 'resources/graphics')

WAITER = pygame.image.load(os.path.join(graphics_path, 'waiter.png'))
TABLE = pygame.image.load(os.path.join(graphics_path, 'table.png'))
ENTRANCE = pygame.image.load(os.path.join(graphics_path, 'entrance.png'))
FLOOR = pygame.image.load(os.path.join(graphics_path, 'floor_test.png'))

"""
def BORDER_IMAGES():
    tile_size = 128
    spritesheet = Spritesheet(os.path.join(graphics_path, 'border.png'))
    images = [spritesheet.load_strip((0, y, tile_size, tile_size), 3, colorkey=(0, 0, 0))
              for y in (0, tile_size, tile_size * 2)]
    return [pygame.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT)).convert_alpha()
            for strip in images for image in strip]
"""