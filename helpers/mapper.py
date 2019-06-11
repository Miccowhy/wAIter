from constants.maps import MAP
from constants.dimensions import GRID_LENGTH, GRID_WIDTH

class Mapper:
    def __init__(self, walls=[], windows=[], entrances=[], empty=[], tables=[], grid=[]):
        self.walls = walls
        self.windows = windows
        self.entrances = entrances
        self.empty = empty
        self.tables = tables
        self.grid = grid
        self.map_objects()

    def map_objects(self):
        with open(MAP, 'r') as f:
        #with open("resources/maps/default.txt", 'r') as f:
            self.grid = f.read().splitlines()
            for i in range(GRID_LENGTH):
                for j in range(GRID_WIDTH):
                    if self.grid[i][j] == "W": self.walls.append([i, j])
                    if self.grid[i][j] == "O": self.windows.append([i, j])
                    if self.grid[i][j] == "E": self.entrances.append([i, j])
                    if self.grid[i][j] == " ": self.empty.append([i, j])
    
    def return_arrangement(self):
        return self.walls, self.windows, self.entrances, self.empty, self.tables

    def get_grid(self):
        return self.grid

    def update_tables(self, tables):
        self.tables = tables
        for element in self.tables:
            self.empty.remove(element)

    def test(self, positions):
        walls, windows, entrances, empty, tables = positions
        print("Walls:")
        print(walls)