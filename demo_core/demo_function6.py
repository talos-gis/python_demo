def grid(char, rows, cols=None):
    if cols is None:
        cols = rows
    ret = ''
    for _ in range(cols):
        for _ in range(rows):
            ret += char
        ret += '\n'
    return ret


def sum_of_digits(number, base=10):
    ret = 0
    while number > 0:
        ret += number % base
        number //= base
    return ret
