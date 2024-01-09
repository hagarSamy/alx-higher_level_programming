#!/usr/bin/python3
'''A module to write a function that reads a text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
    with open(filename, encoding='UTF8') as myFile:
        return myFile.read()
