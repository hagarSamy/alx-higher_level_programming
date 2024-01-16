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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
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

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
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

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
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

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
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

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        '''Calculates and returns the area of
        a rectangle
        '''

        return self.__width * self.__height

    def display(self):
        '''Prints hashes as rectangle'''

        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        '''beautifies the output'''

        s = f"[{Rectangle.__name__}] ({self.id})" +
        f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return s
