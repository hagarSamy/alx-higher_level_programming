#!/usr/bin/python3
'''This module is to Write a class MyList that inherits from list'''


class MyList(list):
    '''A class that prints a list
    Args: superclass
    '''

    def print_sorted(self):
        """method takes self as arg
        Args: self
        Returns : void : print sorted list"""
        print(sorted(self))
