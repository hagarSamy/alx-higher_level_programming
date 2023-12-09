#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    elif not isinstance(roman_string, str):
        return "not a string"
    romNums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0
    for j in range(len(roman_string) - 1):
        if romNums[roman_string[j]] >= romNums[roman_string[j+1]]:
            res += romNums[roman_string[j]]
        else:
            res -= romNums[roman_string[j]]
    res += romNums[roman_string[-1]]
    return res
