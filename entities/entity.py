class Entity:
    def __init__(self, current_tile):
        self.current_tile = current_tile

    def move(self, destination_tile):
        self.current_tile.occupation = None
        destination_tile.occupation = self
        self.current_tile = destination_tile
