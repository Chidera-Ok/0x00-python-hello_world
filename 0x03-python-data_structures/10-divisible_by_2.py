#!/bin/usr/python3

def divisible_by_2(my_list=[]):
    list_copy = my_list.copy()

    idx = 0
    for i in my_list:
        list_copy[idx] = True if i % 2 == 0 else False
        idx += 1
    return (list_copy)
