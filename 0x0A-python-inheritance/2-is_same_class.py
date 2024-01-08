#!/usr/bin/python3

'''A module to returns True if the object is exactly an instance of the specified class
otherwise False
'''


def is_same_class(obj, a_class):
    '''checks if an object is an instance of a class
    Args: an object and a class

    Return: True if true and False otherwise
    '''

    return (type(obj) is a_class)
