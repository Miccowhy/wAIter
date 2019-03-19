import numpy as np

class Restaurant:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Tile:
    def __init__(self, table, kitchen_entrance?):
        self.table = table
        self.kitchen_entrance? = kitchen_entrance?

class Table:
    def __init__(self, customers = [], is_dirty? = False):
        self.customers = customers
        self.is_dirty? = is_dirty?

    @is_dirty?.setter
    def is_dirty?(self, is_dirty?):
        if !__is_boolean?(is_dirty?):
            raise ValueError('is_dirty? must be a boolean!')

    def __is_boolean?(x):
        return type(x) == bool
