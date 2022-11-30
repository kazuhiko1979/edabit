"""
Numbers Transformation
Mubashir (as always) needs your help to complete his assignment.

You are given two positive integers n and m. You have to perform some basic mathematical operations on n to obtain m. These are your options:

(n-1)/2   - if (n-1) is divisible by 2
n/2       - if n is divisible by 2
n*2
Create a function that returns the minimum number of steps required to transform n into m.

Examples
number_transform(2, 8) ➞ 2
// 2 * 2 = 4
// 4 * 2 = 8

number_transform(9, 2) ➞ 2
// (9-1) / 2 = 4
// 4 / 2 = 2

number_transform(1024, 1024) ➞ 0
Notes
m will always be a power of 2.
"""
# v3
from math import log2

def number_transform(n, m):

	return abs(int(log2(n - 1) - 2 if n > 1 and n % 2 else log2(n)) - int(log2(m)))


# v2
# def number_transform(n, m):
#
# 	# return 0 if n==m else 1 + (number_transform(n//2, m) if n>m else number_transform(n, m//2))
#
# 	if n==m:
# 		return 0
# 	if n>m:
# 		return 1 + (number_transform(n // 2, m))
# 	else:
# 		return 1 + number_transform(n, m // 2)

# v1
# def number_transform(n, m):
#
# 	count = 0
#
# 	while n != m:
# 		if (n - 1) % 2 == 0 and n > 1:
# 			n = (n - 1) / 2
# 			count += 1
# 		elif n % 2 == 0 and n > m:
# 			n = n / 2
# 			count += 1
# 		else:
# 			n = n * 2
# 			count += 1
# 	return count


print(number_transform(1, 1))
print(number_transform(2, 4))
print(number_transform(3, 8))
print(number_transform(4, 16))
print(number_transform(4, 1))
print(number_transform(1, 4))
print(number_transform(1024, 1024))
print(number_transform(2048, 1024))
print(number_transform(2048, 2))
print(number_transform(4096, 2))
print(number_transform(4096, 1))
