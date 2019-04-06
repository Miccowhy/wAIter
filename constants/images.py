# Loaded tiles
import pygame
import os

# Using relative paths
current_path = os.path.dirname(__file__)
tiles_path = os.path.join(current_path, 'tiles')

WAITER = pygame.image.load(os.path.join(tiles_path, 'waiter.bmp'))
TABLE = pygame.image.load(os.path.join(tiles_path, 'table.bmp'))
ENTRANCE = pygame.image.load(os.path.join(tiles_path, 'entrance.bmp'))
FLOOR = pygame.image.load(os.path.join(tiles_path, 'floor.bmp'))