"""
# 例題
# 自然数digitsが与えられるので、桁数を分解して足し合わせる、splitAndAddという関数を末尾再帰を使って作成してください。

# 19 → 10
# 23387 → 23
# 546125 → 23
"""

# def splitAndAddHelper(start, n, length_n, total):
#
#     if length_n < 1:
#         return total
#
#     return splitAndAddHelper(start+1, n, length_n-1, total + int(str(n)[start]))
#
# def splitAndAdd(n):
#
#     length_n = len(str(n))
#
#     return splitAndAddHelper(0, n, length_n, 0)

import math

def splitAndAddHelper(digit, total):

    if digit < 10:
        return digit + total

    return splitAndAddHelper(math.floor(digit / 10), total + digit % 10)


def splitAndAdd(digit):

    return splitAndAddHelper(digit, 0)


print(splitAndAdd(19))
print(splitAndAdd(3528))
print(splitAndAdd(23387))
print(splitAndAdd(5456456))


