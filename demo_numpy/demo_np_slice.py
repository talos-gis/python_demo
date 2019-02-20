import numpy as np


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
slice = arr[-2:, :2]  # last two rows, first two columns
print(slice)
slice[0] += 1
print(slice)
print(arr)
