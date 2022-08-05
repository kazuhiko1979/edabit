"""
Length of a Nested List
Python's len() method will return the number of elements in a list. For example, the list below contains 2 elements:

[1, [2, 3]]
# 2 elements, number 1 and list [2, 3]
Suppose we instead wanted to know the total number of non-nested items in the nested list. In the above case, [1, [2, 3]] contains 3 non-nested items, 1, 2 and 3.

Create a function that returns the total number of non-nested items in a nested list.

Examples
get_length([1, [2, 3]]) ➞ 3

get_length([1, [2, [3, 4]]]) ➞ 4

get_length([1, [2, [3, [4, [5, 6]]]]]) ➞ 6

get_length([1, [2], 1, [2], 1]) ➞ 5
Notes
An empty list should return 0.
"""
def get_length(lst):

	# v3
	if type(lst) is int:
		return 1
	else:
		return sum(get_length(i) for i in lst)

	# v2
	# t = 0
	# if not lst:
	# 	return 0
	# for x in lst:
	# 	if isinstance(x, list):
	# 		t += get_length(x)
	# 	else:
	# 		t += 1
	# return t







# v1
# 	if not lst:
# 		return 0
# 	else:
# 		lst = list(flatten_list(lst))
# 		return 1 + get_length(lst[1:])
#
# def flatten_list(l):
#
# 	for el in l:
# 		if isinstance(el, list):
# 			yield from flatten_list(el)
# 		else:
# 			yield el
# 	return el




print(get_length([1, [2, 3]]))
print(get_length([1, [2, [3, 4]]]))
print(get_length([1, [2, [3, [4, [5, 6]]]]]))
print(get_length([1, [2], 1, [2], 1]))
print(get_length([2, [3, [5, 7]], 4, [7]]))

# # v2
# 	if not l:
# 		return 1
# 	if type(l[0]) != list:
# 		return depth(l[1:])
# 	return 1 + depth(l[0])





# def depth(l):
# 	# v3
# 	# if isinstance(l, list):
# 	# 	return 1 + max(depth(x) for x in l)
# 	# else:
# 	# 	return 0
#
# 	# v2
# 	if not l:
# 		return 1
# 	if type(l[0]) != list:
# 		return depth(l[1:])
# 	return 1 + depth(l[0])
#
#
# 	# v1
#     # depths = []
#     # for item in l:
#     #     if isinstance(item, list):
#     #         depths.append(depth(item))
#     # if len(depths) > 0:
#     #     return 1 + max(depths)
#     # return 1
#
# print(depth([1, 2, 3, 4]))
# print(depth([1, [2, 3, 4]]))
# print(depth([1, [2, [3, 4]]]))
# print(depth([1, [2, [3, [4]]]]))
# print(depth([1, [2, [3, [4]]], 4]))
# print(depth([1, [2], 3, [4], 5, [6]]))
# print(depth([1, 2, 3, 4, [[5]], [6], 7]))

# print(flat([1, 2, 3, 4]))
# print(flat([1, [2, 3, 4]]))
# print(flat([1, [2, [3, 4]]]))
# print(flat([1, [2, [3, [4]]]]))
# print(flat([1, [2, [3, [4]]], 4]))
# print(flat([1, [2], 3, [4], 5, [6]]))
# print(flat([1, 2, 3, 4, [[5]], [6], 7]))
