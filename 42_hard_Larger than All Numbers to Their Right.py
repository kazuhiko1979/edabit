"""
Larger than All Numbers to Their Right
Create a function that retrieves every number that is strictly larger than every number that follows it.

Examples
larger_than_right([3, 13, 11, 2, 1, 9, 5]) ➞ [13, 11, 9, 5]
# 13 is larger than all numbers to its right, etc.

larger_than_right([5, 5, 5, 5, 5, 5]) ➞ [5]
# Must be strictly larger.
# Always include the last number.

larger_than_right([5, 9, 8, 7]) ➞ [9, 8, 7]
Notes
The last number in an array is trivially strictly larger than all numbers that follow it (no numbers follow it).
"""

def larger_than_right(lst):

    # temp = []
    # for i in range(0, len(lst)-1):
    #     if max(lst[i+1::]) < lst[i]:
    #         temp.append(lst[i])
    # temp.append(lst[-1])
    # return temp


    # return [i for idx, i in enumerate(lst) if all(i > j for j in lst[idx+1:])]


    return [base for i, base in enumerate(lst) if all(base>lst for lst in lst[i+1:])]



    # if len(set(lst)) == 1:
    #     return list(set(lst))
    # if lst == sorted(lst):
    #     return [lst[-1]]
    # if lst[0] == sorted(lst)[-1]:
    #     return lst
    #
    # # print(lst[0])
    # # print(reversed(lst))
    # # print(sorted(lst))
    #
    # top = lst[0]
    # res = []
    #
    # for i in lst:
    #     if i > lst[0]:
    #         res.append(i)
    # return res



print(larger_than_right([3, 13, 11, 2, 1, 9, 5]))
print(larger_than_right([5, 5, 5, 5, 5, 5]))
print(larger_than_right([5, 9, 8, 7]))
print(larger_than_right([9, 8, 7, 6]))
print(larger_than_right([1, 2, 3, 4]))

