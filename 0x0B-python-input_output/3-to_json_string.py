#!/usr/bin/python3
'''A module to write a
function that returns the
JSON representation of an
object (string)
'''
import json


def to_json_string(my_obj):
    '''returns the json representation of an obj
    Args: the object to convert
    Return: the object's json representation
    '''

    NewObj = json.dumps(my_obj, sort_keys=True)
    return NewObj
