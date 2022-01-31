"""
Lucky Seven
Given a list of numbers, return whether it is possible to make the number 7 by adding any three different numbers together.

Examples
lucky_seven([2, 4, 3, 8, 9, 1]) ➞ True

lucky_seven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ True

lucky_seven([0, 0, 0, 2, 3]) ➞ False
# You cannot repeat the same number to make 2 + 2 + 3 = 7

lucky_seven([0, 0, 7]) ➞ False
# You need three different numbers.
Notes
Tests will only include numbers.
Trivially, any list with a length of less than two automatically fails the test.
"""

from itertools import combinations

def lucky_seven(lst):

    total = 0

    for i in lst:
        for j in lst:
            for z in lst:
                total = i + j + z
                if total == 7 and i != j and j != z and i != z:
                    return total
    return False


    # if not lst:
    #     return False
    # return 7 in [sum(list(i)) for i in combinations(lst, 3) if len(list(i)) == len(set(list(i)))]

print(lucky_seven([2, 4, 3, 8, 9, 1]))
print(lucky_seven([7, 7]))
print(lucky_seven([0, 0, 7]))
print(lucky_seven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(lucky_seven([0, 0, 0, 2, 3]))
print(lucky_seven([1]))
print(lucky_seven([2, 3]))
print(lucky_seven([]))
#