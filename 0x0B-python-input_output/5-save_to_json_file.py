#!/usr/bin/python3
"""
This module provides a function `save_to_json_file`.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves a given object to a file.
    Args:
        my_obj: object to be saved.
        filename: name of the file.
    """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
