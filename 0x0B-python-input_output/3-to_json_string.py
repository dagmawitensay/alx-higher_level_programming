#!/usr/bin/python3
"""
This module provides a functin `to_json_string`
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a given object.
    Args:
        my_obj: object to be converted.
    """
    return json.dumps(my_obj)
