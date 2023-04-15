"""
Primitive Pythagorean Triples
A Pythagorean triple is a set of three integer numbers that form a right triangle. The sum of the squares of the two smaller numbers should equal the square of the largest number. Given three numbers a, b and c (c being the largest):

a^2 + b^2 = c^2
Furthermore, a Pythagorean triple is said to be primitive if the three numbers are pairwise coprime - that is, the greatest common prime factor between any two numbers is 1.

Create a function that takes a list of three numbers (unordered) and returns True if the numbers constitute a primitive Pythagorean triple, False otherwise.

Examples
is_prim_pyth_triple([4, 5, 3]) ➞ True

is_prim_pyth_triple([7, 12, 13]) ➞ False

is_prim_pyth_triple([39, 15, 36]) ➞ False
# Pythagorean triple, but not primitive.

is_prim_pyth_triple([77, 36, 85]) ➞ True
"""

# v2


def is_prim_pyth_triple(lst):
	a, b, c = sorted(lst)
	return a*a + b*b == c*c and gcd(a, gcd(b, c)) == 1


def gcd(a, b):
	return a if not b else gcd(b, a % b)



# v1
# def is_prim_pyth_triple(lst):
#
# 	lst = sorted(lst, reverse=True)
# 	if getGCD(lst[1], lst[2]) == 1:
# 		return pow(lst[0], 2) == pow(lst[1], 2) + pow(lst[2], 2)
# 	return False
#
#
# def getGCD(a, b):
# 	return b == 0 and a or getGCD(b, a % b)


print(is_prim_pyth_triple([4, 5, 3]))
print(is_prim_pyth_triple([7, 12, 13]))
print(is_prim_pyth_triple([39,15,36]))
print(is_prim_pyth_triple([77,36,85]))
print(is_prim_pyth_triple([35,28,21]))
print(is_prim_pyth_triple([80,89,39]))