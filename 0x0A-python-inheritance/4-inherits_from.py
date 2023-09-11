#!/usr/bin/python3
"""
This module provides a function called `inherits_from`
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is a subclass of a_class
    """
    return issubclass(obj, a_class)
