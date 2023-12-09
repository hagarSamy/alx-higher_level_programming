#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        sum = 0
        num = 0
        for a, b in my_list:
            sum += (a * b)
            num += b
    return sum / num
