#!/usr/bin/python3

"""
This module provides a function `is_same_class`
"""


def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True

    return False
