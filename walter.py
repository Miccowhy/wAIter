import pygame
import math
from helpers.pathfinding import astar_search
from gui.map_renderer import MapRenderer
from environment.restaurant import Restaurant
from entities.waiter_agent import WaiterAgent
from constants.colors import BLACK, GREEN, YELLOW
from constants.dimensions import WINDOW_SIZE, GRID_WIDTH, GRID_LENGTH
from constants.movement import Direction


pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("WalterAI")
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

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
            field_clicked = env.grid[row_clicked][column_clicked]
            field_clicked.color_surface(GREEN)

            goal = {'tile': field_clicked, 'direction': Direction.DOWN}
            node_seq = astar_search(agent, goal)
            agent.actions = [node.action for node in node_seq]
            tile_seq = [node.state['tile'] for node in node_seq]
            for tile in tile_seq:
                tile.color_surface(YELLOW)

    screen.fill(BLACK)

    try:
        if not agent.actions:
            for tile in env.grid.flatten():
                tile.load_default_surface()
    except NameError:
        pass

    map_renderer.render()
    # Limit frames per second
    clock.tick(30)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    agent.follow_actions()

pygame.quit()
