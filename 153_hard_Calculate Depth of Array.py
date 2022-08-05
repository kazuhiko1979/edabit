"""
Calculate Depth of Array
Given a list, write a function to calculate it's depth. Assume a normal list has a depth of 1.

Examples
depth([1, 2, 3, 4]) ➞ 1

depth([1, [2, 3, 4]]) ➞ 2

depth([1, [2, [3, 4]]]) ➞ 3

depth([1, [2, [3, [4]]]]) ➞ 4
"""

def depth(l):
	# v3
	# if isinstance(l, list):
	# 	return 1 + max(depth(x) for x in l)
	# else:
	# 	return 0

	# v2
	if not l:
		return 1
	if type(l[0]) != list:
		return depth(l[1:])
	return 1 + depth(l[0])


	# v1
    # depths = []
    # for item in l:
    #     if isinstance(item, list):
    #         depths.append(depth(item))
    # if len(depths) > 0:
    #     return 1 + max(depths)
    # return 1

print(depth([1, 2, 3, 4]))
print(depth([1, [2, 3, 4]]))
print(depth([1, [2, [3, 4]]]))
print(depth([1, [2, [3, [4]]]]))
print(depth([1, [2, [3, [4]]], 4]))
print(depth([1, [2], 3, [4], 5, [6]]))
print(depth([1, 2, 3, 4, [[5]], [6], 7]))

# print(flat([1, 2, 3, 4]))
# print(flat([1, [2, 3, 4]]))
# print(flat([1, [2, [3, 4]]]))
# print(flat([1, [2, [3, [4]]]]))
# print(flat([1, [2, [3, [4]]], 4]))
# print(flat([1, [2], 3, [4], 5, [6]]))
# print(flat([1, 2, 3, 4, [[5]], [6], 7]))
