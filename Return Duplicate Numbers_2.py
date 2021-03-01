"""
Given a list nums where each integer is between 1 and 100, return a sorted list containing only duplicate numbers from the given nums list.

Examples
duplicate_nums([1, 2, 3, 4, 3, 5, 6]) ➞ [3]
duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]) ➞ [72, 81, 99]
duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ None
"""

def duplicate_nums(nums):

    result = list(set([i for i in nums if nums.count(i) > 1]))

    # 空配列を弾く
    if len(result)>0:
        "Noneを返す"
        return sorted(result)
    return None


    # result = []
    # dupl = []
    # for i in nums:
    #     if i not in result:
    #         result.append(i)
    #     else:
    #         dupl.append(i)

    # 空配列を弾く
    # if len(result) == 0:
    #     "Noneを返す"
    #     return
    # return result

print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]))
print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))