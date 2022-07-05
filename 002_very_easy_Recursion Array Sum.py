"""
Recursion: Array Sum
Write a function that finds the sum of a list. Make your function recursive.

Examples
sum_recursively([1, 2, 3, 4]) ➞ 10

sum_recursively([1, 2]) ➞ 3

sum_recursively([1]) ➞ 1

sum_recursively([]) ➞ 0
Notes
Return 0 for an empty list.
"""

def sum_recursively(lst):

	# v2
	if not lst:
		return 0
	return lst.pop() + sum_recursively(lst)



	# v1
	# if lst == []:
	# 	return 0
	# else:
	# 	return sum_recursively(lst[:-1]) + lst[-1]

print(sum_recursively([1, 2, 3, 4]))
print(sum_recursively([1, 2]))
print(sum_recursively([1]))
print(sum_recursively([]))