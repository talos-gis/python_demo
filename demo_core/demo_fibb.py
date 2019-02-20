def fibb(n):
    if n <= 1:
        return n
    return fibb(n-1) + fibb(n-2)


# fibb is too slow
cache = {0: 0, 1: 1}
def fibb_cached(n):
    if n in cache:
        return cache[n]
    ret = fibb_cached(n-1) + fibb_cached(n-2)
    cache[n+1] = ret
    return ret
