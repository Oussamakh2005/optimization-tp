import random
def get_value_and_weight(solution, items):
    v = sum(items[i]['v'] for i, bit in enumerate(solution) if bit == 1)
    w = sum(items[i]['w'] for i, bit in enumerate(solution) if bit == 1)
    return v, w
def genetic_algorithm(items, capacity, pop_size=50, generations=100, mutation_rate=0.05):
    n = len(items)
    
    def fitness(sol):
        v, w = get_value_and_weight(sol, items)
        return v if w <= capacity else 0

    # Initialize Population
    pop = [[random.randint(0, 1) for _ in range(n)] for _ in range(pop_size)]
    
    for _ in range(generations):
        pop = sorted(pop, key=fitness, reverse=True)
        new_pop = pop[:10] # Elitism: keep best 10
        
        while len(new_pop) < pop_size:
            # Selection
            p1, p2 = random.sample(pop[:25], 2)
            # Crossover
            split = random.randint(1, n-1)
            child = p1[:split] + p2[split:]
            # Mutation
            if random.random() < mutation_rate:
                idx = random.randint(0, n-1)
                child[idx] = 1 - child[idx]
            new_pop.append(child)
        pop = new_pop
        
    best_sol = max(pop, key=fitness)
    return fitness(best_sol), best_sol