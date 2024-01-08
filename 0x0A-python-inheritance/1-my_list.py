#!/usr/bin/python3
'''This module is to Write a class MyList that inherits from list'''


class MyList(list):
    '''A class that prints a list
    Args: superclass
    '''

    def print_sorted(self):
        new = []
        for i in self:
            new.append(i)
        new.sort()
        print("{}".format(new))
