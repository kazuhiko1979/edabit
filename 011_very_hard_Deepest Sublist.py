"""
Deepest Sublist
You are given a list which may contain sublists. Your task is to find the depth of the deepest sublist.

[a] = 1 depth
[[a]] = 2 depth
[[[a]]] = 3 depth, etc
Examples
deepest([1, [2, 3], 4, [5, 6]]) ➞ 2

deepest([[[[[[[[[[1]]]]]]]]]]) ➞ 10

deepest([1, 4, [1, 4, [1, 4, [1, 4, [5]]]]]) ➞ 5
"""
import numpy as np

# Ref
# https://stackoverflow.com/questions/6039103/counting-depth-or-the-deepest-level-a-nested-list-goes-to


def deepest(lst):

	# v4
	if type(lst) != list:
		return 0

	return 1 + max(deepest(e) for e in lst)

	# # v3
	# d = 0
	# for item in lst:
	# 	if isinstance(item, list):
	# 		d = max(deepest(item), d)
	# return d + 1

	# v1
	# if isinstance(lst, list):
	# 	return 1 + max(deepest(item) for item in lst)
	# else:
	# 	return 0

	# v2
	# depths = []
	# for item in lst:
	# 	if isinstance(item, list):
	# 		depths.append(deepest(item))
	# if len(depths) > 0:
	# 	return 1 + max(depths)
	# return 1


print(deepest([1, 4, 5]))
print(deepest([[2, 3], 4, [6, 7, [8]]]))
print(deepest([5, [[[[[[[[[[2]]]]]]]]]], [[[[[[[[[[[[4]]]]]]]]]]]]]))
print(deepest([[[3, 2, [[4]], 8], [[2, 4], 5]], 3, 5, [9, 1]]))
print(deepest([[6, 9, 6], [[[1, 4], 0, 8], [8, 0, [4, 1]]], [[5, 3, 4], [4, 3, 5]]]))



