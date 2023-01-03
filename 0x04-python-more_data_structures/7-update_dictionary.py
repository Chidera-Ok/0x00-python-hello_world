#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        dics = {key: value}
        a_dictionary.update(dics)
        return(a_dictionary)
    else:
        return None
