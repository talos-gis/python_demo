import itertools as it

point_inside_rectangle = lambda x, y: abs(x) <= 1 and abs(y) <= 1
for x, y in it.product([-0.5, 0, 1, 1.1], repeat=2):
    is_not_inside = ''
    if not point_inside_rectangle(x, y):
        is_not_inside = 'not '
    print(f'({x}, {y}) is {is_not_inside}inside the rectangle')
