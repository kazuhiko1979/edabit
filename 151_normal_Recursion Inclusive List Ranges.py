"""
Recursion: Inclusive List Ranges
Write a function that, given the start start_num and end end_num values, return a list containing all the numbers inclusive to that range. See examples below.

Examples
inclusive_list(1, 5) ➞ [1, 2, 3, 4, 5]

inclusive_list(2, 8) ➞ [2, 3, 4, 5, 6, 7, 8]

inclusive_list(10, 20) ➞ [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

inclusive_list(17, 5) ➞ [17]
Notes
The numbers in the list are sorted in ascending order.
If start_num is greater than end_num, return a list with the higher value. See example
"""

def inclusive_list(start_num, end_num):

	# v1
	# if start_num >= end_num:
	# 	return [start_num]
	# return [start_num] + inclusive_list(start_num + 1, end_num)

	if start_num == end_num:
		return [start_num]
	if start_num < end_num:
		return [start_num] + inclusive_list(start_num + 1, end_num)
	else:
		return [start_num] + inclusive_list(start_num - 1, end_num)




print(inclusive_list(1, 5))
print(inclusive_list(2, 8))
print(inclusive_list(10, 20))
print(inclusive_list(17, 5))