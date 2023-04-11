import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist
from dataset import attractiveness, supply_locations, demand_locations

def calculate_probabilities(attractiveness, supply_locations, demand_locations):
    """
    Calculates the probability of each demand location visiting each supply location based on the modified Huff model.

    Args:
        attractiveness (list of float): The attractiveness of each supply location.
        supply_locations (numpy array): An n x 2 numpy array containing the coordinates of each supply location.
        demand_locations (numpy array): An m x 3 numpy array containing the coordinates and populations of each demand location.

    Returns:
        numpy array: An m x n numpy array containing the probability of each demand location visiting each supply location.
    """
    # Define the distance decay function (e.g., using the inverse distance squared)
    distance_decay = lambda d: 1 / (1 + d**2)

    # Calculate the distance matrix between demand and supply locations
    distances = cdist(demand_locations[:, :2], supply_locations, 'euclidean')

    # Calculate the probability of visiting each supply location for each demand location
    probabilities = np.zeros((len(demand_locations), len(supply_locations)))
    for i in range(len(demand_locations)):
        for j in range(len(supply_locations)):
            if distances[i, j] <= 2:
                attractiveness_ij = attractiveness[j]
                distance_decay_ij = distance_decay(distances[i, j])
                total_attractiveness = np.sum(attractiveness * distance_decay(distances[i]))
                probabilities[i, j] = attractiveness_ij * distance_decay_ij / total_attractiveness

    return probabilities

def allocate_demand(probabilities, supply_locations, demand_locations):
    """
    Allocates the demand of each demand location to the nearest eligible supply location based on the modified Huff model.

    Args:
        probabilities (numpy array): An m x n numpy array containing the probability of each demand location visiting each supply location.
        supply_locations (numpy array): An n x 2 numpy array containing the coordinates of each supply location.
        demand_locations (numpy array): An m x 3 numpy array containing the coordinates and populations of each demand location.

    Returns:
        numpy array: An n x 1 numpy array containing the allocated demand for each supply location.
    """
    # Create an empty array to store the allocated demand for each supply location
    allocated_demand = np.zeros(len(supply_locations))

    # Calculate the distance matrix between demand and supply locations
    distances = cdist(demand_locations[:, :2], supply_locations, 'euclidean')

    # Allocate demand to the supply locations based on the probabilities and distance constraint
    for i in range(len(demand_locations)):
        # Find the supply location with the highest probability of visitation within 2 miles
        eligible_supply_indices = np.where(distances[i] <= 2)[0]
        if len(eligible_supply_indices) > 0:
            j = np.argmax(probabilities[i, eligible_supply_indices])
            j = eligible_supply_indices[j]
            # Allocate the demand to the selected supply location
            allocated_demand[j] += demand_locations[i, 2]

    return allocated_demand

# Calculate the probabilities of visiting each supply location for each demand location
probabilities = calculate_probabilities(attractiveness, supply_locations, demand_locations)

# Allocate demand to the supply locations based on the probabilities and distance constraint
allocated_demand = allocate_demand(probabilities, supply_locations, demand_locations)

# Print the allocated demand for each supply location
print("Allocated demand:")
for i in range(len(supply_locations)):
    print(f"Supply location {i}: {allocated_demand[i]}")