#!/usr/bin/python3
"""module that writes string to a text file
and returns number of characters written
"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns
        the number of characters written
    """
    with open(filename, encoding="utf-8", mode="w") as my_file:
        return my_file.write(text)
