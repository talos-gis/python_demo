import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 10]
y = [-1, 1, 8, 5, 3, 10, 11, -4]

plt.grid(axis='y')
plt.plot(x, y)
plt.show()
