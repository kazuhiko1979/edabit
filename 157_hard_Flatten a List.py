"""
Flatten a List
Create a function that takes a list. This list can have all kinds of primitives, even other lists. The function should return a single, flat, one-dimensional, list with all elements. Here are the conditions:

If the item is a List, include each item in it and the following still apply:
If the item is a Primitive, include it as is.
Examples
flatten_list([1, 2, [3, [4, 5], 6], 7, 8]) ➞ [1, 2, 3, 4, 5, 6, 7, 8]

flatten_list([1]) ➞ [1]

flatten_list([]) ➞ []
Notes
If no input is given it should return an empty list: [].
"""

def flatten_list(lst):
	# v3
	return eval("[" + str(lst).replace("[", "").replace("]", "") + "]")

	# v2 Recursion
	# if lst == []:
	# 	return lst
	# if isinstance(lst[0], list):
	# 	return flatten_list(lst[0]) + flatten_list(lst[1:])
	# return lst[:1] + flatten_list(lst[1:])

	# v1
	# newlist = []
	# for element in lst:
	# 	print(element)
	# 	if not type(element) == list:
	# 		newlist.append(element)
	# 	else:
	# 		newlist += flatten_list(element)
	# return newlist


print(flatten_list([1, 2, [3, [4, 5], 6], 7, 8]))
