#!/usr/bin/python3
'''A module to Write a function that returns True
if the object is an instance of,
or if the object is an instance of
a class that inherited from, the specified class;
otherwise False
'''


def is_kind_of_class(obj, a_class):
    '''checks if an object is
    an instance of the super or the inheriited class
    Args: class and object names
    REturn: true or false
    '''

    return (isinstance(obj, a_class))
