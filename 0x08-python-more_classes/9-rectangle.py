#!/usr/bin/python3
'''A module to define a rectangle'''


class Rectangle:
    '''A class to deine a rectangle'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        resToReturn = ""
        if (self.__width != 0 and self.__height != 0):
            for i in range(self.__height):
                resToReturn += str(self.print_symbol) * self.__width
                if i < self.__height - 1:
                    resToReturn += "\n"
        return resToReturn

    def __repr__(self):
        """returns the object representation of the instance
        to be used by eval"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        ''' Saying goodbye to leaving rects'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares rect_1, rect_2 two rectangles based on their area
        Args: rect_1 and rect_2 the two rects
        Returns : bigger area rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        return rect_2
    @classmethod
    def square(cls, size=0):
        '''turns a rectangle into a square
        Args: size: height of the square
        Returns : a class triangle of a square
        '''
        return cls(size, size)
