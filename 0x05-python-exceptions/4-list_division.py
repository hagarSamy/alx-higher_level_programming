#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    g = []
    try:
        for i in range(list_length):
            try:
                s = (my_list_1[i] / my_list_2[i])
                g.append(s)
            except TypeError:
                g.append(0)
                print("wrong type")
            except ZeroDivisionError:
                g.append(0)
                print("division by 0")
            except IndexError:
                g.append(0)
                print("out of range")
    finally:
        return g
