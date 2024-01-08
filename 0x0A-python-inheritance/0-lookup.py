#!/usr/bin/python3
'''A module that lists available attributes and methods of an object'''


def lookup(obj):
    '''returns all attributes and methods in an object
    Args: object
    '''

    return dir(obj)
