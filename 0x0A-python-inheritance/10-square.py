#!/usr/bin/python3
'''a class Square that
inherits from Rectangle (9-rectangle.py).
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass that inherits from rectangle
    Args:
            size (int): The size of the new Square.
    '''
    def __init__(self, size):
        ''' initializes a new square
        Args: size
        '''

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''calculates area of a rectangle'''
        return self.__size ** 2
