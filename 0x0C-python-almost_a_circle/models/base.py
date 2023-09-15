#!/usr/bin/python3



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
