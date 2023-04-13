#!/usr/bin/python3
"""A funciton to read file"""

def read_file(filename=""):
    """open and read file"""
    with open(filename, "r", encoding="utf-8") as new_read:
        print(new_read.read())
