"""
Seven Ate Nine
A number can eat the number to the right of it if it's smaller than itself. After eating that number, it becomes the sum of itself and that number. Your job is to create a function that returns the final list after the leftmost element has finished "eating".

Examples
[5, 3, 7] ➞ [8, 7] ➞ [15]

# 5 eats 3 to become 8
# 8 eats 7 to become 15
[5, 3, 9] ➞ [8, 9]

# 5 eats 3 to become 8
# 8 cannot eat 9, since 8 < 9
nom_nom([1, 2, 3]) ➞ [1, 2, 3]

nom_nom([2, 1, 3]) ➞ [3, 3]

nom_nom([8, 5, 9]) ➞ [22]
Notes
Test input contains only a list of numbers.
"""

def nom_nom(lst):

    # 微妙
    res = lst[0]

    for i in range(1, len(lst)):
        if res <= lst[i]:
            return [res] + lst[i:]
        res += lst[i]
    return [res]




    # ダメな例、汎用性がない・・・

    # index = 0
    # sub_index = 0
    #
    # while index < len(lst):
    #     try:
    #         if lst[index] > lst[index + 1]:
    #             subtotal = lst[index] + lst[index + 1]
    #             lst.insert(sub_index, subtotal)
    #             lst.pop(sub_index+1)
    #             lst.pop(sub_index+1)
    #         elif lst[index] <= lst[index + 1]:
    #             index += 1
    #     except:
    #         return lst
    # return lst


# print(nom_nom([1, 2, 3]))
# print(nom_nom([2, 1, 3]))
print(nom_nom([8, 5, 9]))
print(nom_nom([5, 3, 7]))
print(nom_nom([5, 3, 9]))
print(nom_nom([6, 5, 6, 100]))
print(nom_nom([6, 5, 6, 100, 5, 6, 100]))

