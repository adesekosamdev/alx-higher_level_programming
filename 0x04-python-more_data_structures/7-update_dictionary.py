#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    tuple_hold = {key: value}
    a_dictionary.update(tuple_hold)
    return a_dictionary
