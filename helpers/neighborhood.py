from environment.restaurant import Restaurant

class Neighborhood:
    def __init__(self, environment, row_index, col_index):
        self.environment = environment
        self.row_index = row_index
        self.col_index = col_index

    def neighbors(self, indices_differences=[(1, 0), (0, 1), (-1, 0), (0, -1)]):
        #indices_differences = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbors = []
        for diff in indices_differences:
            row = max(self.row_index + diff[0], 0)
            col = max(self.col_index + diff[1], 0)
            try:
                neighbors.append(self.environment.grid[row][col])
            except IndexError:
                continue
        return neighbors

    def quadrant(self):
        return self.neighbors(indices_differences=[(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)])

    def unoccupied_neighbors(self):
        return [neighbor for neighbor in self.neighbors() if neighbor.occupation is None]

    def unoccupied_quadrant(self):
        return [neighbor for neighbor in self.quadrant() if neighbor.occupation is None]