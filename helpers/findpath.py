from constants.dimensions import GRID_LENGTH, GRID_WIDTH
# a star alghortihm implementation


class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def find_path(agent, grid, row_clicked, column_clicked):
    agent._check_direction(grid[row_clicked][column_clicked])
    costs = [[grid[row][col].step_cost for col in range(GRID_LENGTH)] for row in range(GRID_WIDTH)]
    path_grid_coords = astar(costs, (agent.current_tile.row_index, agent.current_tile.col_index),
                                    (row_clicked, column_clicked))
    print(path_grid_coords)
    path = []
    for cords in path_grid_coords:
        path.append(grid[cords[0]][cords[1]])

    print(grid.flatten())
    #path = [tile for tile in grid.flatten() for cords in path_grid_coords
    #        if tile.row_index == cords[0] and tile.col_index == cords[1]]
    print(costs)
    print(path_grid_coords)
    print(path)
    for element in path:
        print(element.row_index, element.col_index)
    #if agent.direction == Direction.LEFT or agent.direction == Direction.UP:
    #   path.reverse()
    return path


def astar(maze, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            #print(item)
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            if path[-1] == path[0]:
                path.remove(path[-1])
            return path[::-1]

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares

            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])
            if (node_position[0] > (len(maze) - 1) or node_position[0] < 0 
                    or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0):
                continue
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = current_node.g + 1
            child.h = (((child.position[0] - end_node.position[0]) ** 2)
                     + ((child.position[1] - end_node.position[1]) ** 2))
            child.f = child.g + child.h

            print(open_list) #debugging
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)
