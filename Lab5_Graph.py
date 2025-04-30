import json
import numpy as np
import matplotlib.pyplot as plt


with open('C:\\Users\\octo1\\OneDrive\\Documents\\CS 437\\Lab 5\\LogData.json', 'r') as f:
    data = json.load(f)
# Set up the figure
fig, ax = plt.subplots(figsize=(10,10))

# Draw x and y axis lines for the quadrants
ax.axhline(0, color='black', linewidth=1)  # Horizontal line
ax.axvline(0, color='black', linewidth=1)  # Vertical line

# For each zebra only
for animal_name, animal_data in data.items():
    if animal_name.startswith("Lion:"):  # You can remove this check if you want ALL animals
        gps_coords = np.array([[float(x), float(y)] for x, y in animal_data["gps coordinates"]])
        x = gps_coords[:,1]  # Longitude (or X)
        y = gps_coords[:,0]  # Latitude (or Y)
        ax.plot(x, y, label=animal_name)  # Plot the movement

# Set equal aspect ratio (important for distances to look right)
ax.set_aspect('equal', 'box')

# Labels and title
plt.xlabel('Longitude (or X)')
plt.ylabel('Latitude (or Y)')
plt.title('Animal Movement Paths (4-Quadrant Map)')
plt.legend()
plt.grid(True)
plt.show()