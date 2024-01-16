#!/usr/bin/python3
'''A module to write the class Rectangle that inherits from Base'''


from models.base import Base


class Rectangle(Base):
    '''A subclass of Base Class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instatiation of a new subclass rectangle
        Args:
        width and height and x and y and id
        '''

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''width getter'''

        return self.__width

    @width.setter
    def width(self, width):
        '''width setter
        args: width
        '''

        self.__width = width

    @property
    def height(self):
        '''height getter'''

        return self.__height

    @height.setter
    def height(self, height):
        '''height setter
        args: height
        '''

        self.__height = height

    @property
    def x(self):
        '''x getter'''

        return self.__x

    @x.setter
    def x(self, x):
        '''x setter
        args: x
        '''

        self.__x = x

    @property
    def y(self):
        '''y getter'''

        return self.__y

    @y.setter
    def y(self, y):
        '''y setter
        args: y
        '''

        self.__y = y
