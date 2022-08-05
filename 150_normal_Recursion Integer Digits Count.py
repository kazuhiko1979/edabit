"""
Recursion: Integer Digits Count
Create a function that recursively counts the integer's number of digits.

Examples
count(318) ➞ 3

count(-92563) ➞ 5

count(4666) ➞ 4

count(-314890) ➞ 6

count(654321) ➞ 6

count(638476) ➞ 6
Notes
You are expected to solve this challenge via recursion.
"""

def count(num):

	# v2
	# if num < 0:
	# 	return count(-num)
	# if num < 10:
	# 	return 1
	# return 1 + count(num // 10)

	# v1
	# num = abs(num)
	#
	# if len(str(num)) > 1:
	# 	return 1 + count(int(str(num)[0:-1]))
	# return 1

print(count(318))
print(count(-92563))
print(count(-314890))
