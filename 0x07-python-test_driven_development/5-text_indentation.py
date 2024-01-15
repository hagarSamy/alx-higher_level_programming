#!/usr/bin/python3
'''A module to write a function that prints
a text with 2 new lines after each of these characters: ., ?
'''


def text_indentation(text):
    '''prints 2 new lines after specefic
    characters in the text
    Args: text
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in(".?:"):
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print("{}".format(text), end="")
