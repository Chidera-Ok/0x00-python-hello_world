#!/usr/bin/python3
"""[a function that prints My name is <first name> <last name>]"""

def say_my_name(first_name, last_name=""):
    """[a function that prints my name]
    
    Arguments:
        first_name {[str]} -- [description]
    
    Keyword Arguments:
        last_name {str} -- [description] (default: {""})
    """
    if type(first_name) is not str and len(firstname) is 0:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
 
    print("My name is {} {}".format(first_name, last_name))
