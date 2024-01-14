#!/usr/bin/python3
''' A module to write a function that
adds 2 integers.
and checks a test file
'''


def add_integer(a, b=98):
    '''A function that adds two integers or floats
    Args: a and b set to default: 98
    Return: sum of both integers
    '''

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, int):
        raise TypeError("b must be an integer or float")
    return (a + b)
