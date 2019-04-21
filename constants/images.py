import pygame
import os
import sys

# Using relative paths
root_path = os.path.dirname(sys.modules['__main__'].__file__)
graphics_path = os.path.join(root_path, 'resources/graphics')

WAITER = pygame.image.load(os.path.join(graphics_path, 'waiter.bmp'))
TABLE = pygame.image.load(os.path.join(graphics_path, 'table.bmp'))
ENTRANCE = pygame.image.load(os.path.join(graphics_path, 'entrance.bmp'))
FLOOR = pygame.image.load(os.path.join(graphics_path, 'floor.bmp'))