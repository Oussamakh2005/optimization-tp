import random

def greedy_deterministic(items, capacity):
    # Sort by density (value/weight) descending
    sorted_items = sorted(items, key=lambda x: x['v']/x['w'], reverse=True)
    knapsack = []
    total_value = 0
    current_weight = 0
    
    for item in sorted_items:
        if current_weight + item['w'] <= capacity:
            knapsack.append(item)
            current_weight += item['w']
            total_value += item['v']
    return total_value, knapsack

def greedy_nondeterministic(items, capacity, randomness=0.3):
    items_copy = sorted(items, key=lambda x: x['v']/x['w'], reverse=True)
    knapsack = []
    total_value = 0
    current_weight = 0
    
    while items_copy:
        # Pick from a small pool of top candidates instead of just the first
        pool_size = max(1, int(len(items_copy) * randomness))
        pick = random.choice(items_copy[:pool_size])
        items_copy.remove(pick)
        
        if current_weight + pick['w'] <= capacity:
            knapsack.append(pick)
            current_weight += pick['w']
            total_value += pick['v']
    return total_value, knapsack