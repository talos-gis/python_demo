import numpy as np
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x = y = np.linspace(-5, 5, 50)
# x = np.linspace(0, 10, 50)[1:]
# y = np.linspace(0, 100, 200)
x, y = np.meshgrid(x, y)

z = (np.sin(x) + y ** 3 / 50)
# z = x / (x + y)

fig = plt.figure()
ax = fig.gca(projection='3d')

surf = ax.plot_surface(x, y, z, cmap=matplotlib.cm.coolwarm)

plt.show()
