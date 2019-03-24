class Entity:
    def __init__(self, current_tile, environment):
        self.current_tile = current_tile
        self.environment = environment

    def move(self, destination_tile):
        self.current_tile.occupation = None
        destination_tile.occupation = self
        self.current_tile = destination_tile
