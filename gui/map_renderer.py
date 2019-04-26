class MapRenderer:
    def __init__(self, environment, screen):
        self.environment = environment
        self.screen = screen

    def render(self):
        self._draw_grid()

    def _draw_grid(self):
        for row in range(self.environment.grid_width):
            for col in range(self.environment.grid_length):
                self._draw_on_tile(self.environment.grid[row][col])

    def _draw_on_tile(self, tile):
        self.screen.blit(tile.image, tile.rect.topleft)
        if tile.occupation is not None:
            self.screen.blit(tile.occupation.image, tile.occupation.rect.topleft)
