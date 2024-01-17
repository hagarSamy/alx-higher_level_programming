#!/usr/bin/python3
'''A square class that inherits from rectangle'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''A subclass of the supersubclass Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Instatiation of a square class'''

        super().__init__(size, size, x=0, y=0, id=None)
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = size

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
    def size(self):
        '''size getter'''

        return self.__size

    @size.setter
    def size(self, size):
        '''size setter
        args: size
        '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = size

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
        a square
        '''

        return self.__size ** 2

    def display(self):
        '''Prints hashes as square'''

        for j in range(self.__y):
            print()
        for i in range(self.__size):
            for k in range(self.__x):
                print(" ", end="")
            print("#" * self.__size)
    def __str__(self):
        '''beautifies the output'''

        s = (
            f"[{Square.__name__}] ({self.id}) "
            f"{self.__x}/{self.__y} - {self.__size}"
        )
        return s

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''

        if args and len(args):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
