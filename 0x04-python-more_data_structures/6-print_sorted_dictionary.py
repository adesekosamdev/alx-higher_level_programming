#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        keys = sorted(a_dictionary.keys())
        for k in keys:
            print("{}: {}".format(k), a_dictionary.get(k))
