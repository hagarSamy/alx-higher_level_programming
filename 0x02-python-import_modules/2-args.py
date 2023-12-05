#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        args = "arguments."
    elif len(sys.argv) == 2:
        args = "argument:"
    else:
        args = "arguments:"
    print("{} {}".format(len(sys.argv) - 1, args))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
