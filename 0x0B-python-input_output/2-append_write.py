#!/usr/bin/python3
"""A function that appends to a file"""


def append_write(filename="", text=""):
    """Append string to a UTF8 text file"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
