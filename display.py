from environment.restaurant import Restaurant
from environment.table import Table
from environment.tile import Tile 

width = int(input('Enter width of the grid: '))
length = int(input('Enter length of the grid: '))

r = Restaurant(length, width)
grid = r.grid
rows = grid.shape[0]
cols = grid.shape[1]

for x in range(0, rows):
    for y in range(0, cols):
        tile = grid[x, y]
        if tile.is_kitchen_entrance:
            print('x ', end='')
        if tile.occupation is not None:
            print('t ', end='')
        if tile.occupation is None and not tile.is_kitchen_entrance:
            print('. ', end='')

        """
        tile = grid[x, y]
        waiter = Tile(x, y)
        if tile is not None:
            print('t ', end='')
        if waiter.is_kitchen_entrance:
            print('x ', end='')
        if waiter is None and not tile.is_kitchen_entrance:
            print('. ', end='')
            """
    print()

print('\nx - kitchen entrance')
print('t - table')
print('. - empty tile')
