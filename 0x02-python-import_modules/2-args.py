#!/usr/bin/python3
import sys 
for length in range(1, len( sys.argv)):
    print("{}: {}".format(length, sys.argv[length]))
