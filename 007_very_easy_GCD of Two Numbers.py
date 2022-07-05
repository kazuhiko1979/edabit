"""
Write a function that returns the greatest common divisor (GCD) of two integers.

Examples
gcd(32, 8) ➞ 8

gcd(8, 12) ➞ 4

gcd(17, 13) ➞ 1
Notes
Both values will be positive.
The GCD is the largest factor that divides both numbers.
"""

def gcd(n1, n2):

	if n2 == 0:
		return n1
	return gcd(n2, n1 % n2)


print(gcd(32, 8))
print(gcd(8, 12))
print(gcd(17, 13))
print(gcd(14, 7))
print(gcd(55, 20))
print(gcd(17, 100))

