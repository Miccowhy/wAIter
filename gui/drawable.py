import pygame
from constants.colors import YELLOW


class Drawable(object):
    def __init__(self, width=None, height=None, color=None, loaded_image=None):
        self.width = width
        self.height = height
        self.color = color

        self.image = pygame.Surface((self.width, self.height))
        if self.color is not None:
            self.image.fill(self.color)

        self.loaded_image = loaded_image
        if self.loaded_image is not None:
            self.image = self.loaded_image.copy()
            # Scale image to tilesize
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.rect = self.image.get_rect()
            self.width = self.rect.width
            self.height = self.rect.height

        self.image.convert()
        self.rect = self.image.get_rect()

    def load_default_surface(self):
        self.image = pygame.Surface((self.width, self.height))
        self.image = self.loaded_image
        # Scale image to tilesize
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.width = self.rect.width
        self.height = self.rect.height
        self.image.convert()

    def color_surface(self, color=YELLOW):
        self.image.fill((color), special_flags=pygame.BLEND_MULT)
        self.image.convert()
