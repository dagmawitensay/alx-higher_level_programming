#!/usr/bin/python3
"""
This module provide a function `from_json_strin`.
"""
import json


def from_json_string(my_str):
    """
    Returns the string representation of a
    given JSON obect.
    Args:
        my_str: a JSON object
    """
    return json.loads(my_str)
