#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            upper = chr(ord(str[i]) - 32)
        else:
            upper = str[i]
        print("{}".format(upper), end='')
    print()
