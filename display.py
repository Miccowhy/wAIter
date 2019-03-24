from environment.restaurant import Restaurant
from environment.table import Table
from entities.waiter_agent import WaiterAgent
from os import system, name
import time


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


width = int(input('Enter width of the grid: '))
length = int(input('Enter length of the grid: '))

r = Restaurant(length, width)
grid = r.grid
agent = WaiterAgent(grid[0][0], r)
rows = grid.shape[0]
cols = grid.shape[1]

while True:
    clear()
    agent.choose_route()
    for x in range(0, rows):
        for y in range(0, cols):
            tile = grid[x, y]
            if tile.is_kitchen_entrance and type(tile.occupation) is not WaiterAgent:
                print('x ', end='')
            if type(tile.occupation) is Table:
                print('t ', end='')
            if type(tile.occupation) is WaiterAgent:
                print('o ', end='')
            if tile.occupation is None and not tile.is_kitchen_entrance:
                print('. ', end='')
        print()
    print()
    time.sleep(0.5)


print('\nx - kitchen entrance')
print('t - table')
print('. - empty tile')
