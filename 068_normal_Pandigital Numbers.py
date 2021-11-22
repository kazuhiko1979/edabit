"""
Pandigital Numbers
A pandigital number contains all digits (0-9) at least once. Write a function that takes an integer, returning True if the integer is pandigital, and False otherwise.

Examples
is_pandigital(98140723568910) ➞ True

is_pandigital(90864523148909) ➞ False
# 7 is missing.

is_pandigital(112233445566778899) ➞ False
Notes
Think about the properties of a pandigital number when all duplicates are removed.
"""

def is_pandigital(n):

    return len(sorted(set(str(n)))) == 10

print(is_pandigital(123456789876543210))
print(is_pandigital(90864523148909))
print(is_pandigital(112233445566778899))




