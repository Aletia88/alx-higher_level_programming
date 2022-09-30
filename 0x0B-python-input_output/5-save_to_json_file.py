#!/usr/bin/python3
"""import json file"""
import json
"""define a function that writes an Object to a text file"""


def save_to_json_file(my_obj, filename):
    """json representaion of a function that writes an objec to a text file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
