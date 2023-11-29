#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a new line."""
    for s in str:
        if s >= 'a' and s <= 'z':
            s = chr(ord(s) - 32)
        print("{}".format(i), end="")
    print()
