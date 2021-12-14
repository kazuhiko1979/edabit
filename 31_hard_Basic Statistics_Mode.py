"""
Basic Statistics: Mode
The mode of a group of numbers is the value (or values) that occur most often (values have to occur more than once). Given a sorted list of numbers, return a list of all modes in ascending order.

Examples
mode([4, 5, 6, 6, 6, 7, 7, 9, 10]) ➞ [6]

mode([4, 5, 5, 6, 7, 8, 8, 9, 9]) ➞ [5, 8, 9]

mode([1, 2, 2, 3, 6, 6, 7, 9]) ➞ [2, 6]
Notes
In this challenge, all group of numbers will have at least one mode.
"""
from collections import Counter

def mode(lst):

    # m = max(lst.count(i) for i in lst)
    # return [i for i in sorted(set(lst)) if lst.count(i) == m]


# mode = lambda l: sorted({n for n in l if l.count(n) == max(map(l.count, l))})

    c = Counter(lst)
    return [x for x, y in sorted(c.items()) if y == max(c.values())]


    # res = {}
    #
    # for i in lst:
    #     if i not in res:
    #         res[i] = 1
    #     else:
    #         res[i] += 1
    #
    # return sorted([kv[0] for kv in res.items() if kv[1] == max(res.values())])


print(mode([4, 5, 6, 6, 6, 7, 7, 9, 10]))
print(mode([4, 5, 5, 6, 7, 8, 8, 9, 9]))
