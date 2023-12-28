#!/usr/bin/python3
'''A square defined by coordinate position'''


class Square:
    '''A class that gets and sets size with a property
      and position as well(coordinate)'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """A public instance method to calculate area of square"""
        return ((self.__size)**2)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or \
            len(value) != 2 or \
                not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints to stdout the square with #s"""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for q in range(self.__position[0]):
                    print(" ", end="")
                print("#" * (self.__size))
