"""
A pronic number (or otherwise called as heteromecic) is a number which is a product of two consecutive integers, that is, a number of the form n(n + 1). Create a function that determines whether a number is pronic or not.

Examples
is_heteromecic(0) ➞ True
# 0 * (0 + 1) = 0 * 1 = 0

is_heteromecic(2) ➞ True
# 1 * (1 + 1) = 1 * 2 = 2

is_heteromecic(7) ➞ False

is_heteromecic(110) ➞ True
# 10 * (10 + 1) = 10 * 11 = 110

is_heteromecic(136) ➞ False

is_heteromecic(156) ➞ True
Notes
You are expected to solve this challenge via recursion.
You can check on the Resources tab for more details about recursion.
An iterative version of this challenge can be found via this link.
"""


def is_heteromecic(n, i=0):

    if i * (i + 1) == n:
        return True
    if n == i:
        return False
    i += 1
    return is_heteromecic(n, i)


print(is_heteromecic(0))
print(is_heteromecic(2))
print(is_heteromecic(156))



