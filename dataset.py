import numpy as np 

# Define the attractiveness of each supply location (e.g., based on product quality, pricing, etc.)
attractiveness = [10, 8, 6, 4, 2]

# Define the locations of the supply locations (e.g., the coordinates of each store)
supply_locations = np.array([
    [37.7749, -122.4194],  # San Francisco, CA
    [40.7128, -74.0060],   # New York, NY
    [34.0522, -118.2437],  # Los Angeles, CA
    [41.8781, -87.6298],   # Chicago, IL
    [51.5074, -0.1278],    # London, UK
])

# Define the demand locations (e.g., the coordinates of each zone) and their populations
demand_locations = np.array([
    [37.7749, -122.4194, 1000],  # San Francisco, CA (1000 people)
    [37.7749, -122.4094, 500],   # San Francisco, CA (500 people)
    [37.7849, -122.4194, 800],   # San Francisco, CA (800 people)
    [40.7128, -74.0060, 1200],   # New York, NY (1200 people)
    [40.7228, -74.0060, 700],    # New York, NY (700 people)
    [34.0522, -118.2437, 900],   # Los Angeles, CA (900 people)
    [34.0422, -118.2437, 600],   # Los Angeles, CA (600 people)
    [41.8781, -87.6298, 1100],   # Chicago, IL (1100 people)
    [41.8881, -87.6298, 400],    # Chicago, IL (400 people)
    [51.5074, -0.1278, 1000],    # London, UK (1000 people)
    [51.5174, -0.1278, 500],     # London, UK (500 people)
    [51.5074, -0.1178, 700],     # London, UK (700 people)
])