"""
Converting One Binary String to Another
Write a function that returns the minimum number of swaps to convert the first binary string into the second.

Examples
min_swaps("1100", "1001") ➞ 1

min_swaps("110011", "010111") ➞ 1

min_swaps("10011001", "01100110") ➞ 4
Notes
Both binary strings will be of equal length.
Both binary strings will have an equal number of zeroes and ones.
A swap is switching two elements in a string (swaps do not have to be adjacent).
"""

def min_swaps(s1, s2):


    # v1
    # if len(s1) > 0:
    #     if s1[0] != s2[0]:
    #         return min_swaps(s1[1:], s2[1:]) + 1 / 2
    #     else:
    #         return min_swaps(s1[1:], s2[1:])
    # return 0

print(min_swaps("1100", "1001"))
print(min_swaps("110011", "010111"))
print(min_swaps("10011001", "01100110"))