from functools import lru_cache


@lru_cache(maxsize=None)
def fibb(n):
    if n <= 1:
        return n
    return fibb(n - 1) + fibb(n - 2)
