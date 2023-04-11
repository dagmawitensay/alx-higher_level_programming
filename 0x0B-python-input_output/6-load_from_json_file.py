#!/usr/bin/python3
"""
Module contains a function that creats object from a file
"""
import json


def load_from_json_file(filename):
    """
    Creates object form file data
    Args:
        filename: name of the file
    """
    with open(filename, 'r', encoding="UTF-8") as file:
        data = file.read()
    return json.loads(data)
