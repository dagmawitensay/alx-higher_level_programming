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

    def to_json_string(list_dictionaries):
        """
        Returns the JSON sring reprsentation of list_dictionaries.
        """
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
