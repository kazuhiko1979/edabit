"""
A salesman has a number of cities to visit. They want to calculate the total number of possible paths they could take, visiting each city once before returning home. Return the total number of possible paths a salesman can travel, given n cities.

If we have cities A, B and C, possible paths would be:

A -> B -> C
A -> C -> B
B -> A -> C
B -> C -> A
C -> B -> A
C -> A -> B
... which gives us 6 as the possible number of paths.

Examples
paths(4) ➞ 24
paths(1) ➞ 1
paths(9) ➞ 362880
"""
from itertools import permutations
import math

def paths(n):

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

    # return math.factorial(n)

    # if n < 2:
    #     return 1
    # else:
    #     return n * paths(n-1)
    #


print(paths(4))

