"""
Recursion: Count The Digits
Create a function that will recursively count the number of digits of a number. Conversion of the number to a string is not allowed, thus, the approach is recursive.

Examples
digits_count(4666) ➞ 4

digits_count(544) ➞ 3

digits_count(121317) ➞ 6

digits_count(0) ➞ 1

digits_count(12345) ➞ 5

digits_count(1289396387328) ➞ 13
Notes
All inputs are integers but some are in exponential form, deal with it accordingly.
You are expected to come up with a solution using the concept of recursion or the so-called recursive approach.
Check out the Resources for more topics about recursion to read on (if you aren't familiar with it yet or haven't fully understood the concept behind it before taking up this challenge or unless otherwise).
"""

def digits_count(num, count=0):


	# v3
	return 1 if -10 < num < 10 else 1 + digits_count(num // 10)

	# v2
	# if abs(num) < 10:
	# 	return 1
	# else:
	# 	return 1 + digits_count(num / 10)

	# v1
	# if type(num) == float:
	# 	num = int(num)
	#
	# if num == 0:
	# 	return 1
	#
	# if num and num != '-':
	# 	num = str(num)[:-1]
	# 	count = count + 1
	# 	return digits_count(num, count)
	# elif num == '-':
	# 	return count
	# elif num != '-':
	# 	return count




# print(digits_count(4666))
# print(digits_count(544))
# print(digits_count(121317))
# print(digits_count(0))
# print(digits_count(12345))
# print(digits_count(1289396387328))
# print(digits_count(-1232323))
# print(digits_count(-231.2e6))
print(digits_count(3.2e6))