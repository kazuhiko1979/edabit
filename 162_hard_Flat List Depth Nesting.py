"""
Create a function that can nest a flat list to represent an incremental depth level sequence.

Examples
incremental_depth([1, 2]) ➞ [1, [2]]

incremental_depth([1, 2, 3, 4, 5]) ➞ [1, [2, [3, [4, [5]]]]]

incremental_depth([1, 3, 2, 6]) ➞ [1, [3, [2, [6]]]]

incremental_depth(["dog", "cat", "cow"]) ➞ ["dog", ["cat", ["cow"]]]
Notes
The elements do not matter to the function, you should increment by index.
Expect the array length to be from 2-20.
"""

def incremental_depth(lst):

	# v1
	if len(lst) == 1:
		return lst
	else:
		return [lst[0], incremental_depth(lst[1:])]


	# print(type([lst[0]]))
	# print(type([lst[1]]))
	# return [lst[0]].append([lst[1]])
	# return ori

	# if lst is None:
	# 	return ori
	# else:
	# 	return ori.append([lst[-1]]) + incremental_depth(lst[:-1])


# for i in reversed(lst):
	# 	ori.append([i])
	# return incremental_depth(lst[:-1])

print(incremental_depth([1, 2, 3, 4, 5]))
print(incremental_depth([1, 3, 2, 6]))
print(incremental_depth(["dog", "cat", "cow"]))