import numpy as np
import random
import math
from load_tsp import total_distance

def get_neighborhood(route):
    """Generates neighbors using 2-opt swaps."""
    for i in range(1, len(route) - 1):
        for j in range(i + 1, len(route)):
            new_route = route.copy()
            new_route[i:j] = route[i:j][::-1]
            yield new_route

def local_search_first_improvement(route, dist_matrix):
    """Accepts the first neighbor that is better than current."""
    best_route = route
    best_dist = total_distance(route, dist_matrix)
    improved = True
    while improved:
        improved = False
        for neighbor in get_neighborhood(best_route):
            d = total_distance(neighbor, dist_matrix)
            if d < best_dist:
                best_dist = d
                best_route = neighbor
                improved = True
                break # First improvement found
    return best_route

def local_search_best_improvement(route, dist_matrix):
    """Examines all neighbors and picks the best one."""
    best_route = route
    best_dist = total_distance(route, dist_matrix)
    improved = True
    while improved:
        improved = False
        current_best_route = best_route
        for neighbor in get_neighborhood(best_route):
            d = total_distance(neighbor, dist_matrix)
            if d < best_dist:
                best_dist = d
                current_best_route = neighbor
                improved = True
        best_route = current_best_route
    return best_route