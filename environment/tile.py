class Tile:
    def __init__(self, row_index, col_index, occupation=None,
                 is_kitchen_entrance=False):
        self.row_index = row_index
        self.col_index = col_index
        self.occupation = occupation
        self.is_kitchen_entrance = is_kitchen_entrance
