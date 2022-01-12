"""
Almost Sorted Sequence
An almost-sorted sequence is a sequence that is strictly increasing or strictly decreasing if you remove a single element from the list (no more, no less). Write a function that returns True if a list is almost-sorted, and False otherwise.

For example, if you remove 80 from the first example, it is perfectly sorted in ascending order. Similarly, if you remove 7 from the second example, it is perfectly sorted in descending order.

Examples
almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41] ) ➞ True

almost_sorted([6, 5, 4, 7, 3]) ➞ True

almost_sorted([6, 4, 2, 0]) ➞ False
// Sequence is already sorted.

almost_sorted([7, 8, 9, 3, 10, 11, 12, 2]) ➞ False
// Requires removal of more than 1 item.
Notes
Completely sorted lists should return False.
Lists will always be > 3 in length (to remove ambiguity).
Numbers in each input list will be unique - don't worry about "ties".
"""

from copy import deepcopy

def almost_sorted(lst):

    lst = [i[1] > i[0] for i in zip(lst, lst[1:])]
    return lst.count(True) == 1 or lst.count(False) == 1



    # for i in range(len(lst)):
    #     l = deepcopy(lst)
    #     l.pop(i)
    #     if l == sorted(l) or l == sorted(l, reverse=True):
    #         return True
    # return False








    # originalListIndex = lst.index(max(lst))
    # print(originalListIndex)
    # print(sorted(lst).index(max(lst)))


    # listIncreasing = []
    # listDecreasing = []
    #
    # max = lst[0]
    # # min = lst[0]
    #
    # removeItems = 0
    #
    # listIncreasing.append(max)
    # listDecreasing.append(min)
    #
    # # return listIncreasing
    #
    #
    # for i in range(0, len(lst)):
    #
    #     if max < lst[i]:
    #         max = lst[i]
    #         listIncreasing.append(max)
    #         continue
    #     elif max > lst[i]:
    #         # listDecreasing.append(max)
    #         listIncreasing.append(max)
    #         listIncreasing.pop()
    #         removeItems += 1
    #         try:
    #             max = copy.deepcopy(lst[i])
    #             if max > lst[i]:
    #                 listIncreasing.append(max)
    #             max = lst[i]
    #         except:
    #             print("error")
    #         continue
    #
    #
    # return listIncreasing, removeItems



    # result = []
    # max = lst[0]
    # removeItems = 0
    # result.append(max)
    #
    # for i in range(1, len(lst)):
    #     if max < lst[i]:
    #         max = lst[i]
    #         result.append(max)
    #         continue
    #     elif max > lst[i]:
    #         result.pop()
    #         removeItems += 1
    #         try:
    #             max = copy.deepcopy(lst[i])
    #             result.append(max)
    #             max = lst[i]
    #         except:
    #             print("error")
    #         continue
    # return result, removeItems

print(almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41]))
print(almost_sorted([6, 5, 4, 7, 3]))
print(almost_sorted([7, 8, 9, 3, 10, 11, 12, 2]))
print(almost_sorted([6, 5, 4, 7, 3]))






















