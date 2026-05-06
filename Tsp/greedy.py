import numpy as np
import random
import math
def greedy_deterministic(dist_matrix, start_node=0):
    """Always picks the nearest unvisited neighbor."""
    num_nodes = len(dist_matrix)
    unvisited = list(range(num_nodes))
    unvisited.remove(start_node)
    route = [start_node]
    
    while unvisited:
        current = route[-1]
        next_node = min(unvisited, key=lambda x: dist_matrix[current, x])
        unvisited.remove(next_node)
        route.append(next_node)
    return route

def greedy_nondeterministic(dist_matrix, k=3):
    """Randomly picks from the 'k' nearest unvisited neighbors."""
    num_nodes = len(dist_matrix)
    unvisited = list(range(num_nodes))
    start_node = random.choice(unvisited)
    unvisited.remove(start_node)
    route = [start_node]
    
    while unvisited:
        current = route[-1]
        # Sort unvisited by distance and pick from top k
        candidates = sorted(unvisited, key=lambda x: dist_matrix[current, x])[:k]
        next_node = random.choice(candidates)
        unvisited.remove(next_node)
        route.append(next_node)
    return route