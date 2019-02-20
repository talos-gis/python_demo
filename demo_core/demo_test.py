import unittest

from demo_core.demo_fibb import fibb, fibb_cached


class FibbTest(unittest.TestCase):
    def test_simple(self):
        for n in range(20):
            self.assertEqual(fibb(n), fibb_cached(n), msg=f'n={n}')
