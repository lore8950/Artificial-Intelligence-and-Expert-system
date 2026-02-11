# y = tan(x)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 400)
y = np.tan(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("tan(x)")
plt.title("y = tan(x)")
plt.ylim(-10, 10)
plt.grid()
plt.show()
