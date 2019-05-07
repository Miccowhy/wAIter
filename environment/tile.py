from gui.drawable import Drawable
from constants.dimensions import TILE_WIDTH, TILE_HEIGHT
from constants.images import FLOOR, ENTRANCE
from constants.movement import Direction


class Tile(Drawable):
    def __init__(self, environment, row_index, col_index, occupation=None,
                 is_kitchen_entrance=False, color=None, loaded_image=FLOOR, step_cost=1):
        if is_kitchen_entrance:
            loaded_image = ENTRANCE
        super().__init__(width=TILE_WIDTH, height=TILE_HEIGHT, color=color,
                         loaded_image=loaded_image)
        self.environment = environment
        self.row_index = row_index
        self.col_index = col_index
        self.occupation = occupation
        self.is_kitchen_entrance = is_kitchen_entrance
        self.step_cost = step_cost

    def neighbors(self):
        indices_differences = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbors = []
        for diff in indices_differences:
            row = max(self.row_index + diff[0], 0)
            col = max(self.col_index + diff[1], 0)
            try:
                neighbors.append(self.environment.grid[row][col])
            except IndexError:
                continue
        return neighbors

    def unoccupied_neighbors(self):
        return [neighbor for neighbor in self.neighbors() if neighbor.occupation is None]

    def unoccupied_neighbors_by_directions(self):
        return [{'tile': neighbor, 'direction': Direction.obtain_direction(self, neighbor)}
                for neighbor in self.unoccupied_neighbors()]
