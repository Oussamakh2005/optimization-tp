import random

def generate_knapsack_data(size=None, min_val=1, max_val=10):
    """
    Generates synthetic data for the Knapsack problem.
    
    - size: The number of items to generate. If None, returns a dict of standard sizes.
    - min_val: Minimum value/weight for an item.
    - max_val: Maximum value/weight for an item.
    - return: A dict {'items': [...], 'capacity': int} or a dict of dicts if size is None.
    """
    
    def create_set(n):
        items = [{'v': random.randint(min_val, max_val), 
                  'w': random.randint(min_val, max_val)} for _ in range(n)]
        # Capacity is 50% of total potential weight
        capacity = int(sum(item['w'] for item in items) * 0.5)
        return {'items': items, 'capacity': capacity}

    # If user specifies a single size (e.g., 50)
    if size is not None:
        return create_set(size)
    
    # Default behavior: generate the full suite of test sizes
    standard_sizes = [50, 100, 200, 500, 1000]
    return {s: create_set(s) for s in standard_sizes}

# Usage Examples 
# Generate just one specific size
data_200 = generate_knapsack_data(size=10)
print(data_200['items'])
print(f"Items generated: {len(data_200['items'])}")
print(f"Capacity: {data_200['capacity']}")
