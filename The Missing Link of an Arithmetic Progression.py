"""
Your function will get a list with a number sequence. However, one item will be missing. It's your job to find out which one is not in the list.

To illustrate, given the list [1, 3, 4, 5], 2 is missing so the output must be 2.

Examples
missing([1, 3, 4, 5]) ➞ 2
missing([2, 4, 6, 8, 10, 14, 16]) ➞ 12
missing([1.5, 2, 3]) ➞ 2.5
Notes
The missing item will never be the smallest or largest number in the list.
In every list, exactly one item is missing.
"""
from numpy import arange


def missing(lst):

    diff_head = float(lst[1] - lst[0])
    diff_bottom = float(lst[-1] - lst[-2])

    mis_list = []

    if diff_head == diff_bottom:
        step = diff_head
        for x in range(lst[0], lst[-1]+1, int(step)):
            if x not in lst:
                mis_list.append(x)
    else:
        step = abs(diff_head - diff_bottom)
        for x in arange(lst[0], lst[-1] + 1, step):
            if x not in lst:
                mis_list.append(x)

    for num in mis_list:
        return num


print(missing([1, 3, 4, 5]))
print(missing([2, 4, 6, 8, 10, 14, 16]))
print(missing([1.5, 2, 3]))




