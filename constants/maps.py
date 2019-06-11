import pygame
import os
import sys

# Using relative paths
root_path = os.path.dirname(sys.modules['__main__'].__file__)
maps_path = os.path.join(root_path, 'resources/maps')

MAP = os.path.join(maps_path, 'default.txt')