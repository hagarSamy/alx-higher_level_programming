#!/usr/bin/python3
'''A module to write a
function that reads a
text file (UTF8) and prints it to stdout
'''


def read_file(filename=""):
    """reads files
    Args:
        filename
    """

    with open(filename, encoding="utf-8") as myFile:
        print((myFile.read()), end="")
