from scipy.optimize import minimize
import numpy as np

clusters = np.array([[1, 1], [1, -5], [-5, 0]])


def foo(point):
    distances = np.linalg.norm(clusters - point, axis=1)
    return distances.sum()


assert foo([0, 0]) == (np.sqrt(2) + np.sqrt(26) + 5)  # should be abs < 0.001, but this works so who cares

x0 = [0, 0]
res = minimize(foo, x0, method='nelder-mead', tol=1e-8)
print('x: ', res.x)
print('y: ', res.fun)
print('iterations: ', res.nit)
