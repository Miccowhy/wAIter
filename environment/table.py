from gui.drawable import Drawable
from constants.images import TABLE
from constants.dimensions import TILE_HEIGHT, TILE_WIDTH


class Table(Drawable):
    def __init__(self, customers=[], is_dirty=False):
        super().__init__(width=TILE_WIDTH, height=TILE_HEIGHT, loaded_image=TABLE)
        self.customers = customers
        self.is_dirty = is_dirty
