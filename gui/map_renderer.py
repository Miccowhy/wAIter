from constants.images import ENTRANCE


class MapRenderer:
    def __init__(self, environment, screen):
        self.environment = environment
        self.screen = screen

    def render(self):
        self._draw_grid()

    def _draw_grid(self):
        for row in range(self.environment.grid_width):
            for col in range(self.environment.grid_length):
                tile = self.environment.grid[row][col]
                if tile.is_kitchen_entrance:
                    self._draw_on_tile(tile, image=ENTRANCE)
                else:
                    self._draw_on_tile(tile)
                if tile.occupation is not None:
                    self._draw_on_tile(tile.occupation)

    def _draw_on_tile(self, obj, image=None):
        if image is None:
            image = obj.image
        self.screen.blit(image, obj.rect.topleft)
