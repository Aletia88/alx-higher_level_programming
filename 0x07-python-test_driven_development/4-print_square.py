#!/usr/bin/python3
"""Print square"""

def print_square(size):
    """Print a square"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
        if type(size) is float:
            raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
             print('#', end ='')
        print()
