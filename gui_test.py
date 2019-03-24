"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
from random import randint
import threading

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0) 
PINK = (255, 0 , 255)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5
 
def draw_grid():
    threading.Timer(1.0, draw_grid).start()

    
    for row in range(10):
            for column in range(10):
                color = WHITE

                # tile ready to order 
                if grid[row][column] == 1:
                    color = GREEN
                # eating right now
                if grid[row][column] == 2:
                    color = YELLOW
                # ready to clean dishes
                if grid[row][column] == -1:
                    color = RED
                # empty 
                if grid[row][column] == 0:
                    color = WHITE
                # entrance
                if grid[row][column] == 3:
                    color = BLACK
                # waiter 
                if grid[row][column] == 7:
                    color = PINK # tak wiem, to nie różowy
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
         
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell


#random population of tables
for x in range(10):
    grid[randint(0, 9)][randint(0, 9)] = 1
    grid[randint(0, 9)][randint(0, 9)] = 0
    grid[randint(0, 9)][randint(0, 9)] = -1
    grid[randint(0, 9)][randint(0, 9)] = 2

# waiter
grid[2][4] = 7
# entrance 
grid[0][5] = 3
grid[0][4] = 3 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("WalterAI")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    draw_grid() 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()