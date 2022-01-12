"""
リストを取得し、奇数回出現する整数を見つける関数を作成します。

Examples
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1
find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5
find_odd([10]) ➞ 10

備考：
奇数回出現する整数は常に1つだけです。
"""

def find_odd(lst):

    return [i for i in lst if lst.count(i) % 2][0]


    # for i in lst:
    #     if lst.count(i) % 2 == 1:
    #         return i


    # temp = {}
    #
    # for i in lst:
    #     if i in temp:
    #         temp[i] += 1
    #     else:
    #         temp[i] = 1
    #
    # # print(temp)
    #
    # for key, value in temp.items():
    #     if value % 2 != 0:
    #         return key

print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
print(find_odd([10]))





"""
Create a function that takes a list and finds the integer which appears an odd number of times.

Examples
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1
find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5
find_odd([10]) ➞ 10
Notes
There will always only be one integer that appears an odd number of times.
"""


















# def find_odd(lst):
#
#
#     temp = {}
#
#     for i in lst:
#         if i in temp:
#             temp[i] += 1
#         else:
#             temp[i] = 1
#
#     print(temp)
#
#     for k, v in temp.items():
#         if v % 2 != 0:
#             return k
#
#
#     for i in lst:
#         if lst.count(i) % 2 == 1:
#             return i
#
#
#
#     return [i for i in lst if lst.count(i) % 2][0]
#
#
#
# print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
# print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
# print(find_odd([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]))
# print(find_odd([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))