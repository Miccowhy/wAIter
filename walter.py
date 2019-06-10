import pygame
import random
from ai.pathfinding import astar_search
from ai.genetic_furnishing import Genetic_fitness
from gui.map_renderer import MapRenderer
from environment.restaurant import Restaurant
from environment.table import Table
from entities.waiter_agent import WaiterAgent
from entities.customer import Customer
from constants.colors import BLACK
from constants.dimensions import WINDOW_SIZE, GRID_WIDTH, GRID_LENGTH
from constants.movement import Direction
from constants.datasets import PIZZAS_DF
from constants.conversations import PIZZA_CONVERSATION

from itertools import chain

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("WalterAI")
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

env = Restaurant(GRID_LENGTH, GRID_WIDTH)
print(Genetic_fitness(env))

agent = WaiterAgent(env.grid[0][5])
customer = Customer(env.grid[8][4], direction=Direction.UP)
env.grid[0][5].occupation = agent
env.grid[8][4].occupation = customer
map_renderer = MapRenderer(env, screen, agent, customer)
conversation_finished = False

# Simple scenario - customer enters the restaurant and then waiter serves him
customer_goal = {'tile': env.grid[2][5], 'direction': Direction.DOWN}
cus_node_seq = astar_search(customer, customer_goal)
agent_goal = {'tile': env.grid[1][4], 'direction': Direction.RIGHT}
agent_node_seq = astar_search(agent, agent_goal)
customer.actions = [node.action for node in cus_node_seq]
agent.actions = [node.action for node in agent_node_seq]
'''
for i in range(GRID_WIDTH):
    for j in range(GRID_LENGTH):
        if isinstance(env.grid[i][j].occupation, Table):
            print(str(i) + ", " + str(j))
'''

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    map_renderer.render()
    # Limit frames per second
    clock.tick(30)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    customer.follow_actions()
    if not customer.actions:
        agent.follow_actions()
    if not agent.actions and not conversation_finished:
        print('Pizzas:')
        print(PIZZAS_DF)
        predictions = customer.decision_tree.predict(PIZZAS_DF)
        probs = customer.decision_tree.predict_proba(PIZZAS_DF)
        print('Predictions:')
        print(predictions)
        print('Probabilities:')
        print(probs)

        suggested_pizzas = []
        for index in range(len(predictions)):
            if predictions[index] == 1:
                suggested_pizzas.append(PIZZAS_DF.iloc[index].name)

        print('Suggested pizzas:', suggested_pizzas)
        map_renderer.text_queue = PIZZA_CONVERSATION(random.choice(suggested_pizzas))
        conversation_finished = True

pygame.quit()
