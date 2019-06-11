from constants.dimensions import GRID_LENGTH, GRID_WIDTH

class Neighborhood:
    def __init__(self):
        pass

    def neighbors(self, row_index, col_index, indices_differences=[(1, 0), (0, 1), (-1, 0), (0, -1)]):
        neighbors = []
        for diff in indices_differences:
            if row_index + diff[0] >= 0 and row_index + diff[0] < GRID_WIDTH:
                row = row_index + diff[0] 
            else: continue
            if row_index + diff[1] >= 0 and col_index + diff[1] < GRID_LENGTH:
                col = col_index + diff[1] 
            else: continue
            neighbors.append([row, col])
        return neighbors

    def quadrant(self, row_index, col_index):
        return self.neighbors(row_index, col_index, indices_differences=[(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)])