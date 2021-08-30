"""
In each input list, every number repeats at least once, except for two. Write a function that returns the two unique numbers.

Examples
return_unique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]

return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]

return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]
Notes
Keep the same ordering in the output.
"""


def return_unique(lst):

    return [i for i in lst if lst.count(i) == 1]

    # lst = [i for i in enumerate(lst)]
    # print(lst)
    #
    # lst = [[key, value] for key, value in lst]
    # print(lst)
    #
    # print([[key, value, lst.count(value)] for key, value in lst])

    # print(value)
    # lst = [[i, lst.count(i)] for i in set(lst)]

    # return [i[0] for i in lst if i[1] == 1]


    # dic = (dict((i, lst.count(i)) for i in set(lst)))
    # return [key for key, value in dic.items() if value == 1]

print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))
print(return_unique([4, 3, 9, 9, 1, 1, 6, 1, 6, 2, 4]))
print(return_unique([44, 44, 44, 2, 55, 55, 55, 0, 66, 66, 66]))
print(return_unique([-9, -9, -9, 7, -9, -9, 1]))
print(return_unique([2, 2, -19, 2, 7, 7, 4, 9, 9, 0, 0, 3, 3, 3]))