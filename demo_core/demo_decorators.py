from functools import singledispatch


@singledispatch
def to_grid(x):
    raise TypeError


@to_grid.register(str)
def _(x):
    return x+'\n'+'\n'.join(x[1:])


@to_grid.register(int)
def _(x):
    return to_grid('+'*x)


@to_grid.register(float)
def _(x):
    return to_grid(str(x))


for i in ['cat', 4, 12.5]:
    print()
    print(f'to_grid({i}):')
    print(to_grid(i))
