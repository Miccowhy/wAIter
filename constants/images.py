import pygame
import os
import sys

# Using relative paths
root_path = os.path.dirname(sys.modules['__main__'].__file__)
graphics_path = os.path.join(root_path, 'resources/graphics')

TABLE = pygame.image.load(os.path.join(graphics_path, 'table.png'))
ENTRANCE = pygame.image.load(os.path.join(graphics_path, 'entrance.png'))
FLOOR = pygame.image.load(os.path.join(graphics_path, 'floor.png'))


def WAITER_SPRITESHEET():
    return pygame.image.load(os.path.join(graphics_path, 'waiter_spritesheet.png')).convert()
