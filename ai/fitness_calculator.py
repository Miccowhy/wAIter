import numpy as np
import random
from collections import Counter
from environment.restaurant import Restaurant
from constants.desirability import WINDOW_VIEW, CLOSE_TABLES, ENTRANCE_BARRICADE, NEARBY_WALL
from constants.dimensions import GRID_WIDTH, GRID_LENGTH
from constants.genetics import MAX_MUTATIONS, GENE_STABILITY, TABLES_AMOUNT, REPRODUCTIONS, SWAPPING_TRESHOLD

class Fitness:
    def __init__(self, habitat, available_positions = [], population = {}):
        self.available_positions = available_positions
        self.population = population
        self.habitat = habitat
        for col in range(GRID_LENGTH):
            for row in range(GRID_WIDTH):
                if habitat[col][row].occupation is None:
                    self.available_positions.append([col, row])
        self.chromosome_length = len(available_positions.append)

    def create_ancestors(self):
        for i in range(2):
            ancestor = []
            random_positions = random.sample(self.available_positions, TABLES_AMOUNT)
            for item in self.available_positions:
                ancestor.append(1) if item in random_positions else ancestor.append(0)
                self.population[ancestor] = self.compute_score(ancestor)

    def descendants_iteration(self):
        for turns in range(REPRODUCTIONS):
            parents = Counter(self.population).most_common(2)
            descendants = [parents[0][0][:round(self.chromosome_length * SWAPPING_TRESHOLD)] + parents[1][0][round(self.chromosome_length * SWAPPING_TRESHOLD):], parents[1][0][:round(self.chromosome_length * SWAPPING_TRESHOLD)] + parents[0][0][round(self.chromosome_length * SWAPPING_TRESHOLD):]]
            for chromosome in descendants:
                chromosome = self.mutation(chromosome)
                self.population[chromosome] = self.compute_score(chromosome)
        return max(self.population, key=self.population.get)

    def mutation(self, descentant):
        genes = random.sample(range(descentant), random.randint(MAX_MUTATIONS))
        for gene in genes:
            if random.random() > GENE_STABILITY:
                descentant[gene] = 1 if descentant[gene] = 0 else 0
        return descentant

    def compute_score(self, chromosome):
        positions = []
        evolution_grid = [[0 for i in range(GRID_WIDTH)] for i in range(GRID_LENGTH)]
        for value in self.chromosome_length:
            #positions.append(self.habitat.grid[value[0]][value[1]]) if chromosome[value]
            if chromosome[value]:
                tile = self.habitat.grid[value[0]][value[1]]
                evolution_grid[value[0]][value[1]]+= ENTRANCE_BARRICADE if tile.is_restaurant_entrance

                for element in tile.neigbor():
                    if isinstance(element.occupation, Wall):
                        evolution_grid[value[0]][value[1]] += WINDOW_VIEW if element.occupation.is_window else evolution_grid[value[0]][value[1]] += NEARBY_WALL

                for element in tile.quadrant():
                    evolution_grid[element.col_index][element.row_index] += CLOSE_TABLES
'''        
        for element in env[col][row].neigbor():
            if isinstance(element.occupation, Wall):
            evolution_score += WINDOW_VIEW if element.occupation.is_window else NEARBY_WALL
'''