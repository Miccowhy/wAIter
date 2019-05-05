import pygame
import math
from helpers.pathfinding import astar_search
from gui.map_renderer import MapRenderer
from environment.restaurant import Restaurant
from entities.waiter_agent import WaiterAgent
from constants.colors import BLACK
from constants.dimensions import WINDOW_SIZE, GRID_WIDTH, GRID_LENGTH
from constants.movement import Direction

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("WalterAI")
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

env = Restaurant(GRID_WIDTH, GRID_LENGTH)
agent = WaiterAgent(env.grid[0][0])
env.grid[0][0].occupation = agent
map_renderer = MapRenderer(env, screen, agent)


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column_clicked = math.trunc(pos[0] / 50)
            row_clicked = math.trunc(pos[1] / 50)
            goal = {'tile': env.grid[row_clicked][column_clicked], 'direction': Direction.DOWN}
            states_sequence = astar_search(agent, goal)
            agent.path = [state['tile'] for state in states_sequence]

    screen.fill(BLACK)
    map_renderer.render()
    # Limit frames per second
    clock.tick(30)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    agent.follow_path()

pygame.quit()
