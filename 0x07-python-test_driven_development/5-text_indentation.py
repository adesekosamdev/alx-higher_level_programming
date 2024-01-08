#!/usr/bin/python3
""" module that prins new lines after some characters
"""


def text_indentation(text):
    """function that prints a text with 2 new lines
       after each of these characters: ., ? and :
    Args:
        text (str): string to print
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    temp = text.replace(".", ".\n\n")
    temp2 = temp.replace("?", "?\n\n")
    temp = temp2.replace(":", ":\n\n")
    temp2 = temp.rstrip(" ")
    temp = temp2.lstrip(" ")
    temp3 = temp.split("\n")
    for i in range(len(temp3)):
        temp3[i] = temp3[i].rstrip(" ")
        temp3[i] = temp3[i].lstrip(" ")
    print('\n'.join(temp3), end='')
