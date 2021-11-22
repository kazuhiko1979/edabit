"""
Write a function that counts the number of times a specific digit occurs in a range (inclusive).
The function will look like:

digit_occurrences(start, end, digit) ➞ number of times digit occurs
Examples
digit_occurrences(51, 55, 5) ➞ 6
# [51, 52, 53, 54, 55] : 5 occurs 6 times

digit_occurrences(1, 8, 9) ➞ 0

digit_occurrences(-8, -1, 8) ➞ 1

digit_occurrences(71, 77, 2) ➞ 1
Notes
Ranges can be negative.
start <= end
"""
import math

def digit_occurrences(start, end, digit):

    # return str(list(range(start, end+1))).count(str(digit))

    res = ''.join([str(i) for i in range(start, end+1)])
    return res.count(str(digit))

    # count = 0
    # for num in range(start, end+1):
    #     for letter in str(num):
    #         if letter in str(digit):
    #             count += 1
    # return count




print(digit_occurrences(51, 55, 5))
print(digit_occurrences(1, 8, 9))
print(digit_occurrences(-8, -1, 8))
print(digit_occurrences(71, 77, 2))