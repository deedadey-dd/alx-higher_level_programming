#!/usr/bin/python3
"""A funciton that returns description from dictionary"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
