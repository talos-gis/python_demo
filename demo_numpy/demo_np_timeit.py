from time import time
import random

import numpy as np


def time_me(sample_size, total=False, compare_to=None):
    def ret(func):
        duration = 0
        for _ in range(sample_size):
            start = time()
            func()
            duration += time() - start
        avr = duration / sample_size
        print(func.__name__ + ': ', avr, 'seconds')
        if total:
            print('\t', total, duration, 'seconds')
        if compare_to:
            faster_by = compare_to.time / avr
            print(f'\t{func.__name__} is {faster_by:.1f} times faster than {compare_to.__name__}')

        func.time = avr
        return func

    return ret


# generate a million random numbers
@time_me(10)
def loop_random():
    ret = []
    for _ in range(1_000_000):
        ret.append(random.uniform(0, 1))
    return ret


@time_me(10)
def std_random():
    return [random.uniform(0, 1) for _ in range(1_000_000)]


@time_me(1000, compare_to=std_random)
def np_random():
    return np.random.uniform(size=1_000_000)


seed = np.random.randint(0, 1000, size=1_000_000)


# sum ten million numbers
@time_me(10)
def loop_sum():
    ret = 0
    for i in seed:
        ret += i
    return ret


@time_me(10)
def std_sum():
    return sum(seed)


@time_me(1_000, compare_to=std_sum)
def np_sum():
    return np.sum(seed)
