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
        '''writes the JSON string representation of list_objs to a file
        Args: list_objs:  a list of instances who inherits of Base(rect/squ)
        '''

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

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set
        Args: dictionary: kword args
        '''

        '''creating a dummy instance with arbitrary values'''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''

        filename = cls.__name__ + ".json"
        if not filename:
            return []
        with open(filename, "r") as f:
            '''getting data as 1 string'''
            dataOfStrings = f.read()
        ''''''
        listofdictionaries = [cls.from_json_string(dataOfStrings)]
        listofinstances = [cls.create(**dictionary)
                           for dictionary in listofdictionaries]
        return listofinstances
