#!/usr/bin/python3
"""
This module provies a function `class_to_json`
"""


def class_to_json(obj):
    """
    Converts css to JSON
    """
    return obj.__dict__
