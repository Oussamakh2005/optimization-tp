import time
from greedy import greedy_deterministic
from greedy import greedy_nondeterministic
from local_search import local_search
from simulated_annealing import simulated_annealing
from genetic import genetic_algorithm
from generate_data import generate_knapsack_data

def test_all_algorithms(size=10):
    # 1. Generate the data
    data = generate_knapsack_data(size=size)
    items = data['items']
    capacity = data['capacity']
    
    print(f"--- Knapsack Test (Size: {size}, Capacity: {capacity}) ---")
    print(f"Items: {items}\n")
    
    # Define the algorithms to test
    # Format: (Name, Function, Extra Arguments)
    algorithms = [
        ("Greedy (Deterministic)", greedy_deterministic, []),
        ("Greedy (Nondeterministic)", greedy_nondeterministic, [0.4]),
        ("Local Search (First-Imp)", local_search, ['first']),
        ("Local Search (Best-Imp)", local_search, ['best']),
        ("Simulated Annealing", simulated_annealing, [1000, 0.95, 500]),
        ("Genetic Algorithm", genetic_algorithm, [20, 50, 0.1]) # Smaller pop/gen for size 10
    ]
    
    results = []
    
    for name, func, args in algorithms:
        start_time = time.time()
        # Call the function with items, capacity, and its specific args
        value, solution = func(items, capacity, *args)
        end_time = time.time()
        
        duration = end_time - start_time
        results.append({
            "name": name,
            "value": value,
            "time": duration
        })

    # 2. Display Results
    print(f"{'Algorithm':<25} | {'Max Value':<10} | {'Time (s)':<10}")
    print("-" * 50)
    for res in results:
        print(f"{res['name']:<25} | {res['value']:<10} | {res['time']:.6f}")

# Execute the test
test_all_algorithms(10)