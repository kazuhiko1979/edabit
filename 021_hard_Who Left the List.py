"""
You are given two lists. The elements in lst1 threw a party and started to mix around. However, one of the element got lost! Your task is to return the element which was lost.

Examples
missing([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8]) ➞ 2

missing([True, True, False, False, True], [False, True, False, True]) ➞ True

missing(["Jane", "is", "pretty", "ugly"], ["Jane", "is", "pretty"]) ➞ "ugly"

missing(["different", "types", "5", 5, [5], (5,)], ["5", "different", [5], "types", 5]) ➞ (5,)
Notes
Assume that the first list always contains 1 or more elements.
Elements are always lost.
An element can also have duplicates.
"""
from collections import Counter

def missing(lst1, lst2):

    return [e for e in lst1 if lst1.count(e) > lst2.count(e)][0]

    # for el in lst1:
    #     if el not in lst2:
    #         return el
    #     lst2.remove(el)


    # for x in lst2:
    #     lst1.remove(x)
    # return lst1[0]
    #


    # dic1 = {str(x):lst1.count(x) for x in lst1}
    #
    # for j in lst2:
    #     if str(j) in dic1:
    #         dic1[str(j)] += 1
    #     else:
    #         dic1[str(j)] = 1
    #
    # for key, value in dic1.items():
    #     if value == 1:
    #         for x in lst1:
    #             if key == str(x):
    #                 return x
    #
    # if len(dic1) == 2:
    #     key = [k for k, v in dic1.items() if v == max(dic1.values())]
    #     if key[0]:
    #         return True


    # dic1 = {}
    #
    # for i in lst1:
    #     if str(i) in dic1:
    #         dic1[str(i)] += 1
    #     else:
    #         dic1[str(i)] = 1
    #

    # for j in lst2:
    #     if str(j) in dic1:
    #         dic1[str(j)] += 1
    #     else:
    #         dic1[str(j)] = 1
    #

    # for key, value in dic1.items():
    #     if value == 1:
    #         for x in lst1:
    #             if key == str(x):
    #                 return x
    #
    # if len(dic1) == 2:
    #     key = [k for k, v in dic1.items() if v == max(dic1.values())]
    #     if key[0]:
    #         return True


print(missing([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8]))
print(missing([True, True, False, False, True], [False, True, False, True]))
print(missing(["Jane", "is", "pretty", "ugly"], ["Jane", "is", "pretty"]))
print(missing(["different", "types", "5", 5, [5], (5,)], ["5", "different", [5], "types", 5]))
print(missing(list('fate'),list('fat')))