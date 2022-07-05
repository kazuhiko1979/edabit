"""
Combinatorial Exploration
Given a known number of unique items, how many ways could we arrange them in a row?

Create a function that takes an integer n and returns the number of digits of the number of possible permutations for n unique items. For instance, 5 unique items could be arranged in 120 unique ways. 120 has 3 digits, hence the integer 3 is returned.

Examples
no_perms_digits(0) ➞ 1

no_perms_digits(1) ➞ 1

no_perms_digits(5) ➞ 3

no_perms_digits(8) ➞ 5
Notes
This challenge requires some understanding of combinatorics.
"""

def factorial(num):

    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def no_perms_digits(num):

    return len(str(factorial(num)))

print(no_perms_digits(0))
print(no_perms_digits(1))
print(no_perms_digits(2))
print(no_perms_digits(3))
print(no_perms_digits(4))
print(no_perms_digits(5))
print(no_perms_digits(6))
print(no_perms_digits(7))
print(no_perms_digits(8))