#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        list_from_string = list(my_string)
        list_len = len(list_from_string)
        count = 0
        for i in range(0, list_len):
            if list_from_string[i] == "c" or list_from_string[i] == "C":
                list_from_string.pop(i)
                list_from_string.append(i)
                count = count + 1
        list_from_string = list_from_string[:(list_len-count)]
        new_string = ''.join(list_from_string)
        return new_string
    else:
        return ""
