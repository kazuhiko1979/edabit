"""
Create a function that takes a string containing integers as well as other characters and return the sum of the negative integers only.

Examples
negative_sum("-12 13%14&-11") ➞ -23
# -12 + -11 = -23

negative_sum("22 13%14&-11-22 13 12") ➞ -33
# -11 + -22 = -33
"""
import re


def negative_sum(char):

    regex = re.compile(r'[\-]?[0-9]+')

    nums = [int(k) for k in regex.findall(char)]
    return sum([num for num in nums if num < 0])

print(negative_sum("-12 13%14&-11"))
print(negative_sum("22 13%14&-11-22 13 12"))

