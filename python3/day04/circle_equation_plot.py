# Plot of x² + y² = r² (Circle)

import numpy as np
import matplotlib.pyplot as plt

# Radius
r = 5

# Angle values from 0 to 2π
theta = np.linspace(0, 2*np.pi, 400)

# Parametric equations of circle
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot the circle
plt.plot(x, y)

# Labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of x² + y² = r²")

# Make the circle perfectly round
plt.axis("equal")

# Grid
plt.grid()

# Show
plt.show()
