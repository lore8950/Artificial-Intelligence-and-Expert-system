# Plot of y = cos(x)

import numpy as np
import matplotlib.pyplot as plt

# Generate x values from -2π to 2π
x = np.linspace(-2*np.pi, 2*np.pi, 400)

# Compute cos(x)
y = np.cos(x)

# Plot the graph
plt.plot(x, y)

# Labels and title
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.title("Graph of y = cos(x)")

# Grid for better visualization
plt.grid()

# Display the graph
plt.show()
