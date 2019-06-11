import pygame
import random
from ai.pathfinding import astar_search
from ai.genetic_furnishing import Genetic_fitness
from gui.map_renderer import MapRenderer
from environment.restaurant import Restaurant
from environment.mapper import Mapper
from entities.waiter_agent import WaiterAgent
from entities.customer import Customer
from constants.colors import BLACK
from constants.dimensions import WINDOW_SIZE, GRID_WIDTH, GRID_LENGTH
from constants.movement import Direction
from constants.datasets import PIZZAS_DF
from constants.conversations import PIZZA_CONVERSATION


pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("WalterAI")
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.8)

mapper = Mapper()
fit = Genetic_fitness(mapper)
positions = fit.get_position()
mapper.update_tables(positions)
env = Restaurant(GRID_LENGTH, GRID_WIDTH)
arr = mapper.return_arrangement()
env.push_grid_positions(arr)
entry = arr[2]

agent = WaiterAgent(env.grid[entry[0][0], entry[0][1]])
customer = Customer(env.grid[entry[1][0], entry[1][1]], direction=Direction.UP)
env.grid[entry[0][0], entry[0][1]].occupation = agent
env.grid[entry[1][0], entry[1][1]].occupation = customer
map_renderer = MapRenderer(env, screen, agent, customer)
conversation_finished = False

# Simple scenario - customer enters the restaurant and then waiter serves him
cg, ag = mapper.seat_customer()
customer_goal = {'tile': env.grid[cg[0]][cg[1]], 'direction': Direction.UP}
cus_node_seq = astar_search(customer, customer_goal)
customer.actions = [node.action for node in cus_node_seq]
agent_goal = {'tile': env.grid[ag[0]][ag[1]], 'direction': Direction.DOWN}
agent_node_seq = astar_search(agent, agent_goal)
agent.actions = [node.action for node in agent_node_seq]


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
