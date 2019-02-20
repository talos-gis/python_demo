from typing import Iterable, Tuple
from numbers import Number

import itertools as it


def offset(x_offset: Number, y_offset: Number, input: Iterable[Tuple[Number, Number]]):
    def mutate(x, y):
        return x+x_offset, y+y_offset

    for (x, y) in input:
        yield mutate(x, y)


seed = [-5, 3, 10]

mutated = offset(-2, 5, it.product(seed,repeat=2))

print(list(mutated))
