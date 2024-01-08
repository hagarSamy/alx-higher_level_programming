#!/usr/bin/python3
''' A module to write an arbitrary class'''


class BaseGeometry:
    ''' A class that raises an error'''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''A method that validates value'''

        self.name = name
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(self.name))
        else:
            raise TypeError("{} must be an integer".format(self.name))
