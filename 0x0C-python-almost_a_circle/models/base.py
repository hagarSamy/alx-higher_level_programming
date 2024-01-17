#!/usr/bin/python3
''''A module to initiate a class'''

import json


class Base:
    '''A class to set self id'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''instatiation
        Args: the id: None is default value'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns the JSON string representation
        of list_dictionaries
        '''

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''

        filename = cls.__name__ + ".json"
        if list_objs is None or list_objs == []:
            listDicts = []
        else:
            listDicts = []
            for obj in list_objs:
                listDicts.append(obj.to_dictionary())
                '''same as
                listDicts = [obj.to_dictionary() for obj in list_objs]
                '''

        with open(filename, "w") as jf:
            jf.write(cls.to_json_string(listDicts))
