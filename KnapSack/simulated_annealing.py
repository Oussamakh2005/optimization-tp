import math
import random
def get_value_and_weight(solution, items):
    v = sum(items[i]['v'] for i, bit in enumerate(solution) if bit == 1)
    w = sum(items[i]['w'] for i, bit in enumerate(solution) if bit == 1)
    return v, w
def simulated_annealing(items, capacity, temp=1000, cooling_rate=0.99, iterations=1000):
    n = len(items)
    current_sol = [0] * n
    curr_v, curr_w = get_value_and_weight(current_sol, items)
    
    best_sol = list(current_sol)
    best_v = curr_v
    
    for _ in range(iterations):
        # Pick random neighbor
        i = random.randint(0, n - 1)
        neighbor = list(current_sol)
        neighbor[i] = 1 - neighbor[i]
        
        next_v, next_w = get_value_and_weight(neighbor, items)
        
        if next_w <= capacity:
            # Acceptance probability
            delta = next_v - curr_v
            if delta > 0 or random.random() < math.exp(delta / temp):
                current_sol, curr_v = neighbor, next_v
                if curr_v > best_v:
                    best_sol, best_v = list(current_sol), curr_v
        
        temp *= cooling_rate
    return best_v, best_sol