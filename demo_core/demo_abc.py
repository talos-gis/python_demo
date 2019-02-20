from typing import Tuple

from abc import ABC, abstractmethod
import numpy as np


class Shape(ABC):
    @abstractmethod
    def __contains__(self, point):
        pass

    @abstractmethod
    def bounds(self) -> Tuple[float, float, float, float]:
        pass

    def area(self, sample_size=100_000):
        minx, maxx, miny, maxy = self.bounds()
        x = np.random.uniform(minx, maxx, size=(sample_size, 1))
        y = np.random.uniform(miny, maxy, size=(sample_size, 1))
        points = np.concatenate((x, y), axis=1)
        rect_area = (maxx - minx) * (maxy - miny)
        points_inside = sum(1 for x in points if x in self)
        return rect_area * (points_inside / sample_size)


class Circle(Shape):
    def __init__(self, radius, center=(0, 0)):
        self.center = center
        self.radius = np.array(radius)

    def bounds(self):
        return self.center[0] - self.radius, self.center[0] + self.radius, \
               self.center[1] - self.radius, self.center[1] + self.radius

    def __contains__(self, item):
        return np.linalg.norm(self.center - item) <= self.radius


print(Circle(1, (5, 2)).area())  # pi


class Rectangle(Shape):
    def __init__(self, *bounds):
        self._bounds = np.array(bounds)
        assert self._bounds[0] < self._bounds[1]
        assert self._bounds[2] < self._bounds[3]

    def bounds(self):
        return self._bounds

    def __contains__(self, point):
        x, y = point
        return self._bounds[0] <= x < self._bounds[1] \
            and self._bounds[2] <= y < self._bounds[3]


rect = Rectangle(1, 3, 2, 5)
print(rect.area())  # 6


class Polygon(Shape):
    def __init__(self, x, y=None):
        if y is None:
            x = np.array(x)
            y = x[..., 1]
            x = x[..., 0]
        else:
            x, y = np.array([x, y])
        assert len(x) == len(y)
        self.x = x
        self.y = y

    def bounds(self):
        return self.x.min(), self.x.max(), self.y.min(), self.y.max()

    def __contains__(self, point):
        x, y = point
        ret = False
        for x0, x1, y0, y1 in zip(self.x, np.roll(self.x, 1), self.y, np.roll(self.y, 1)):
            slope = (y1 - y0) / (x1 - x0)
            intersect_y = y0 + (x - x0) * slope
            if intersect_y < y:
                continue
            if y0 > y1:
                y0, y1 = y1, y0
            assert y0 <= y1
            if y0 <= intersect_y < y1:
                ret = not ret
        return ret

    def area(self, sample_size=None):
        total = 0
        for x0, x1, y0, y1 in zip(self.x, np.roll(self.x, 1), self.y, np.roll(self.y, 1)):
            total = x0 * y1 - x1 * y0
        return abs(total / 2)


triangle = Polygon([(0, 0), (5, 0), (2, 3)])
print(triangle.area())  # 7.5


class Union(Shape):
    def __init__(self, *parts):
        self.parts = parts

    def __contains__(self, item):
        return any(item in part for part in self.parts)

    def bounds(self):
        min_x_parts, max_x_parts, min_y_parts, max_y_parts = zip(*(p.bounds() for p in self.parts))
        return min(min_x_parts), max(max_x_parts), min(min_y_parts), max(max_y_parts)


union = Union(rect, Rectangle(2, 6, 2, 4))
print(union.area())  # 12
