"""
Count The Digits
Create a function that counts the number of digits in a number. Conversion of the number to a string is not allowed, thus, the approach is either recursive or iterative.

Examples
digits_count(4666) ➞ 4

digits_count(544) ➞ 3

digits_count(121317) ➞ 6

digits_count(0) ➞ 1

digits_count(12345) ➞ 5

digits_count(1289396387328) ➞ 13
Notes
All inputs are integers but some are in exponential form, deal with it accordingly.
"""

def digits_count(num):

	count = 1
	num = abs(num)

	if num < 10:
		return count

	while True:
		count += 1
		num = num // 10
		if num < 10:
			break
	return count



	# V1
	#
	# if num == 0:
	# 	return 1
	#
	# count = 0
	#
	# while num != 0:
	# 	num //= 10
	# 	count += 1
	#
	# return count

print(digits_count(4666))
print(digits_count(544))
print(digits_count(121317))
print(digits_count(0))
print(digits_count(12345))
print(digits_count(1289396387328))
