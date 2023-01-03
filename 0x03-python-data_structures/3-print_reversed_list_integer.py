#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    j = 0
    for elements in my_list:
        j += 1
    for i in range(j - 1, -1, -1):
        print("{}".format(my_list[i]))
