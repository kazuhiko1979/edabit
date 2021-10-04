"""
Create a function that gets every pair of numbers from an array that sums up to eight and returns it as an array of pairs (sorted ascendingly). See the following examples for more details.

Examples
sums_up([1, 2, 3, 4, 5]) ➞ [[3, 5]]

sums_up([1, 2, 3, 7, 9]) ➞ [[1, 7]]

sums_up([10, 9, 7, 2, 8]) ➞ []

sums_up([1, 6, 5, 4, 8, 2, 3, 7]) ➞ [[2, 6], [3, 5], [1, 7]]
// [6, 2] first to complete the cycle (to sum up to 8)
// [5, 3] follows
// [1, 7] lastly
// the pair that completes the cycle is always found on the left
// [2, 6], [3, 5], [1, 7] sorted according to cycle completeness, then pair-wise.
"""

# lst = [1, 2, 3, 4, 5]
# lst = [1, 2, 3, 7, 9]
# lst = [1, 6, 5, 4, 8, 2, 3, 7]
# lst = [10, 9, 7, 1, 8, -2, -1, 2, 6]
# lst2 = lst.copy()

# print(lst)
# print(lst2)
# for n1 in lst:
#     for n2 in lst2:
#         if n1 + n2 == 8:
#             # print("Lst_Index:", lst.index(n1) + 1, ":", n1, "Lst2_Index:", lst2.index(n2) + 1, ":", n2)
#             print("Total_Index_num", (lst.index(n1) + 1), lst2.index(n2) + 1, "num:", n1, n2)
#             # print((lst.index(n1) + 1), lst2.index(n2) + 1)


def sums_up(lst):

    res = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == 8:
                res.append([lst[i], lst[j]])

    res.sort(key=lambda x:lst.index(x[1]))
    return {"pairs": [sorted(pair) for pair in res]}


print(sums_up([1, 2, 3, 4, 5]))