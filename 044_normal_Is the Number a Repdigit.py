"""
A repdigit is a positive number composed out of the same digit. Create a function that takes an integer and returns whether it's a repdigit or not.

Examples
is_repdigit(66) ➞ True

is_repdigit(0) ➞ True

is_repdigit(-11) ➞ False
Notes
The number 0 should return True (even though it's not a positive number).
Check the Resources tab for more info on repdigits.
"""

def is_repdigit(num):

    return num >= 0 and len(set(str(num))) == 1

    # if 0 <= num < 10:
    #     return True
    # elif len(set(list(str(num)))) == 1:
    #     return True
    # else:
    #     return False

print(is_repdigit(66))
print(is_repdigit(0))
print(is_repdigit(-11))
print(is_repdigit(1001))

