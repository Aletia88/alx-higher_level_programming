#!/usr/bin/python3
import sys
arg = len(sys.argv) - 1
if (len(sys.argv) == 1):
    print("0 arguments.")
elif(len(sys.argv) == 2):
    print("1 argument: ")
else:
    print ("{} arguments:".format(arg))
for length in range(1, len( sys.argv)):
    print("{}: {}".format(length, sys.argv[length]))
