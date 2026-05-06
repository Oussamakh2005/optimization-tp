import numpy as np
import random
import math

def simulated_annealing(dist_matrix, temp=1000, cooling=0.995, iterations=5000):
    """Probabilistic search that allows worse moves to escape local optima."""
    current_route = list(range(len(dist_matrix)))
    random.shuffle(current_route)
    current_dist = total_distance(current_route, dist_matrix)
    best_route, best_dist = current_route, current_dist
    
    for _ in range(iterations):
        # 2-opt swap for neighbor
        i, j = sorted(random.sample(range(len(dist_matrix)), 2))
        neighbor = current_route.copy()
        neighbor[i:j] = current_route[i:j][::-1]
        neighbor_dist = total_distance(neighbor, dist_matrix)
        
        # Acceptance criteria
        if neighbor_dist < current_dist or random.random() < math.exp((current_dist - neighbor_dist) / temp):
            current_route, current_dist = neighbor, neighbor_dist
            if current_dist < best_dist:
                best_route, best_dist = current_route, current_dist
        
        temp *= cooling
    return best_route