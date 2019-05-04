import pygame
import math
from gui.map_renderer import MapRenderer
from helpers.findpath import find_path
from environment.restaurant import Restaurant
from entities.waiter_agent import WaiterAgent
from constants.colors import BLACK, GREEN
from constants.dimensions import WINDOW_SIZE, GRID_WIDTH, GRID_LENGTH


pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("WalterAI")
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

env = Restaurant(GRID_WIDTH, GRID_LENGTH)
agent = WaiterAgent(env.grid[0][0])
map_renderer = MapRenderer(env, screen, agent)
env.grid[0][0].occupation = agent
test_path = [env.grid[0][1], env.grid[0][2], env.grid[0][3], env.grid[0][4], env.grid[1][4],
             env.grid[2][4], env.grid[3][4], env.grid[4][4], env.grid[4][3], env.grid[4][2],
             env.grid[4][1], env.grid[4][0], env.grid[3][0], env.grid[2][0], env.grid[1][0],
             env.grid[0][0]]

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column_clicked = math.trunc(pos[0] / 50)
            row_clicked = math.trunc(pos[1] / 50)
            if column_clicked < GRID_WIDTH and row_clicked < GRID_LENGTH:
                try:
                    field_clicked.load_default_surface()
                except NameError:
                    pass
                try:
                    for field in way_to_go:
                        field.load_default_surface()
                except NameError:
                    pass
                way_to_go = find_path(agent, env.grid, row_clicked, column_clicked)
                #print(way_to_go)
                field_clicked = env.grid[row_clicked][column_clicked]
                field_clicked.color_surface(GREEN)
            
                agent.path = way_to_go.copy()
#                agent.path = test_path.copy()

    screen.fill(BLACK)
    map_renderer.render()
    # Limit frames per second
    clock.tick(30)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    agent.follow_path()

pygame.quit()
