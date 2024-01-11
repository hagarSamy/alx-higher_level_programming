#!/usr/bin/python3
'''A module to write a class Student'''


class Student:
    """A class Student defined by first and
    last name and age
    """

    def __init__(self, first_name, last_name, age):
        '''A function to initialize an instance(instantiation)
        Args: first and last names and age
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A public method to retrieve a
        dict representation of a St instance
        """

        DictToReturn = {}
        if isinstance(attrs, list):
            for attr in attrs:
                if type(attr) == str:
                    if hasattr(self, attr):
                        DictToReturn.update({attr: getattr(self, attr)})
        else:
            return self.__dict__
        return DictToReturn
