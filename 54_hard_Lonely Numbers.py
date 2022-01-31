"""
Lonely Numbers
Given a number, insert duplicate digits on both sides of all digits which appear in a group of 1.

Worked Example
numbers_need_friends_too(22733) ➞ 2277733

# The number can be split into groups 22, 7, and 33.
# 7 appears on its own.
# Put 7s on both sides to create 777.
# Put the numbers together and return the result.
Examples
numbers_need_friends_too(123) ➞ 111222333

numbers_need_friends_too(56657) ➞ 55566555777

numbers_need_friends_too(33) ➞ 33
Notes
All tests will include positive integers.
"""
from itertools import groupby


def numbers_need_friends_too(num):

    # result = ''
    #
    # for key, group in groupby(str(num)):
    #     length = len(list(group))
    #     result += 3 * key if length is 1 else length * key
    #
    # return result

    result = ''

    for lst in [list(group) for key, group in groupby(str(num))]:
        if len(lst) == 1:
            result += lst[0] * 3
        else:
            result += ''.join(lst)

    return int(result)

    # res = []
    #
    # try:
    #     for i in range(0, len(str(num))):
    #         if str(num)[i-1] != str(num)[i] != str(num)[i+1]:
    #             n = str(num)[i] * 3
    #             res.append(n)
    #         else:
    #             res.append(str(num)[i])
    # except:
    #     pass
    #
    # if str(num)[-1] != str(num)[-2]:
    #     n = str(num)[-1] * 3
    #     res.append(n)
    #
    # return int(''.join(res))

print(numbers_need_friends_too(123))
print(numbers_need_friends_too(56657))
print(numbers_need_friends_too(33))
print(numbers_need_friends_too(22733))
print(numbers_need_friends_too(11223333))



