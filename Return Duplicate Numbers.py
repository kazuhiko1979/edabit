"""
Given a list nums where each integer is between 1 and 100, return a sorted list containing only duplicate numbers from the given nums list.

Examples
duplicate_nums([1, 2, 3, 4, 3, 5, 6]) ➞ [3]
duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]) ➞ [72, 81, 99]
duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ None
Notes
The given list won't contain the same number three times.
If there are no duplicate numbers, return None.
"""
def duplicate_nums(num):

    lst = []
    result = []
    for i in num:
        if i not in lst:
            lst.append(i)
        else:
            result.append(i)

    # # 空配列を弾く
    # if len(result) == 0:
    #     # return
    # return result.sort()


# print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
# print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]))
# print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


print(duplicate_nums([1, 2, 3, 4, 3, 5, 6])) # [3]
print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # None
print(duplicate_nums([20, 30, 40, 30, 20, 40])) # [20, 30, 40]
print(duplicate_nums([100, 59, 12, 13, 54, 76, 100, 14, 12])) # [12, 100])
print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54])) # [72, 81, 99])
print(duplicate_nums([11, 22, 33, 44, 55, 44, 33, 22, 11])) # [11, 22, 33, 44])

