"""
Create a function that counts the number of blocks of two or more adjacent 1s in a list.

Examples
count_ones([1, 0, 0, 1, 1, 0, 1, 1, 1]) ➞ 2
# Two instances: [1, 1] (middle) and [1, 1, 1] (end)

count_ones([1, 0, 1, 0, 1, 0, 1, 0]) ➞ 0

count_ones([1, 1, 1, 1, 0, 0, 0, 0]) ➞ 1

count_ones([0, 0, 0]) ➞ 0
Notes
A single 1 by itself (surrounded by a zero on its left and right), does not count towards the total (see first example).
Each input will contain only zeroes and ones.
"""


def count_ones(lst):

    ones = ''.join(str(i) for i in lst).split('0')

    return sum(len(i) > 1 for i in ones)


print(count_ones([1, 0, 0, 1, 1, 0, 1, 1, 1]))
print(count_ones([1, 1, 1, 1, 0, 0, 0, 0]))



