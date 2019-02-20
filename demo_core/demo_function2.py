import itertools as it


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    for i in it.count(3, step=2):
        if i**2 > n:
            break
        if n % i == 0:
            return False
    return True


for n in range(2, 20):
    if is_prime(n):
        print(f'{n} is prime')
    else:
        print(f'{n} is not prime')
