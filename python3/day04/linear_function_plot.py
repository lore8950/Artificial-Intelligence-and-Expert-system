# Plot of y = x

import numpy as np
import matplotlib.pyplot as plt

# Generate x values from -10 to 10
x = np.linspace(-10, 10, 400)

# Linear function
y = x

# Plot the graph
plt.plot(x, y)

# Labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of y = x")

# Grid
plt.grid()

# Show the graph
plt.show()
