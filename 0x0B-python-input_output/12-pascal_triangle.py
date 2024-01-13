#!/usr/bin/python3
'''Create a function
that returns a list of lists
of integers representing the Pascals
triangle of n
'''


def pascal_triangle(n):
    """A func to return Pascal's triangle"""

    ls = []
    if n <= 0:
        return ls
    ls = [[1]]
    for row in range(1, n):
        newRow = [1]
        for k in range(1, row):
            newRow.append(ls[row - 1][k - 1] + ls[row - 1][k])
        newRow.append(1)
        ls.append(newRow)
    return ls
