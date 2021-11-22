"""
Write three functions:

boolean_and
boolean_or
boolean_xor
These functions should evaluate a list of True and False values, starting from the leftmost element and evaluating pairwise.

Examples
boolean_and([True, True, False, True]) ➞ False
# [True, True, False, True] => [True, False, True] => [False, True] => False

boolean_or([True, True, False, False]) ➞ True
# [True, True, False, True] => [True, False, False] => [True, False] => True

boolean_xor([True, True, False, False]) ➞ False
# [True, True, False, False] => [False, False, False] => [False, False] => False
Notes
XOR is the same as OR, except that it excludes [True, True].
Each time you evaluate an element at 0 and at 1, you collapse it into the single result.
"""
from functools import reduce


def boolean_and(lst):

    return reduce(lambda a, b : a & b, lst)

    # if False in lst:
    #     return False
    # return True

def boolean_or(lst):

    return reduce(lambda a, b : a | b, lst)

    # if True in lst:
    #     return True
    # return False

def boolean_xor(lst):

    return reduce(lambda a, b : a ^ b, lst)

    # if lst.count(True) % 2 == 0:
    #     return False
    # return True

print(boolean_and([True, True, False, True]))
print(boolean_xor([True, True, False, True]))
