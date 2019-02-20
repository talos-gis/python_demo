def foo(x):
    if x == 0:
        return 0
    return foo(x//10) + x % 10


for i in [0, 1, 21, 85, 112]:
    print(f'foo({i}) = {foo(i)}')
