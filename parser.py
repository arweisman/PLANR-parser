import numpy as np
import matplotlib.pyplot as plt
import math

filename = "ultra_simple_test_output"
linesToSkip = 6

theta = []
dist = []
q_val = 0

# Open file and read line by line
with open(filename, "r") as f:
    for line in f:
        # Skip the first few lines of status data
        if (linesToSkip >= 0):
            linesToSkip -= 1
            continue

        # Begin parsing formatted data
        line = line.strip(' S\n')   # characters to trim
        data = line.split(" ")      # split on spaces

        q_val = int(data[5])        # Q... seems to be zero if out of range?

        # Only record values with valid(?) q_val
        if (q_val != 0):
            theta.append(math.radians(float(data[1])))
            dist.append(float(data[3]))

# Create plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(theta, dist)

ax.set_title("Sample Scan", va='bottom')
plt.show()
