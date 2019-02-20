import numpy as np

a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a)
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))
print(a.sum(axis=2))
print(a.sum(axis=(0, 1)))
