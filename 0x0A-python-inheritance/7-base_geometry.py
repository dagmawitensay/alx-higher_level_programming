#!/usr/bin/python3
"""
This module provides a calss called `BaseGeometry`
"""


class BaseGeometry:
    """
    A base geometry class
    Public_Methods:
        area(self): raise an exception:
        integer_validator(self, name, value): vaidates value
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
