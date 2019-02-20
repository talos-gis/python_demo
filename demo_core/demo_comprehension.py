from itertools import count, islice
from math import sqrt, ceil


def is_perfect(x):
    return sum(i for i in range(1, x) if x % i == 0) == x


def is_prime(x):
    return x == 2 or (x % 2 != 0 and
                      all(x % i != 0 for i in range(3, ceil(sqrt(x))+1, 2)))


# list comprehension
divisors_of_30 = [30//x for x in range(1,31) if 30 % x == 0]
print(divisors_of_30)
# generator comprehension
perfect_nums = (x for x in count(1) if is_perfect(x))
print(perfect_nums)
print(list(islice(perfect_nums, 3)))
# dictionary comprehension
squares_and_roots = {square: int(sqrt(square)) for square in range(50) if sqrt(square) % 1 == 0}
print(squares_and_roots)
# set comprehension
primes = {x for x in range(2, 20) if is_prime(x)}
print(primes)
