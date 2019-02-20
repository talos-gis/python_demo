from math import sqrt


def vector_length(a, b, c):
    return sqrt(a ** 2 + b ** 2 + c ** 2)


vector = (1, 2, 3)
# doing this would be cumbersome
vector_length(vector[0], vector[1], vector[2])
print(vector_length(*vector))
