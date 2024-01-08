#!/usr/bin/python3
''' A module to write an arbitrary class'''


class BaseGeometry:
    ''' A class that raises an error'''

    def area(self):
        raise Exception("area() is not implemented")
