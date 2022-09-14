#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        value = a / b
        print("Inside result: {:.1f}".format(value))
    except:
        value = "None"
        print("Inside result: {:.1f}".format(result))
    finally:
        return value
