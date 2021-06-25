"""
Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.

Examples
advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]

advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]

advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]
Notes
The sublists should be returned in the order of each element's first appearance in the given list.
"""
import collections

def advanced_sort(lst):

    # dic, lst1 = {}, []
    # for i in lst:
    #     dic.setdefault(i, 0)
    #     dic[i] += 1
    # for key, value in dic.items():
    #     if key in lst:
    #         lst1.append([key] * value)
    # return sorted(lst1, key=lambda x: lst.index(x[0]))

    c = collections.Counter(lst)
    lst1 = [[i]*j for i, j in c.items()]
    return sorted(lst1, key=lambda x: lst.index(x[0]))


print(advanced_sort([1, 2, 1, 2]))
print(advanced_sort([2, 1, 2, 1]))
print(advanced_sort([5, 4, 5, 5, 4, 3]))
print(advanced_sort(["b", "a", "b", "a", "c"]))


