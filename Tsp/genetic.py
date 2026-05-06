import numpy as np
import random
import math

def genetic_algorithm(dist_matrix, pop_size=50, generations=200):
    """Population-based search using Crossover and Mutation."""
    num_nodes = len(dist_matrix)
    
    def create_individual():
        ind = list(range(num_nodes))
        random.shuffle(ind)
        return ind

    population = [create_individual() for _ in range(pop_size)]
    
    for _ in range(generations):
        population = sorted(population, key=lambda x: total_distance(x, dist_matrix))
        new_pop = population[:10] # Elitism
        
        while len(new_pop) < pop_size:
            # Ordered Crossover (OX)
            p1, p2 = random.sample(population[:25], 2)
            start, end = sorted(random.sample(range(num_nodes), 2))
            child = [None] * num_nodes
            child[start:end] = p1[start:end]
            pointer = 0
            for city in p2:
                if city not in child:
                    while child[pointer] is not None: pointer += 1
                    child[pointer] = city
            
            # Mutation (Swap)
            if random.random() < 0.1:
                idx1, idx2 = random.sample(range(num_nodes), 2)
                child[idx1], child[idx2] = child[idx2], child[idx1]
            
            new_pop.append(child)
        population = new_pop
        
    return population[0]