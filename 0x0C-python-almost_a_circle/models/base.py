#!/usr/bin/python3
"""
This module defines a base class for models.
"""
import json



class Base:
    """
    A base class for the package.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """Instantiation of the class"""
        if not id:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON sring reprsentation of list_dictionaries.
        Args:
            list_dictionaries: list of dictionaries
        """
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file.
        Args:
            list_objs: list of objects
        """
        name = cls.__name__ + ".json"
        with open(name, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                dictionary = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(dictionary))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        Args:
            json_string: a string representing a list of dictionaries.
        """
        if json_string is None:
            return []

        return json.loads(json_string)
