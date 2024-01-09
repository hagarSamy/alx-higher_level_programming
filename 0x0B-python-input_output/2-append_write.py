#!/usr/bin/python3
''' A module to write a
function that appends a
string at the end of a text file (UTF8) and
returns the number of characters added
'''


def append_write(filename="", text=""):
    '''appendss a string to end of a file
    Args: the file and the text
    Return: number of chars written
    '''

    with open(filename, "a", encoding="utf-8") as f:
        charsWritten = f.write(text)
    return charsWritten
