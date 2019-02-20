import numpy as np

arr = np.array([1, 5, -8, 3, 1, 25])
print(arr)
print(arr > 2)
print(arr[[2, 3, 5]])
print(arr[[True, True, False, True, False, True]])
print(arr[arr > 2])
