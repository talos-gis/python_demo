from random import choice


def grid(char, rows, cols):
    ret = ''
    for _ in range(cols):
        for _ in range(rows):
            ret += char
        ret += '\n'
    return ret


def is_between(text, minimum, maximum):
    return minimum <= len(text) < maximum  # equivalent to minimum <= len(text) and len(text) < maximum


# both grid and is_between take the same arguments
funcToUse = is_between
print(funcToUse('|+|', 3, 5))

funcToUse = grid
print(funcToUse('|+|', 3, 5))
