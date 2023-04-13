#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r") as new_read:
        print(new_read.read())
