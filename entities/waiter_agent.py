import random
import numpy as np
from .entity import Entity


class WaiterAgent(Entity):
    def __init__(self, current_tile):
        super(WaiterAgent, self).__init__(current_tile)

    # Currently, agent chooses his route randomly, based on possible moves list
    def choose_route(self):
        possible_moves = np.array(
                         [tile for tile in
                          self.current_tile.neighbors()
                          if tile.occupation is None
                          and not tile.is_kitchen_entrance])  # Currently, agent avoids kitchen entrance
        self.move(random.choice(possible_moves))