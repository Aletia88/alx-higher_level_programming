#!/usr/bin/python3
"""importing json"""
import json
"""define  function that returns an object"""


def from_json_string(my_str):
    """from json string to object"""
    return json.loads(my_str)
