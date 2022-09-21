#!/usr/bin/python3
"""Defines a loked class."""
class LokedClass:
    """
    Prevent the user from instantiating new Lockedclass attributes for anything but attributes called 'first_name'.
    """
    __slots__ = ["first_name"]
