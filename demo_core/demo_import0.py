import math  # module import

print(math.sin(math.pi/3))

from functools import partial  # specific import
gcd_with_120 = partial(math.gcd, 120)
for e in [0, 1, 24, 81, 120]:
    print(f'gcd(120,{e}) = {gcd_with_120(e)}')

import itertools as it  # alias module import
product = it.product([1, 2, 3], ['a', 'b', 'c'])
for p in product:
    print(p)
