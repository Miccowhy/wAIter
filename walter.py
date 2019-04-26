import pygame
from gui.map_renderer import MapRenderer
from environment.restaurant import Restaurant
from entities.waiter_agent import WaiterAgent
from constants.colors import BLACK
from constants.dimensions import WINDOW_SIZE, GRID_WIDTH, GRID_LENGTH


pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("WalterAI")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

env = Restaurant(GRID_WIDTH, GRID_LENGTH)
agent = WaiterAgent(env.grid[0][0])
map_renderer = MapRenderer(env, screen)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    map_renderer.render()
    # Limit frames per second
    clock.tick(5)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    agent.choose_route()

pygame.quit()
