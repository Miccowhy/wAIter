class Tile:
    def __init__(self, row_index, col_index, table=None, is_occupied=False,
                 is_kitchen_entrance=False):
        self.row_index = row_index
        self.col_index = col_index
        self.table = table
        self.is_occupied = is_occupied
        self.is_kitchen_entrance = is_kitchen_entrance
