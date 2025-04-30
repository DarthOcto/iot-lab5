import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load data
with open('C:\\Users\\octo1\\OneDrive\\Documents\\CS 437\\Lab 5\\LogData.json', 'r') as f:
    data = json.load(f)

# Set up 3D plot
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')

# For each zebra only
for animal_name, animal_data in data.items():
    if animal_name.startswith("Zebra:"):
        timestamps = list(map(float, animal_data["timestamp"]))
        gps_coords = np.array([[float(x), float(y)] for x, y in animal_data["gps coordinates"]])
        
        x = gps_coords[:,1]  # Longitude
        y = gps_coords[:,0]  # Latitude
        z = timestamps       # Time
        
        ax.plot(x, y, z, label=animal_name)

# Labels and title
ax.set_xlabel('Longitude (or X)')
ax.set_ylabel('Latitude (or Y)')
ax.set_zlabel('Time')
ax.set_title('Zebra Movement Over Space and Time (3D)')
ax.legend()
plt.show()
