import numpy as np

nums = np.array([[5.54, 3.38, 7.99, 33],
                 [3.54, 8.32, 6.99, 23],
                 [1.54, 2.39, 9.29, 22.1]])

print("Original array:")
print(nums)
print("\nNew array of equal shape and data type of the said array filled by 0:")
print(np.zeros_like(nums))