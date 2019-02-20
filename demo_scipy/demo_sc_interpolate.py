import numpy as np
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')

x_new = np.linspace(0, 10, num=41, endpoint=True)
plt.plot(x, y, 'o', x_new, f(x_new), '-', x_new, f2(x_new), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()