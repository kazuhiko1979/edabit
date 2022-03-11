"""
Digital Division
In this challenge, you have to verify if a number is exactly divisible by a combination of its digits. There are three possible conditions to test:

The given number is exactly divisible by each of its digits excluding the zeros.
The given number is exactly divisible by the sum of its digits.
The given number is exactly divisible by the product of its digits.
Given an integer n, implement a function that returns:

If every test is true, a string "Perfect".
If some test is true, the number of true tests (1 or 2).
If every test is false, a string "Indivisible".
Examples
digital_division(21) ➞ 1
# Exactly divisible only by the sum of its digits (2 + 1 = 3).

digital_division(128) ➞ 2
# Exactly divisible by each of its digits.
# Exactly divisible by the product of its digits (1 * 2 * 8 = 16).

digital_division(100) ➞ 2
# Exactly divisible by each of its digits (excluding zeros).
# Exactly divisible by the sum of its digits (1 + 0 + 0 = 1).

digital_division(12) ➞ "Perfect"
# Exactly divisible by each of its digits.
# Exactly divisible by 3 (sum of digits = 1 + 2).
# Exactly divisible by 2 (product of digits = 1 * 2).

digital_division(31) ➞ "Indivisible"
# Every testing condition is false.
"""

import numpy as np
from functools import reduce

def digital_division(n):

	digits = [int(char) for char in str(n) if char != "0"]
	test1 = list(filter(lambda x: n % x == 0, digits)) == digits
	test2 = n % sum(digits) == 0
	test3 = not "0" in str(n) and n % reduce(lambda x, y: x * y, digits) == 0

	# print(digits)
	# print(test1)
	# print(test2)
	# print(test3)

	tests = [test1, test2, test3]

	if tests.count(True) == 3:
		return "Perfect"
	elif tests.count(True) == 0:
		return "Indivisible"
	else:
		return tests.count(True)





	# digits = [int(i) for i in str(n)]
	#
	# test1 = all(n % d == 0 for d in digits if d != 0)
	# test2 = n%sum(digits) == 0
	# test3 = False if 0 in digits else n % np.prod(digits) == 0
	#
	# # print(test1)
	# # print(test2)
	# # print(test3)
	#
	# passed = sum((test1, test2, test3))
	#
	# # print(passed)
	#
	# return {3: 'Perfect', 0: 'Indivisible'}.get(passed, passed)




	# count_divisible = 0
	#
	# temp = 1
	# for i in list(str(n)):
	# 	temp *= int(i)
	# try:
	# 	if n % temp == 0:
	# 		count_divisible += 1
	# except ZeroDivisionError:
	# 	pass
	#
	#
	# temp2 = 0
	# for j in list(str(n)):
	# 	temp2 += int(j)
	# if n % temp2 == 0:
	# 	count_divisible += 1
	#
	#
	# bol = []
	# for x in list(str(n)):
	# 	try:
	# 		if n % int(x) == 0:
	# 			bol.append(True)
	# 		elif int(x) == 0:
	# 			bol.append(True)
	# 		else:
	# 			bol.append(False)
	# 	except ZeroDivisionError:
	# 		pass
	# if all(bol):
	# 	count_divisible += 1
	#
	#
	# if count_divisible == 3:
	# 	return "Perfect"
	# elif count_divisible == 0:
	# 	return "Indivisible"
	# else:
	# 	return count_divisible


print(digital_division(21))
print(digital_division(128))
print(digital_division(100))
print(digital_division(12))
print(digital_division(31))

