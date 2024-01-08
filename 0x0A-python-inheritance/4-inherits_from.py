#!/usr/bin/python3
'''A module that returns True if
the object is an instance of a class that
inherited (directly or indirectly) from
the specified class; otherwise False
'''


def inherits_from(obj, a_class):
    '''checks if an object belongsbto  a subclass
    Args: object and a class
    Return: true if yes anf false otherwise
    '''

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
