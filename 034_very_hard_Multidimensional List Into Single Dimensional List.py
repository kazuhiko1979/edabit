"""
Multidimensional List Into Single Dimensional List
Create a function that takes a multi-dimensional list and converts it (recursively) into a single-dimensional list and returns it. Use a RECURSIVE approach.

Examples
flatten([[17.2, 5, "code"]]) ➞ [17.2, 5, "code"]

flatten([[[[[2, 14, "rubber"]]], 2, 3, 4]])) ➞ [2, 14, "rubber", 2, 3, 4]

flatten([["dimension"]]) ➞ ["dimension"]
Notes
Input contains at least one element.
The use of built-in methods is discouraged.
"""

def flatten(lst):

	# v2
	if not isinstance(lst, list):
		return [lst]
	return sum((flatten(item) for item in lst), [])




	# v1
	# if not lst and lst != 0:
	# 	return []
	# if not isinstance(lst, list):
	# 	return [lst]
	# elif len(lst) >= 0:
	# 	return flatten(lst[0]) + flatten(lst[1:])

print(flatten([[17.2, 5, "code"]]))
print(flatten([[[[[2, 14, "rubber"]]], 2, 3, 4]]))

