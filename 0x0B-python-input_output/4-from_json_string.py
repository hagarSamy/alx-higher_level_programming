#!/usr/bin/python3
'''A module to write a
function that returns
an object (Python data structure)
represented by a JSON string
'''
import json


def from_json_string(my_str):
    '''returns an object python
    Args: the json string to convert
    Return: the Pthon object
    '''

    NewObj = json.loads(my_str)
    return NewObj
