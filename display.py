import environment as env

width = int(input('Enter width of the grid: '))
length = int(input('Enter length of the grid: '))

r = env.Restaurant(length, width)
grid = r.grid
rows = grid.shape[0]
cols = grid.shape[1]

for x in range(0, rows):
    for y in range(0, cols):
        tile = grid[x, y]
        table = tile.table
        if table is not None:
            print('t ', end='')
        if tile.is_kitchen_entrance:
            print('x ', end='')
        if table is None and not tile.is_kitchen_entrance:
            print('. ', end='')
    print()

print('\nx - kitchen entrance')
print('t - table')
print('. - empty tile')
