#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        l = len(my_list)
        if l == 0:
            return None
        else:
            max = 0
            for i in range(0, l):
                if my_list[i] > max:
                    max = my_list[i]
            return max