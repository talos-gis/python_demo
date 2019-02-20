import matplotlib
import numpy as np

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

x = np.linspace(1, 100, 100)
fg, ax = plt.subplots()
y = 1 - ((50-1)/50) ** (x*(x+1)/2)
ax.plot(x, y)

ax.grid(axis='y')
plt.show()
