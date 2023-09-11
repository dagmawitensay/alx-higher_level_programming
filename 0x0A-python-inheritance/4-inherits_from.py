#!/usr/bin/python3
"""
This module provides a function called `inherits_from`
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is a subclass of a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
