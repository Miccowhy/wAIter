import pygame
from constants.images import BANANA
from constants.movement import BANANA_COST


class MapRenderer:
    def __init__(self, environment, screen, agent):
        self.environment = environment
        self.screen = screen
        self.agent = agent

    def render(self):
        self._draw_grid()
        self._draw(self.agent)

    def _draw_grid(self):
        for row in range(self.environment.grid_width):
            for col in range(self.environment.grid_length):
                tile = self.environment.grid[row][col]
                self._draw(tile)
                if tile.occupation is not None:
                    self._draw(tile.occupation)
                if tile.cost == BANANA_COST:
                    self._draw(tile, image=BANANA)

    def _draw(self, tile, image=None):
        if image is None:
            self.screen.blit(tile.image, tile.rect.topleft)
        else:
            self.screen.blit(pygame.transform.scale(image, (50, 50)), tile.rect.topleft)
