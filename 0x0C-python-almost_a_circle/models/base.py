#!/usr/bin/python3
''''A module to initiate a class'''


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        '''instatiation'''

        if id:
            self.id = id
        Base.__nb_objects += 1
