import numpy as np
import random
from collections import Counter
from environment.restaurant import Restaurant
from environment.table import Table
from environment.wall import Wall, Window
from helpers.neighborhood import Neighborhood
from constants.desirability import WINDOW_VIEW, CLOSE_TABLES, ENTRANCE_BARRICADE, NEARBY_WALL
from constants.dimensions import GRID_WIDTH, GRID_LENGTH
from constants.genetics import MAX_MUTATIONS, GENE_STABILITY, TABLES_AMOUNT, REPRODUCTIONS, SWAPPING_TRESHOLD

class Genetic_fitness:
    def __init__(self, env, population = {}):
        self.available_positions = env.return_arrangement()[3]
        self.population = population
        self.habitat = env.get_grid()
        self.chromosome_length = len(self.available_positions)
        self.final_positions = None
        self.create_ancestors()

    def create_ancestors(self):
        for i in range(2):
            ancestor = []
            random_positions = random.sample(self.available_positions, TABLES_AMOUNT)
            for item in self.available_positions:
                ancestor.append(1) if item in random_positions else ancestor.append(0)
            self.population[tuple(ancestor)] = self.compute_score(ancestor)
        self.descendants_iteration()

    def descendants_iteration(self):
        positions = []
        for turns in range(REPRODUCTIONS):
            parents = Counter(self.population).most_common(2)
            descendants = [parents[0][0][:round(self.chromosome_length * SWAPPING_TRESHOLD)] + parents[1][0][round(self.chromosome_length * SWAPPING_TRESHOLD):], parents[1][0][:round(self.chromosome_length * SWAPPING_TRESHOLD)] + parents[0][0][round(self.chromosome_length * SWAPPING_TRESHOLD):]]
            for chromosome in descendants:
                chromosome = self.mutation(chromosome)
                self.population[tuple(chromosome)] = self.compute_score(chromosome)
        for value in range(self.chromosome_length):
            if max(self.population, key=self.population.get)[value]:
                positions.append(self.available_positions[value])
        self.final_positions = positions
        print("Scores of top 100 of population")
        for subject in range(100):
            print(Counter(self.population).most_common(100)[subject][1], end=" ")

    def mutation(self, descentant):
        genes = random.sample(range(len(descentant)), random.randrange(MAX_MUTATIONS))
        chromosome = list(descentant)
        for gene in genes:
            if random.random() > GENE_STABILITY:
                chromosome[gene] = 1 if chromosome[gene] == 0 else 0
        return tuple(chromosome)

    def compute_score(self, chromosome):
        overall_score = 0
        evolution_grid = [[0 for i in range(GRID_WIDTH)] for j in range(GRID_LENGTH)]
        for value in range(self.chromosome_length):
            if chromosome[value]:
                pos = self.available_positions[value]
                eval_tile = self.habitat[pos[0]][pos[1]]
                for val in Neighborhood().neighbors(pos[0], pos[1]):
                    if self.habitat[val[0]][val[1]] == "W": evolution_grid[pos[0]][pos[1]] += NEARBY_WALL
                    if self.habitat[val[0]][val[1]] == "O": evolution_grid[pos[0]][pos[1]] += WINDOW_VIEW
                for val in Neighborhood().quadrant(pos[0], pos[1]):
                    if self.habitat[val[0]][val[1]] == "E": evolution_grid[pos[0]][pos[1]]+= ENTRANCE_BARRICADE
                    evolution_grid[val[0]][val[1]] += CLOSE_TABLES
                overall_score += evolution_grid[pos[0]][pos[1]]
        return overall_score

    def get_position(self):
        return self.final_positions