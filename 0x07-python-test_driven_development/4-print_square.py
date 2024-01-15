#!/usr/bin/python3
'''A module to write a function that
prints a square of hashes
'''


def print_square(size):
    '''prints a square of hashes
    Args: length of the square
    '''

    if isinstance(size, float):
        size = int(size)
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
