#!/usr/bin/python3
import json
"""
This module provides a functin `to_json_string`
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of a given object.
    """
    return json.dumps(my_obj)
