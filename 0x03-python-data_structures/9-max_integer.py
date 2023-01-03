#!/usr/bin/python3
def max_integer(my_list=[]):
    idx = 0
    j = my_list[0]
    for i in my_list:
        idx += 1
        if i > j:
            j = i
    return (none if len(my_list) == 0 else j)
