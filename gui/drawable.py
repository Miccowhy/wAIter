import pygame


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
            self.image = loaded_image
            # Scale image to tilesize
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.rect = self.image.get_rect()
            self.width = self.rect.width
            self.height = self.rect.height

        self.image.convert()
        self.rect = self.image.get_rect()
