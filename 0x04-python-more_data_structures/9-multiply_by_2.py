#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        hold = a_dictionary.copy()
        for k, v in sorted(hold.items()):
            value = value * 2
            tuple_hold = {k: value}
            hold.update(tuple_hold)
        return hold
