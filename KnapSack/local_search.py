import random
def get_value_and_weight(solution, items):
    v = sum(items[i]['v'] for i, bit in enumerate(solution) if bit == 1)
    w = sum(items[i]['w'] for i, bit in enumerate(solution) if bit == 1)
    return v, w

def local_search(items, capacity, strategy='first'):
    n = len(items)
    # Start with an empty knapsack valid solution
    current_sol = [0] * n
    current_val, _ = get_value_and_weight(current_sol, items)
    
    while True:
        improved = False
        best_neighbor = None
        best_neighbor_val = current_val
        
        # Explore neighbors (1-bit flips)
        indices = list(range(n))
        random.shuffle(indices) # Shuffle for first-improvement randomness
        
        for i in indices:
            neighbor = list(current_sol)
            neighbor[i] = 1 - neighbor[i]
            val, weight = get_value_and_weight(neighbor, items)
            
            if weight <= capacity and val > best_neighbor_val:
                if strategy == 'first':
                    current_sol, current_val = neighbor, val
                    improved = True
                    break
                else: # Best improvement
                    best_neighbor = neighbor
                    best_neighbor_val = val
                    improved = True
        
        if strategy == 'best' and improved:
            current_sol, current_val = best_neighbor, best_neighbor_val
        elif not improved:
            break
            
    return current_val, current_sol