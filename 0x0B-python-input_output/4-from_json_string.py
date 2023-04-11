#!/usr/bin/python3
"""
Module contains function that converts json string to object
"""
import json


def from_json_string(my_str):
    """
    returns object from json string
    """
    return json.loads(my_str)
