#!/usr/bin/python3
"""A module that inherits the list"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints a sorted list in ascending order"""
        print(sorted(self))
