#!/usr/bin/python3
"""
This module provies `student` class.
"""


class Student:
    """
    A student class with student assciated attributes
    and a method to return dictinary representation of student.
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns Json representation of the object.
        """
        return self.__dict__
