#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    b = "None" if a <= 0 else sentence[0]
    our_tuple = a, b
    return our_tuple
