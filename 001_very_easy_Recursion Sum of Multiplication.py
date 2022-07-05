"""
Recursion: Sum of Multiplication
Given a number, return the total sum of that number multiplied by every number between 1 and 10. Do not use the sum() built-in function.

Examples
multi_sum(1) ➞ 55
# 1 x 1 + 1 x 2 + 1 x 3 ...... 1 x 9 + 1 x 10 = 55

multi_sum(6) ➞ 330
# 6 x 1 + 6 x 2 + 6 x 3 ...... 6 x 9 + 6 x 10 = 330

multi_sum(10) ➞ 550

multi_sum(8) ➞ 440

multi_sum(2) ➞ 110
Notes
Use recursion to solve this challenge.
"""

def multi_sum(n, ten = 10):

    # v2
    return ten and n * ten + multi_sum(n, ten-1)


    # v1
    # while ten <= 1:
    #     return n * ten
    # else:
    #     return multi_sum(n, ten-1) + (n * ten)

print(multi_sum(1))
print(multi_sum(6))