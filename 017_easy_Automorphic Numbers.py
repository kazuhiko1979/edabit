"""
A number n is automorphic if n^2 ends in n.

For example: n=5, n^2=25

Create a function that takes a number and returns True if the number is automorphic, False if it isn't.

Examples
is_automorphic(5) ➞ True

is_automorphic(8) ➞ False

is_automorphic(76) ➞ True
"""
def is_automorphic(n):

    # return int(str(n**2)[-(len(str(n))):]) == n

    return str(n**2).endswith(str(n))


print(is_automorphic(0))
print(is_automorphic(1))
print(is_automorphic(5))
print(is_automorphic(76))
print(is_automorphic(36))

