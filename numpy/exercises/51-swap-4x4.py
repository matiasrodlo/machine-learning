import numpy as np

nums = np.arange(16, dtype='int').reshape(-1, 4)

print("Original array: ")
print(nums)

new_nums = nums[:, ::-1]

print("\nNew array after swapping first and last columns of the said array:")
print(new_nums) 
