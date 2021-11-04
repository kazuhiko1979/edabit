"""
You are given two numbers a and b.
Create a function that returns the next number greater than a and b and divisible by b.

Examples
divisible_by_b(17, 8) ➞ 24

divisible_by_b(98, 3) ➞ 99

divisible_by_b(14, 11) ➞ 22
Notes
a will always be greater than b.
"""

def divisible_by_b(a, b):

    while a % b != 0:
        if a % b != 0:
            a += 1
    return a

print(divisible_by_b(17, 8))
print(divisible_by_b(98, 3))
print(divisible_by_b(14, 11))


