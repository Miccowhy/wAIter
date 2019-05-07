# Suppose our current tile is grid[0][1]
# State is hash, i.e.
# {'tile': grid[0][1], 'direction': Direction.DOWN}
# Goal is also a hash, i.e.
# {'tile': env.grid[2][6], 'direction': Direction.LEFT}
# Successor function returns successors, which are all possible states,
# reachable by single action from current state, i.e. (for our example state):
# {'tile': grid[0][2], 'direction': Direction.DOWN},
# {'tile': grid[0][1], 'direction': Direction.LEFT} etc...


import numpy as np
import math
from enum import Enum
from constants.movement import Direction


class Node:
    def __init__(self, tile, direction, goal, action=None, parent=None, cost=None):
        self.state = {'tile': tile, 'direction': direction}
        self.action = action
        self.parent = parent
        self.goal = goal
        if cost is None:
            cur_cords = (self.state['tile'].rect[0], self.state['tile'].rect[1])
            dest_cords = (self.goal['tile'].rect[0], self.goal['tile'].rect[1])
            cost = tile.step_cost + self._calculate_distance(cur_cords, dest_cords)
        if parent is not None:
            cost = cost + parent.cost
        self.cost = cost

    def goal_achieved(self):
        return (self.state['tile'] is self.goal['tile']
                and self.state['direction'] is self.goal['direction'])

    def _calculate_distance(self, a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def __eq__(self, other):
        return (self.state == other.state)


class Action(Enum):
    MOVE = 1
    ROTATE = 2


def astar_search(agent, goal):
    initial_node = Node(agent.current_tile, agent.direction, goal, cost=0)
    frontier = [initial_node]
    explored = []

    while frontier:
        node = frontier.pop()
        if node.goal_achieved():
            path = [node]
            while node.parent is not None:
                path.append(node.parent)
                node = node.parent
            path.reverse()
            return path

        explored.append(node.state)

        for successor in successors(node):
            if successor not in frontier and successor.state not in explored:
                frontier.append(successor)
            else:
                node_to_swap_index = find_higher_path_cost(successor, frontier)
                if node_to_swap_index:
                    frontier[node_to_swap_index] = successor

        frontier.sort(key=lambda node: node.cost, reverse=True)


def find_higher_path_cost(successor, frontier):
    for node in frontier:
        if successor.state == node.state and node.cost > successor.cost:
            return frontier.index(node)


def is_first_visit(node, explored, frontier):
    return node not in explored and node not in frontier


def successors(node):
    successors = []
    for dir in Direction:
        if dir is not node.state['direction']:
            action_with_dir = (Action.ROTATE, dir)
            successors.append(Node(node.state['tile'], dir, node.goal, action=action_with_dir,
                                   parent=node, cost=0))

    active_neighbors = [neighbor for neighbor in
                        node.state['tile'].unoccupied_neighbors_by_directions(node.state['direction'])
                        if neighbor['direction'] == node.state['direction']]

    for neighbor in active_neighbors:
        action_with_dir = (Action.MOVE, neighbor['direction'])
        successors.append(Node(neighbor['tile'], neighbor['direction'], node.goal,
                          action=action_with_dir, parent=node))
    return successors


def get_distance(a, b):
    return np.sum(np.abs(np.subtract(a, b)))


def map_without_parent(lis):
    return list(map(without_parent, lis))


def without_parent(successor):
    return {key: value for key, value in successor.items() if key != 'parent'}
