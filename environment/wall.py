from gui.drawable import Drawable
from constants.images import WALL, WINDOW
from constants.dimensions import TILE_HEIGHT, TILE_WIDTH


class Wall(Drawable):
    def __init__(self):
        super().__init__(width=TILE_WIDTH, height=TILE_HEIGHT, loaded_image=WALL)


class Window(Drawable):
    def __init__(self):
        super().__init__(width=TILE_WIDTH, height=TILE_HEIGHT, loaded_image=WINDOW)
