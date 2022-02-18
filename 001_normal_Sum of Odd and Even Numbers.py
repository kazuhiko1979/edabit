"""
数値リストから、各偶数値、奇数値の合計を返すリストをつくる！

例：
sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([55, 36, 20, 3, 4, 1]) ➞ [60, 59])
# 36 + 20 + 4 = 60, 55 + 3 + 1 = 59

sum_odd_and_even([37, 11, 9, 0, 3, 1]) ➞ [0, 61])

"""

def sum_odd_and_even(lst):

    # odd, even = 0, 0
    #
    # for i in lst:
    #     if i % 2:
    #         odd += i
    #     else:
    #         even += i
    #
    # return [even, odd]
    #
    # sum_even = sum([i for i in lst if i % 2 == 0])
    # sum_odd = sum([j for j in lst if j % 2 != 0])
    # return [sum_even, sum_odd]

    return [sum(i for i in lst if i % 2 == 0), sum(i for i in lst if i % 2 != 0)]

print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
print(sum_odd_and_even([55, 36, 20, 3, 4, 1]))
print(sum_odd_and_even([37, 11, 9, 0, 3, 1]))























# def sum_odd_and_even(lst):
#
#     # odd, even = 0, 0
#     #
#     # for i in lst:
#     #     if i % 2:
#     #         odd += i
#     #     else:
#     #         even += i
#     # return [even, odd]
#
#     # sum_even = sum([i for i in lst if i % 2 == 0])
#     # sum_odd = sum([j for j in lst if j % 2 != 0])
#
#     # return [sum_even, sum_odd]
#
#     return [sum(i for i in lst if not i % 2), sum(i for i in lst if i % 2)]
#
# print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
# print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
# print(sum_odd_and_even([55, 36, 20, 3, 4, 1]))
# print(sum_odd_and_even([37, 11, 9, 0, 3, 1]))



