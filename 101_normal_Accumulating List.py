"""
Accumulating List
Create a function that takes in a list and returns a list of the accumulating sum.

Examples
accumulating_list([1, 2, 3, 4]) ➞ [1, 3, 6, 10]
# [1, 3, 6, 10] can be written as  [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]

accumulating_list([1, 5, 7]) ➞ [1, 6, 13]

accumulating_list([1, 0, 1, 0, 1]) ➞ [1, 1, 2, 2, 3]

accumulating_list([]) ➞ []
Notes
An empty list input [] should return an empty list [].
"""
from itertools import accumulate

def accumulating_list(lst):

    # return [sum(lst[:i+1]) for i in range(len(lst))]

    return list(accumulate(lst))




    # res = []
    #
    # index = 0
    # while index < len(lst)+1:
    #     res.append(sum(lst[0:index]))
    #     index += 1
    # res.pop(0)
    #
    # return res

print(accumulating_list([1, 2, 3, 4]))
print(accumulating_list([1, 5, 7]))
print(accumulating_list([1, 0, 1, 0, 1]))
print(accumulating_list([]))