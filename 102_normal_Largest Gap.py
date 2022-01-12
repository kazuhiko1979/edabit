"""
Largest Gap
Given a list of integers, return the largest gap between elements of the sorted version of that list.

Here's an illustrative example. Consider the list:

[9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]
... which, after sorting, becomes the list:

[0, 0, 4, 5, 5, 6, 9, 20, 25, 26, 26]
... so that we now see that the largest gap in the list is the gap of 11 between 9 and 20.

Examples
largest_gap([9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]) ➞ 11
# After sorting get [0, 0, 4, 5, 5, 6, 9, 20, 25, 26, 26]
# Largest gap of 11 between 9 and 20

largest_gap([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]) ➞ 4
# After sorting get [1, 3, 4, 5, 7, 7, 7, 7, 11, 12, 12, 13, 14]
# Largest gap of 4 between 7 and 11

largest_gap([13, 3, 8, 5, 5, 2, 13, 6, 14, 2, 11, 4, 10, 8, 1, 9]) ➞ 2
# After sorting get [1, 2, 2, 3, 4, 5, 5, 6, 8, 8, 9, 10, 11, 13, 13, 14]
# Largest gap of 2 between 6 and 8
"""

def largest_gap(lst):

    # return max(y-x for x, y in zip(sorted(lst), sorted(lst)[1:]))

    lst.sort()
    return max(b-a for a,b in zip(lst, lst[1:]))


    # index = 0
    # lst = sorted(lst)
    # res = []
    #
    # while index < len(lst):
    #     try:
    #         res.append(lst[index+1] - lst[index])
    #         index += 1
    #     except:
    #         return max(res)


print(largest_gap([9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]))
print(largest_gap([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]))





