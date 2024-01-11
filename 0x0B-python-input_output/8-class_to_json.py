#!/usr/bin/python3
'''A module to write a function that
returns the dictionary description(__dict__)
with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
'''


def class_to_json(obj):
    ''' A function that retrieves the
    dict descritption of an object
    Args: object
    Return: the dictionary description of an obh
    '''

    #vars(obj) gives same result
    return obj.__dict__
