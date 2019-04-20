import pygame

class TileGrid(object):
    def __init__(self, width=None, height=None, color=None, loadedimage=None):
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        if self.color != None:
            self.image.fill(self.color)
        self.loadedimage = loadedimage
        if self.loadedimage != None:
            self.image = loadedimage

            # Scale image to tilesize
            self.image = pygame.transform.scale(self.image,(self.width,self.height))

            self.rect = self.image.get_rect()
            self.width = self.rect.width
            self.height = self.rect.height
        self.image.convert()
        self.rect = self.image.get_rect()
