#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        return [replace if element is search else element for element in my_list]
