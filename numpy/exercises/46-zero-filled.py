import numpy as np

nums = np.zeros(shape=(5, 6), dtype='int')

print("Original array: ")
print(nums)

nums[::2, ::2] = 3

nums[1::2, ::2] = 7

print("\nNew array: ")
print(nums)