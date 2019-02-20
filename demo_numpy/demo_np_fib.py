import numpy as np


def fib_lin(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


assert fib_lin(10) == 55


def fib_log(n):
    step = np.mat([[1, 1], [1, 0]], dtype=np.int64)
    step = step ** (n-1)
    return step[0, 0]


# ideally, this would be in a different file
import unittest


class FibTest(unittest.TestCase):
    def test_eq(self):
        for i in range(50):
            log = fib_log(i)
            lin = fib_lin(i)
            self.assertEqual(log, lin, f'i={i}')


unittest.main(verbosity=5)
