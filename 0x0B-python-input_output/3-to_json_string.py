#!/usr/bin/python3
"""
Module contains a function that returns the json repretaion of object
"""


import json


def to_json_string(my_obj):
    """
    Returns the json representation of the object
    """
    return json.dumps(my_obj)
