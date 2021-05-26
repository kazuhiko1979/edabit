"""
Given a list of numbers, return whether it is possible to make the number 7 by adding any three different numbers together.

Examples
lucky_seven([2, 4, 3, 8, 9, 1]) ➞ True
lucky_seven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ True
lucky_seven([0, 0, 0, 2, 3]) ➞ False
# You cannot repeat the same number to make 2 + 2 + 3 = 7

lucky_seven([4, 3]) ➞ False
# You need three different numbers.
"""
import itertools


def lucky_seven(lst):

    for i in itertools.combinations(lst, 3):
        if sum(i) == 7 and len(i) == 3:
            return True
    return False

print(lucky_seven([2, 4, 3, 8, 9, 1]))
print(lucky_seven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(lucky_seven([0, 0, 0, 2, 3]))
print(lucky_seven([4, 3]))
print(lucky_seven([-9, 7, 6, -5, 10, 3, -8, 8, -6, 0]))