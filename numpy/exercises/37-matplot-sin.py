import numpy as np

import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.2)

y = np.sin(x)

print("Plot the points using matplotlob: ")

plt.plot(x, y)
plt.show()