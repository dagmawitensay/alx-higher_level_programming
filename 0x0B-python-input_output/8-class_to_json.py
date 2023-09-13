#!/usr/bin/python3
"""
This module provies a function `class_to_json`
"""
import json


def class_to_json(obj):
    """
    Converts class to json.
    """
    res = {}
    if hasattr(obj, '__dict__'):
        res = obj.__dict__.copy()

    return res
