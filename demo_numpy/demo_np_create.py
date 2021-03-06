import numpy as np

a = np.zeros((2, 2))  # Create an array of all zeros
print(a)

b = np.ones((1, 2))  # Create an array of all ones
print(b)

c = np.full((2, 2), 7)  # Create a constant array
print(c)

d = np.eye(2)  # Create a 2x2 identity matrix
print(d)

e = np.random.random((2, 2))  # Create an array filled with random values
print(e)
