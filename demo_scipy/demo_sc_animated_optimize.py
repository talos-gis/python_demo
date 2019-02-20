from scipy.optimize import minimize
import numpy as np

import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

clusters = np.array([[1, 1], [-2, -5], [-5, 0]])
weights = np.array([3, 1, 3])

def foo(point):
    distances = np.linalg.norm(clusters - point, axis=1) * weights
    return distances.sum()


def callback(xk):
    point.set_offsets([xk])
    for l, o in zip(lines, clusters):
        line = np.array([o, xk])
        l.set_data(line[:, 0], line[:, 1])
    label.set_text(str(foo(xk)))
    plt.pause(pause_time)


fg, ax = plt.subplots()

ax.scatter(clusters[..., 0], clusters[..., 1], weights * 10)
point = ax.scatter([], [], 50)
lines = ax.plot([], [], '--', [], [], '--', [], [], '--', c=(1, 0, 0, 0.5))
for l, w in zip(lines, weights):
    l.set_lw(w)
label = ax.text(0, 0, '', transform=ax.transAxes)

pause_time = 0.0001

fg.show()

x0 = [0, -5]
res = minimize(foo, x0, method='nelder-mead', tol=1e-8, callback=callback)
print('x: ', res.x)
print('y: ', res.fun)
print('iterations: ', res.nit)
