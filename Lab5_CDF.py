import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import json
from scipy.spatial.distance import euclidean

# Load the data
with open('C:\\Users\\octo1\\OneDrive\\Documents\\CS 437\\Lab 5\\LogData.json', 'r') as f:
    data = json.load(f)

# Function to calculate speeds for a zebra
def calculate_speeds(zebra_data):
    timestamps = list(map(float, zebra_data["timestamp"]))
    gps_coords = np.array([[float(x), float(y)] for x, y in zebra_data["gps coordinates"]])
    distances = [euclidean(gps_coords[i], gps_coords[i+1]) for i in range(len(gps_coords)-1)]
    time_differences = np.diff(timestamps)
    speeds = np.array(distances) / np.array(time_differences)
    return speeds[speeds > 0]

# Set up the plot
plt.figure(figsize=(10,7))

# For each zebra only
for zebra_name, zebra_data in data.items():
    if zebra_name.startswith("Zebra:"):
        speeds = calculate_speeds(zebra_data)
        sns.kdeplot(speeds, cumulative=True, bw_adjust=0.5, label=zebra_name)

# Customize the plot
plt.title('CDF of Zebra Movement Speed')
plt.xlabel('Speed (distance units per time unit)')
plt.ylabel('CDF')
plt.legend(title="Zebra")
plt.grid(True)
plt.show()