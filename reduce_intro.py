import timeit
import functools


def calc_values(x, y: int):
    return x + y


numbers = [1, 2, 3, 4, 5, 6]

reduced_values = functools.reduce(calc_values, numbers)
print(reduced_values)
