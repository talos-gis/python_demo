from itertools import islice, count, takewhile


def primes():
    prev_primes = []
    for n in count(start=2):
        potential_factors = takewhile(lambda x: x*x <= n, prev_primes)
        if not any(n % p == 0 for p in potential_factors):
            yield n
            prev_primes.append(n)


prime_generator = primes()
# don't do this:
# list(primes())
print(prime_generator)
first_10_primes = islice(prime_generator, 10)
print(list(first_10_primes))
