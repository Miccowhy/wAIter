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

    def _draw(self, tile):
        self.screen.blit(tile.image, tile.rect.topleft)
