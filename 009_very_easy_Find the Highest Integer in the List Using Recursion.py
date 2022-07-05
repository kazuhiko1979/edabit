"""
Find the Highest Integer in the List Using Recursion
Create a function that finds the highest integer in the list using recursion.

Examples
find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99

find_highest([0, 12, 4, 87]) ➞ 87

find_highest([8]) ➞ 8
Notes
Please use the recursion to solve this (not the max() method).
"""

def find_highest(lst:int) -> int:

	# v2
	if len(lst) == 1:
		return lst[0]
	r = find_highest(lst[1:])
	return r if r > lst[0] else lst[0]

	# v1
	# if len(lst) <= 1:
	# 	return lst[0]
	# else:
	# 	if lst[0] > find_highest(lst[1:]):
	# 		return lst[0]
	# 	else:
	# 		return find_highest(lst[1:])

print(find_highest([-1, 3, 5, 6, 99, 12, 2]))
print(find_highest([0, 12, 4, 87]))




