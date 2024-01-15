#!/usr/bin/python3
'''A module to Write a function that
divides all elements of a matrix
'''


def matrix_divided(matrix, div):
    '''divides all elements of a matrix
    Args: the matrix: a list of lists
    of ints or floats
    and a number (int or float) other than 0
    Return: a matrix of nums with 2 decimal places
    '''

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix == []:
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/float")
    for row in matrix:
        if row == []:
            raise TypeError("matrix must be a matrix \
                            (list of lists) of integers/float")
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix \
                            (list of lists) of integers/float")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    return [[round((element / div), 2) for element in row] for row in matrix]
