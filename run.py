import pygame
from gui.grid import draw_grid
from environment.restaurant import Restaurant
from entities.waiter_agent import WaiterAgent


pygame.init()

BLACK = (0, 0, 0)
GRID_WIDTH = 9
GRID_LENGTH = 9
WINDOW_SIZE = [500, 500]

screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("WalterAI")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

env = Restaurant(GRID_WIDTH, GRID_LENGTH)
agent = WaiterAgent(env.grid[0][0])

done = False
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Agent will choose random neighbouring tile to move into it
    agent.choose_route()
    # Set the screen background
    screen.fill(BLACK)
    # Draw the grid
    draw_grid(env, screen)
    # Limit to 60 frames per second
    clock.tick(5)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
pygame.quit()
