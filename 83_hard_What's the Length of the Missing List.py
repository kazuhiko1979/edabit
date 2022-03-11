"""
What's the Length of the Missing List?
Create a function that takes a list of lists and return the length of the missing list.

Examples
find_missing([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]) ➞ 3

find_missing([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1]]) ➞ 3

find_missing([[4, 4, 4, 4], [1], [3, 3, 3]]) ➞ 2
Notes
Test input lists won't always be sorted in order of length.
If the list of lists is None or empty, your function should return False.
If a list within the parent list is None or empty, return False.
There will always be a missing element and its length will be between the given lists.
"""

def find_missing(lst):

	if not lst or any(i in (None, []) for i in lst):
		return False
	arr = set(len(i) for i in lst)
	missing = set(range(min(arr), max(arr) + 1)) - arr
	return missing.pop()


	# if lst is None or [] in lst or lst == []:
	# 	return False
	# original = set(len(l) for l in lst)
	# return (set(range(min(original), max(original)+1)) - original).pop()


	# if not lst or not lst[0] or not lst[1]:
	# 	return False
	#
	# original = [len(i) for i in lst]
	# master = [j for j in range(min([len(i) for i in lst]), max([len(i) for i in lst])+1)]
	#
	#
	# return list(set(master) - set(original))[-1]

print(find_missing([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]))
print(find_missing([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1]]))
print(find_missing([[4, 4, 4, 4], [1], [3, 3, 3]]))
print(find_missing([[False], [False, False, False]]))
print(find_missing([["f", "r", "s"], ["d", "e"], ["a", "f", "b", "n"], ["z"], ["fg", "gty", "d", "dfr", "dr", "q"]]))
print(find_missing([[5, 2, 9], [4, 5, 1, 1, 5, 6], [1, 1], [5, 6, 7, 8, 9]]))
print(find_missing([]))
print(find_missing(None))
print(find_missing([[], [1, 2, 2]]))

