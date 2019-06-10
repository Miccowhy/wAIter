import numpy
from helpers.findpath import astar
#maze = numpy.random.randint(100, size=(9, 9))
#print(maze)

maze = [[1, 1, 0, 3, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 3, 0, 0],
        [1, 1, 4, 0, 1, 0, 1, 1, 0, 1],
        [1, 1, 5, 0, 1, 0, 6, 0, 25, 0],
        [1, 1, 2, 0, 1, 0, 0, 1, 0, -2],
        [23, 1, 0, 0, 0, 0, 32, 0, 0, 0],
        [1, 1, 6, 0, 1, 5, 2, 3, 9, 1],
        [1, 1, 0, 0, 1, 0, 3, 3, 9, 1],
        [1, 1, 1, 1, 1, 1, 1, 6, 9, 9]]

start = (0,0)
end = (8,8)

print(astar(maze, start, end))



