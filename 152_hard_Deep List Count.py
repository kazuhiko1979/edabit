"""
Deep List Count
Create a function that takes a list and returns the number of ALL elements within it (including those within the sub-level list(s)).

Examples
deep_count([1, 2, 3]) ➞ 3

deep_count([[1], [2], [3]]) ➞ 6

deep_count(["x", "y", ["z"]]) ➞ 4

deep_count(["a", "b", ["c", "d", ["e"]]]) ➞ 7
Notes
In the examples above, notice how the sub-lists within the main list count as an element as well as the elements within that sub-list.
"""

def deep_count(lst):

	# v2
	count = 0
	for item in lst:
		if isinstance(item, list):
			count += 1 + deep_count(item)
		else:
			count += 1
	return count

	# v1
	# if not type(lst) == list:
	# 	return 0
	# count = len(lst)
	# for each_element in lst:
	# 	count += deep_count(each_element)
	# return count


print(deep_count([1, 2, 3]))
print(deep_count([[1], [2], [3]]))
print(deep_count(["x", "y", ["z"]]))
print(deep_count(["a", "b", ["c", "d", ["e"]]]))