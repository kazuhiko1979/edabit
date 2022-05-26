"""
Geometric Mean
The geometric mean of numbers a and b is the square root of their product (i.e. √(ab)). For example, the geometric mean of 2 and 8 is √(2*8)=4.

Two integers (a and b) are randomly (and independently) chosen between 1 and n (inclusive) where n is an integer greater than one. Create a function that takes a number n as an argument and returns the probability that the geometric mean of a and b is an integer.

Examples
f(2) ➞ 0.5
# There are four possible pairs: (1, 1), (2, 1), (1, 2) and (2, 2).
# The pairs (1, 1) and (2, 2) are wanted (√(1*1)=1 and √(2*2)=2)
# but the pairs (2, 1) and (1, 2) are not (√(2*1)=√2 and √(1*2)=√2).
# Thus, the probability is 2/4 = 0.5.

f(10) ➞ 0.18

f(100) ➞ 0.031
"""

from itertools import product
import math

def f(n):

	# v2
	lst = [(a*b)**0.5 for a in range(1, n+1) for b in range(1, n+1)]
	return sum(i % 1 == 0 for i in lst) / len(lst)


	# v1
	# L = [i for i in range(1, n+1)]
	# R = sorted([i for i in range(1, n+1)], reverse=True)
	# pairs = list(product(L, R))
	#
	# count_all = len([len(str(math.sqrt(i[0]*i[1]))) - len(str(round(math.sqrt(i[0]*i[1])))) for i in pairs])
	# count_int = ([len(str(math.sqrt(i[0]*i[1]))) - len(str(round(math.sqrt(i[0]*i[1])))) for i in pairs].count(2))
	#
	# return count_int / count_all


print(f(2))
print(f(10))
print(f(100))