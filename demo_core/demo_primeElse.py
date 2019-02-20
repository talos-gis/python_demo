x = 97
for i in range(2, x):
    if x % i == 0:
        print(f'{i} divides {x}')
        break
else:
    print(f'{x} is prime!')
