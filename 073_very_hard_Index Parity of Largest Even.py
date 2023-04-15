"""
Index Parity of Largest Even
Write a function that returns the largest even integer in a list with its corresponding index and the parity of that index, but determining the parity of that index is limited to not using the modulo operator %.

Output Structure:
You have to return a Dictionary.

{"@odd|even index " + index_of_largest: largest_integer}
Examples
bitwise_index([107, 19, 36, -18, -78, 24, 97]) ➞ {"@even index 2": 36}

bitwise_index([31, 7, 2, 13, 7, 9, 10, 13]) ➞ {"@even index 6": 10}

bitwise_index([4, 4, 4, 4, 4, 4]) ➞ {"@even index 0": 4}

bitwise_index([-31, -7, -13, -7, -9, -13]) ➞ "No even integer found!"
Notes
The use of index() and max() are restricted.
If there are no even integers, return "No even integer found!".
The set of limitations imposed on this challenge dictates the level of difficulty.
Another version of this challenge that deals with recursion can be found here.
"""
# v2
def bitwise_index(lst):

	mx = sorted([i for i in lst if not i & 1])
	if not mx:
		return "No even integer found!"
	for i, num in enumerate(lst):
		if num == mx[-1]:
			return {'@{} index {}'.format(["even", "odd"][i & 1], i): mx[-1]}


# v1
# import copy
#
#
# def bitwise_index(lst):
#
# 	even_list = [is_even(i)[1] if is_even(i)[0] else -1 for i in lst]
#
# 	if set(even_list) == {-1}:
# 		return "No even integer found!"
# 	elif len(set(even_list)) == 1:
# 		return dict([["@even index 0", even_list[0]]])
#
# 	max_int = even_list[0]
#
# 	for idx, n in enumerate(even_list):
# 		if n > max_int:
# 			max_int = n
# 			max_idx = idx
# 	return dict([["@{} index {}".format(is_even(max_idx)[2], max_idx), max_int]])
#
#
# def is_even(num):
# 	original_num = copy.deepcopy(num)
# 	while num >= 2:
# 		num -= 2
# 	if num == 0:
# 		return [True, original_num, "even"]
# 	else:
# 		return [False, original_num, "odd"]


print(bitwise_index([107, 19, 36, -18, -78, 24, 97]))
print(bitwise_index([31, 7, 2, 13, 7, 9, 10, 13]))
print(bitwise_index([4, 4, 4, 4, 4, 4]))
print(bitwise_index([-31, -7, -13, -7, -9, -13]))
print(bitwise_index([1, 128, 9, 56, -1, 7, 18, 49]))
print(bitwise_index([63, 12, 77, 112, 75, 92]))
print(bitwise_index([6, 6, 6, 6, 6, 6]))

