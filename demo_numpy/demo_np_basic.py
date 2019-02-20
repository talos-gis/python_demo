import numpy as np  # bread and butter right here

a = np.array([1, 2, 3])  # Create a rank 1 array
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5  # Change an element of the array
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])  # Create a rank 2 array
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0])
print(b[0])  # the first row
print(b[..., 0])  # first element of every row
print(b[:2, 1])  # second element of the first tow rows

print(b)
print(b*3)
print(b*a)
print(b@a)
