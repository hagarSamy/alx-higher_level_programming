#!/usr/bin/python3
'''A module to write an
function that creates
an Object from a json file
'''
import json


def load_from_json_file(filename):
    '''creates an Object from a json file
    Args: the file to convert
    Return: void
    '''

    with open(filename, "r") as jf:
        return json.load(jf)

    