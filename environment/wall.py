from gui.drawable import Drawable
from constants.images import WALL, WINDOW
from constants.dimensions import TILE_HEIGHT, TILE_WIDTH


class Wall(Drawable):
    def __init__(self, is_window=False):
        super().__init__(width=TILE_WIDTH, height=TILE_HEIGHT)
        self.is_window = is_window
        super().__init__(loaded_image=WINDOW) if is_window else super().__init__(loaded_image=WALL)


