import numpy as np
import random
import math
def load_tsp(file_content):
    nodes = []
    start_reading = False
    for line in file_content.strip().split('\n'):
        if "NODE_COORD_SECTION" in line:
            start_reading = True
            continue
        if "EOF" in line or not line.strip():
            break
        if start_reading:
            parts = line.split()
            nodes.append((float(parts[1]), float(parts[2])))
    return np.array(nodes)

def calculate_dist_matrix(nodes):
    """Calculates the Euclidean distance matrix."""
    num_nodes = len(nodes)
    dist_matrix = np.zeros((num_nodes, num_nodes))
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            dist = np.linalg.norm(nodes[i] - nodes[j])
            dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix

def total_distance(route, dist_matrix):
    """Calculates the total length of a tour."""
    dist = sum(dist_matrix[route[i], route[i+1]] for i in range(len(route)-1))
    dist += dist_matrix[route[-1], route[0]] # Return to start
    return dist