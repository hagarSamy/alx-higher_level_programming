#!/usr/bin/python3
'''A module to write an
an Object to a text file
using a JSON representation
'''
import json


def save_to_json_file(my_obj, filename):
    '''writes an object to a text file
    Args: the object to write and
    the file to write to
    Return: void
    '''

    with open(filename, "w") as jf:
       jf.write(json.dump(my_obj))

    