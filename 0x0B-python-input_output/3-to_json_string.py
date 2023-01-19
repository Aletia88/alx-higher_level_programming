#!/usr/bin/python3
"""importing json"""
import json
"""define a function that returns the JSON representation of an object"""


def to_json_string(my_obj):
    """"load string"""
    return json.dumps(my_obj)
