#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range (len(row)):
            if i == len(row) - 1:
                x = ""
            else:
                x = " "
            print("{:d}".format(row[i]), end=x)
        print()
