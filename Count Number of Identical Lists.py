"""
Create a function that takes four lists as arguments and
returns a count of the total number of identical lists.

Examples
count_identical_lists([0, 0, 0], [0, 1, 2], [0, 0, 0], [2, 1, 0]) ➞ 2
count_identical_lists([0, 1, 0], [0, 1, 2], [0, 2, 0], [2, 1, 0]) ➞ 0
count_identical_lists([0, 1, 2], [0, 1, 2], [0, 1, 2], [2, 1, 0]) ➞ 3
"""
from collections import Counter
import pandas as pd


def count_identical_lists(lst1, lst2, lst3, lst4):

    lst = [lst1, lst2, lst3, lst4]
    duplicated = []
    temp = []

    for x in lst:
        if x not in duplicated:
            duplicated.append(x)
        else:
            temp.append(x)

    temp = int(len(temp))

    if temp != 0:
        temp = temp + 1
    return temp

print(count_identical_lists([0, 0, 0], [0, 1, 2], [0, 0, 0], [2, 1, 0]))
print(count_identical_lists([0, 1, 0], [0, 1, 2], [0, 2, 0], [2, 1, 0]))
print(count_identical_lists([0, 1, 2], [0, 1, 2], [0, 1, 2], [2, 1, 0]))
