#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except Exception:
        c = "None"
    finally:
        if (c == "None"):
            print("Inside result: {}".format(c))
        else:
            print("Inside result: {:.1f}".format(c))
        return c
