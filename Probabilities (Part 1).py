"""
Given a list of numbers and a value n, write a function that returns the probability of choosing a number greater than or equal to n from the list. The probability should be expressed as a percentage, rounded to one decimal place.

Examples
probability([5, 1, 8, 9], 6) ➞ 50.0
probability([7, 4, 17, 14, 12, 3], 16) ➞ 16.7
probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6) ➞ 70.0
Notes
Precent probability of event = 100 * (num of favourable outcomes) / (total num of possible outcomes)
"""
from typing import List


def probability(lst: List, n: int):

    count_high = 0
    count_low = 0
    for i in lst:
        if i >= n:
            count_high += 1
        else:
            count_low += 1

    n = len(lst)

    return round((count_high / n) * 100, 1)

print(probability([5, 1, 8, 9], 6) )
print(probability([7, 4, 17, 14, 12, 3], 16))
print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))



