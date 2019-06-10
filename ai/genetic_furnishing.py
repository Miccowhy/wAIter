import numpy as np
import random
from collections import Counter
from environment.restaurant import Restaurant
from environment.wall import Wall, Window
#from helpers.neighborhood import Neighborhood
from constants.desirability import WINDOW_VIEW, CLOSE_TABLES, ENTRANCE_BARRICADE, NEARBY_WALL
from constants.dimensions import GRID_WIDTH, GRID_LENGTH
from constants.genetics import MAX_MUTATIONS, GENE_STABILITY, TABLES_AMOUNT, REPRODUCTIONS, SWAPPING_TRESHOLD

class Genetic_fitness:
    def __init__(self, habitat, available_positions = [], population = {}):
        self.available_positions = available_positions
        self.population = population
        self.habitat = habitat
        for col in range(GRID_LENGTH):
            for row in range(GRID_WIDTH):
                if habitat.grid[col][row].occupation is None:
                    self.available_positions.append([col, row])
        self.chromosome_length = len(available_positions)
        self.create_ancestors()

    def create_ancestors(self):
        for i in range(2):
            ancestor = []
            random_positions = random.sample(self.available_positions, TABLES_AMOUNT)
            #print(self.available_positions)
            #print(random_positions)
            for item in self.available_positions:
                ancestor.append(1) if item in random_positions else ancestor.append(0)
            #print(ancestor)
            self.population[tuple(ancestor)] = self.compute_score(ancestor)
        self.descendants_iteration()

    def descendants_iteration(self):
        for turns in range(REPRODUCTIONS):
            print(self.population)
            parents = Counter(self.population).most_common(2)
            descendants = [parents[0][0][:round(self.chromosome_length * SWAPPING_TRESHOLD)] + parents[1][0][round(self.chromosome_length * SWAPPING_TRESHOLD):], parents[1][0][:round(self.chromosome_length * SWAPPING_TRESHOLD)] + parents[0][0][round(self.chromosome_length * SWAPPING_TRESHOLD):]]
            for chromosome in descendants:
                chromosome = self.mutation(chromosome)
                self.population[tuple(chromosome)] = self.compute_score(chromosome)
        return max(self.population, key=self.population.get)

    def mutation(self, descentant):
        genes = random.sample(range(descentant), random.randint(MAX_MUTATIONS))
        for gene in genes:
            if random.random() > GENE_STABILITY:
                descentant[gene] = 1 if descentant[gene] == 0 else 0
        return descentant

    def compute_score(self, chromosome):
        positions = []
        evolution_grid = [[0 for i in range(GRID_WIDTH)] for i in range(GRID_LENGTH)]
        for value in range(self.chromosome_length):
            if chromosome[value]:
                pos = self.available_positions[value]
                print(pos)
                eval_tile = self.habitat.grid[pos[0]][pos[1]]
                print(eval_tile)
                if eval_tile.is_restaurant_entrance: evolution_grid[pos[0]][pos[1]]+= ENTRANCE_BARRICADE

                #for element in Neighborhood.neighbors(habitat, pos[0], pos[1]):
                for element in eval_tile.neighbors():
                    if eval_tile.is_restaurant_entrance: evolution_grid[pos[0]][pos[1]]+= ENTRANCE_BARRICADE 
                    if isinstance(element.occupation, Wall): evolution_grid[pos[0]][pos[1]] += NEARBY_WALL
                    if isinstance(element.occupation, Window): evolution_grid[pos[0]][pos[1]] += WINDOW_VIEW

                for element in eval_tile.quadrant():
                    evolution_grid[element.col_index][element.row_index] += CLOSE_TABLES