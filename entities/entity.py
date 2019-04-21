from gui.drawable import Drawable
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT


class Entity(Drawable):
    def __init__(self, current_tile, loaded_image=None):
        super().__init__(width=TILE_WIDTH, height=TILE_HEIGHT, loaded_image=loaded_image)
        self.current_tile = current_tile

    def move(self, destination_tile):
        self.current_tile.occupation = None
        destination_tile.occupation = self
        self.current_tile = destination_tile
