"""
Swap X and Y Coordinates
Write a function that swaps the X and Y coordinates in a string.

Examples
swap_xy("(1, 2), (3, 4)") ➞ "(2, 1), (4, 3)"

swap_xy("(11, 23), (43, 99)") ➞ "(23, 11), (99, 43)"

swap_xy("(-5, -3), (7, 4)") ➞ "(-3, -5), (4, 7)"
"""
import re

def swap_xy(str):

    result = [int(d) for d in re.findall(r'-?\d+', str)]

    v1, v2, v3, v4 = result

    res = '({}, {}), ({}, {})'.format(v2, v1, v4, v3)

    return res

    # return (v2, v1), (v4, v3)

    #
    # result[0], result[1] = result[1], result[0]
    # result[2], result[3] = result[3], result[2]
    #
    # str1 = (result[0], result[1])
    #
    # str2 = result[3], result[2]
    # return type(str1)

print(swap_xy("(1, 2), (3, 4)"))