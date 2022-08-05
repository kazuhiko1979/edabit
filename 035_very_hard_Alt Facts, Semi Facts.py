"""
Alt Facts, Semi Facts
The factorial of a positive number n is the product of all numbers from 1 to n.

5! = 5 x 4 x 3 x 2 x 1 = 120
The semifactorial (also known as the double factorial) of a positive number n is the product of all numbers from 1 to n that have the same parity (i.e. odd or even) as n.

12!! = 12 x 10 x 8 x 6 x 4 x 2 = 46,080

7!! = 7 x 5 x 3 x 1 = 105
The alternating factorial of a positive number n is the sum of the consecutive factorials from n to 1, where every other factorial is multiplied by -1.

Alternating factorial of 1:

af(1) = 1!
Alternating factorial of 2:

af(2) = 2! + (-1)x(1!) = 2! - 1! = 2 -1 = 1
Alternating factorial of 3:

af(3) = 3! - 2! + 1! = 6 - 2 + 1 = 5
Create a function that takes a number n and returns the difference between the alternating factorial and semifactorial of n.

Examples
alt_semi(1) ➞ 0

alt_semi(2) ➞ -1

alt_semi(3)➞ 2
"""

def alt_semi(n):

	def fac(n):
		if n <= 1:
			return n
		return n*fac(n-1)

	def semi(n):
		if n <= 2:
			return n
		return n*semi(n-2)

	def alt(n):
		if n <= 1:
			return n
		return fac(n)+(-1) * (alt(n-1))

	return alt(n) - semi(n)

print(alt_semi(3))


