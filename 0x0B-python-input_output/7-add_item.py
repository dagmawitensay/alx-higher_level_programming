#!/usr/bin/python3
"""
This moudle provides functions.
"""
import sys
import json
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:0])
save_to_json_file(my_list, filename)
