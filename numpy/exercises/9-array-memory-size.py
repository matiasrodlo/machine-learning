import numpy as np

x = np.array([1, 7, 13, 105])

print("Original array: ")
print(x)

print("Size of the memory occupied by the said array: ")
print("%d bytes" % (x.size * x.itemsize))