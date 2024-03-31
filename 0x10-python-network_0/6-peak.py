#!/usr/bin/python3
''' A module defining a function that find the peak in a list'''


def find_peak(list_of_integers):
    '''A function to find the peak'''
    if not list_of_integers:
        return "None"
    max = list_of_integers[0]
    for i in range(len(list_of_integers)):
        temp = list_of_integers[i]
        if max < temp:
            max = temp
    return max
