import numpy as np

nums = np.array([[5.54, 3.38, 7.99],
                 [3.54, 8.32, 6.99],
                 [1.54, 2.39, 9.29]])

print("Original array:")
print(nums)

n= 8.32
r = 18.32

print("/nReplace elements of the said array which are equal to", n, "with", r)
print(np.where(nums == n, r, nums))

print("/nReplace elements of the said array which are less than", n, "with", r)
print(np.where(nums < n, r, nums))

print("/nReplace elements of the said array which are greater than", n, "with", r)
print(np.where(nums > n, r, nums))
