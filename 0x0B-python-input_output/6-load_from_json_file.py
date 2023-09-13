#!/usr/bin/python3
"""
This module provides a function `load_from_json_file`.
"""
import json


def load_from_json_file(filename):
    """
    creates object from JSON file.
    Args:
        filename: name of the file.
    """
    with open(filename) as file:
        data = file.read()

    return json.loads(data)
