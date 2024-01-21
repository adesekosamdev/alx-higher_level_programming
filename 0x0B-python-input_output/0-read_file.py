#!/usr/bin/python3
""" module that prints stdout from a file
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
