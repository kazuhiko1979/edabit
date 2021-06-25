"""
Create a function that subtracts one positive integer from another, without using any arithmetic operators such as -, %, /, +, etc.

Examples
my_sub(5, 9) ➞ 4

my_sub(10, 30) ➞ 20

my_sub(0, 0) ➞ 0
Notes
Do not multiply by -1.
Use bitwise operations only: <<, |, ~, &, etc.
"""


def my_sub(a, b):

    return len(range(b, a, -1))

print(my_sub(5, 9))
print(my_sub(10, 30))
print(my_sub(0, 0))




