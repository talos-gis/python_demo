sixth = 1 / 6
print(sixth)
one = sixth + sixth + sixth + sixth + sixth + sixth

print(one == 1)

print(one)
print(abs(one - 1) < 1e-7)
from math import isclose

print(isclose(one, 1))
