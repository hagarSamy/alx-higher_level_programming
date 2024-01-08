#!/usr/bin/python3
'''A module to write a class Rectangle
that inherits from BaseGeometry (7-base_geometry.py).
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A subclass that inherits from geometry
    Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
    '''
    def __init__(self, width, height):
        ''' initializes a new rectangle
        Args: width and height
        '''

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    
    def area(self):
        '''calculates area of a rectangle'''
        return self.__width * self.__height
    
    def __str__(self):
        '''Beautifies the output'''
        ToReturn = "[" + type(self).__name__ + "]" + " "
        ToReturn += str(self.__width) + "/"
        ToReturn += str(self.__height)
        return ToReturn
