from .entity import Entity
from constants.images import WAITER_SPRITESHEET


class WaiterAgent(Entity):
    def __init__(self, current_tile):
        super().__init__(current_tile=current_tile, loaded_image=WAITER_SPRITESHEET())
