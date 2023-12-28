#!/usr/bin/python3
'''A square defined by size'''


class Square:
    '''A class that defines defines a square by size with defaukt val.'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size
