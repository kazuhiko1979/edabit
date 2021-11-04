"""
Given a list and a set, return a sorted list with its items in ascending order but prioritize the elements in the set over the other items in the list.

Examples
priority_sort([5, 4, 3, 2, 1], {2, 3}) ➞ [2, 3, 1, 4, 5]

priority_sort([5, 4, 3, 2, 1], {3, 6}) ➞ [3, 1, 2, 4, 5]

priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}) ➞ [-4, -3, -5, -2, -1, 0]
Notes
If the list is empty, return an empty list.
If the set is empty there is nothing to prioritize, but the list should still be sorted.
The set may contain values that are not in the list.
The list may contain duplicates.
The list and the set will only contain integer values.
"""

def priority_sort(lst, s):

    return sorted(lst, key= lambda x: (x not in s, x))


    # res = [i for i in sorted(lst) if i in s]
    # diff_list = sorted(list(set(lst) ^ set(res)))
    # return res + diff_list if set(sorted(diff_list)) ^ set(sorted(lst)) else sorted(lst)


    # lst = sorted(lst)
    # res = []

    # if i in s:
    #     res.append(i)

    # diff_list = sorted(diff_list)

    # if set(sorted(diff_list)) ^ set(sorted(lst)):
    #     return res + diff_list
    # else:
    #     return sorted(lst)

    #     return res + diff_list
    # else:
    #     return sorted(lst)


print(priority_sort([5, 4, 3, 2, 1], {2, 3}))
print(priority_sort([], {2, 3}))
print(priority_sort([], {}))
print(priority_sort([1, 2, 3], {}))
print(priority_sort([5, 4, 3, 2, 1], {3, 6}))
print(priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}))
print(priority_sort([-10, 0, 10], {0}))
print(priority_sort([4, 2, 2], {1}))
print(priority_sort([1, 5, 5, 5, 5, 2, 1], {1, 5}))





