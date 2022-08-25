#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import *
    x = (sys.argv)
    length = len(x) - 1
    if (length > 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    elif(length == 3):
        if (x[2] == '+'):
             print("{}".format(add(int(x[1]), int(x[3]))))
        elif (x[2] == '-'):
            print("{}".format(sub(int(x[1]), int(x[3]))))
        elif (x[2] == '*'):
            print("{}".format(mul(int(x[1]), int(x[3]))))
        elif (x[2] == '/'):
            print("{}".format(div(int(x[1]), int(x[3]))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
