"""
Recursion: List Summation
Create a function that sums up all the elements in the list recursively. The use of the sum() built-in function is not allowed, thus, the approach is recursive.

Examples
recur_add([1, 2, 3, 4, 10, 11]) ➞ 31

recur_add([-3, 4, 11, 10, 21, 32, -9]) ➞ 66

recur_add([-21, -7, 19, 3, 4, -8]) ➞ -10
Notes
You're expected to solve this challenge using a recursive approach.
"""

def recur_add(lst):

	# v2
	return 0 if not lst else lst[0] + recur_add(lst[1:])

	# v1
	# if len(lst) <= 1:
	# 	return lst[0] if lst else 0
	# current = lst.pop()
	# lst[-1] += current
	# return recur_add(lst)


print(recur_add([1, 2, 3, 4, 10, 11]))
print(recur_add([-3, 4, 11, 10, 21, 32, -9]))

