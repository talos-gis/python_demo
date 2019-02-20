def grid(text: str, rows: int, cols: int)->str:
    """
    create a grid string
    :param text: the string to put in every cell of the grid
    :param rows: how many rows to put in the grid
    :param cols: how many columns to put in the grid
    :return: the formed grid
    """
    return '\n'.join(str(text)*rows for _ in range(cols))

# note that annotations aren't actually checked, they're just there for analysis
print(grid([1,2,3],3,3))
