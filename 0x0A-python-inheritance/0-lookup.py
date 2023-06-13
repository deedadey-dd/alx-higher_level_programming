#!/usr/bin/python3

"""
    A module that returns the list of available attributes
    and methods of an object
"""

def lookup(obj):
    """this fuctions returns a list of available attributes of an object"""
    
    return dir(obj)
