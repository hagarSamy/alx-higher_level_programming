#!/usr/bin/python3
''' A module to write a
function that writes a
string to a text file (UTF8) and
returns the number of characters written
'''


def write_file(filename="", text=""):
    '''overwrites a string to a file
    Args: the file and the text
    Return: number of chars written
    '''

    with open(filename, "w", encoding="utf-8") as f:
        charsWritten = f.write(text)
    return charsWritten
