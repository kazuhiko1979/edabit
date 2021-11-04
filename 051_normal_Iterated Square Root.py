"""
The iterated square root of a number is the number of times the square root function must be applied to bring the number strictly under 2.

Given an integer, return its iterated square root. Return "invalid" if it is negative.

Examples
i_sqrt(1) ➞ 0

i_sqrt(2) ➞ 1

i_sqrt(7) ➞ 2

i_sqrt(27) ➞ 3

i_sqrt(256) ➞ 4

i_sqrt(-1) ➞ "invalid"
Notes
Idea for iterated square root by Richard Spence.
"""
import math

def i_sqrt(n, i = 0):

    if n < 0:
        return "invalid"
    return i if n < 2 else i_sqrt(n**(1/2), i+1)


    # if n == 1:
    #     return 0
    # elif n < 0:
    #     return "invalid"
    #
    # sqrt_num = math.sqrt(n)
    # count = 1
    # while sqrt_num >= 2:
    #     sqrt_num = math.sqrt(sqrt_num)
    #     count += 1
    # return count


print(i_sqrt(1))
print(i_sqrt(2))
print(i_sqrt(7))
print(i_sqrt(27))
print(i_sqrt(256))
print(i_sqrt(-1))
print(i_sqrt(16943))