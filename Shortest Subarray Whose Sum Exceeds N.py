"""
Write a function that returns the length of the shortest contiguous sublist whose sum of all elements strictly exceeds n.

Examples
min_length([5, 8, 2, -1, 3, 4], 9) ➞ 2

min_length([3, -1, 4, -2, -7, 2], 4) ➞ 3
# Shortest sublist whose sum exceeds 4 is: [3, -1, 4]

min_length([1, 0, 0, 0, 1], 1) ➞ 5

min_length([0, 1, 1, 0], 2) ➞ -1
Notes
The sublist should be composed of contiguous elements from the original list.
If no such sublist exists, return -1.
"""


def min_length(lst, n):

    sublist = []
    max_sublist = []
    re_sublist = []

    if max(lst) > n:
        return 1

    max_index = lst.index(max(lst))
    tmp_sublist = (lst[:max_index+1])[::-1]

    for x in lst[::-1]:
        re_sublist.append(x)
        if sum(re_sublist) > n:
            break

    for j in tmp_sublist:
        max_sublist.append(j)
        if sum(max_sublist) > n:
            break

    for i in lst:
        sublist.append(i)
        if sum(sublist) > n:
            break

    if sum(max_sublist) > n:
        if sum(sublist) > n:
            return min(len(max_sublist), len(sublist))
        return -1

    if sum(re_sublist) > n:
        if sum(sublist) > n:
            return min(len(re_sublist), len(sublist))
        return min(len(re_sublist), len(sublist))
    return -1

    if sum(re_sublist) > n:
        if sum(max_sublist) > n:
            return min(len(re_sublist), len(max_sublist))
        return -1

    if sum(sublist) > n:
        if sum(re_sublist) > n:
            return min(len(re_sublist), len(sublist))


