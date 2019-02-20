def grid(text, rows, cols):
    """
    create a grid string
    :param text: the string to put in every cell of the grid
    :param rows: how many rows to put in the grid
    :param cols: how many columns to put in the grid
    :return: the formed grid
    docstrings can also have examples (you can even test these examples, but you can figure that out on your own)
    >>> print(grid('*',3,4))
    ***
    ***
    ***
    ***
    """
    return '\n'.join(str(text) * rows for _ in range(cols))


help(grid)
