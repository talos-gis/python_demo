import numpy as np
from math import sqrt, isclose, pi


class Circle:
    def __init__(self, radius=None):
        self.radius = radius

    def __str__(self):
        return f'Circle with radius {self.radius}'

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @classmethod
    def from_points(cls, *points):
        point0, point1, point2 = (np.array(p) for p in points)
        a = np.linalg.norm(point0 - point1)
        b = np.linalg.norm(point1 - point2)
        c = np.linalg.norm(point2 - point0)
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))

        diameter = a * b * c / (2 * area)
        ret = cls()
        ret.diameter = diameter
        return ret

    @property
    def area(self):
        return pi * self.radius ** 2


c = Circle.from_points((-3, 4), (4, 5), (1, -4))
assert isclose(c.radius, 5)
