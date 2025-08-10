import numpy as np

nums = np.arange(16, dtype='int').reshape(-1,4)

print("Original array:")
print(nums)

nums[[0, -1],:] = nums[[-1, 0],:]

print("\nNew array after swapping first and last row of the said array: ")
print(nums)