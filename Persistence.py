"""
The additive persistence of an integer, n, is the number of times you have to replace n with the sum of its digits until n becomes a single digit integer.

The multiplicative persistence of an integer, n, is the number of times you have to replace n with the product of its digits until n becomes a single digit integer.

Create two functions that take an integer as an argument and:

Return its additive persistence.
Return its multiplicative persistence.
Examples: Additive Persistence
additive_persistence(1679583) ➞ 3
# 1 + 6 + 7 + 9 + 5 + 8 + 3 = 39
# 3 + 9 = 12
# 1 + 2 = 3
# It takes 3 iterations to reach a single-digit number.

additive_persistence(123456) ➞ 2
# 1 + 2 + 3 + 4 + 5 + 6 = 21
# 2 + 1 = 3

additive_persistence(6) ➞ 0
# Because 6 is already a single-digit integer.
Examples: Multiplicative Persistence
multiplicative_persistence(77) ➞ 4
# 7 x 7 = 49
# 4 x 9 = 36
# 3 x 6 = 18
# 1 x 8 = 8
# It takes 4 iterations to reach a single-digit number.

multiplicative_persistence(123456) ➞ 2
# 1 x 2 x 3 x 4 x 5 x 6 = 720
# 7 x 2 x 0 = 0

multiplicative_persistence(4) ➞ 0
# Because 4 is already a single-digit integer.
Notes
The input n is never negative.
"""
from functools import reduce

def additive_persistence(n) -> int:

    count = 0

    def additive_calc(n):

        nonlocal count

        if len(str(n)) == 1:
            return n
        else:
            count += 1
            n = sum([int(i) for i in str(n)])
            return additive_calc(n)

    additive_calc(n)
    return count


def multiplicative_persistence(n) -> int:

    count = 0

    def multi_calc(n):

        nonlocal count

        if len(str(n)) == 1:
            return n
        else:
            count += 1
            n = reduce(lambda x, y: x*y, [int(i) for i in list(str(n))])
            return multi_calc(n)

    multi_calc(n)
    return count

print(additive_persistence(1679583))
print(additive_persistence(123456))
print(additive_persistence(19999999999999999999999))
print(additive_persistence(5))
print(additive_persistence(27))
print(additive_persistence(58))
print(additive_persistence(5789))

print(multiplicative_persistence(77))
print(multiplicative_persistence(123456))
print(multiplicative_persistence(4))
print(multiplicative_persistence(7))
print(multiplicative_persistence(1234567890))
print(multiplicative_persistence(39))
