import numpy as np

np.random.seed(20)

cbrt = np.cbrt(7)

nd1 = 200

print(cbrt * np.random.randn(10, 4) + nd1)