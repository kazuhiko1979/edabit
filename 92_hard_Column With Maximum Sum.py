"""
Column With Maximum Sum
Given a list of numbers and a value for n, split the numbers into n-sized groups. If we imagine that these groups are stacked on top of each other (see below), return the column number that has the greatest sum. If two or more columns have the same sum, return the one with the smallest column number.

Example
nums = [4, 14, 12, 7, 14, 16, 5, 13, 7, 16, 11, 19]
n = 4
Gives the array:

[[4, 14, 12, 7],
[14, 16,  5, 13],
[7, 16, 11, 19]]

# 1, 2, 3, 4 (column)
# 25, 46, 28, 39 (sum)
You would return 2, as the 2nd column has the greatest sum.

Notes
Nums will always divide into equal-length groups.
"""

import numpy as np

def col_with_max_sum(nums, n):

	# v1
	n_slice = [nums[i::4] for i in range(4)]
	return n_slice.index(max(n_slice)) + 1

	# v2
	# n_slice = [nums[i:i+n] for i in range(0, len(nums), n)]
	# transpose_Of_n_slice = [sum(i) for i in zip(*n_slice)]
	#
	# return transpose_Of_n_slice.index(max(transpose_Of_n_slice)) + 1


	# v1
	# temp = []
	#
	# while len(nums) >= n:
	# 	n_list = nums[0:n]
	# 	temp.append(n_list)
	# 	nums = nums[n:]
	#
	# temp = np.array(temp).T
	# temp = [sum(i) for i in temp]
	# return temp.index(max(temp)) + 1


print(col_with_max_sum([4, 14, 12, 7, 14, 16, 5, 13, 7, 16, 11, 19], 4))
print(col_with_max_sum([14, 9, 19, 6, 13, 13, 3, 2, 12], 3))
print(col_with_max_sum([1, 13, 15, 5, 16, 1, 4, 9, 20], 3))
print(col_with_max_sum([15, 4, 6, 10, 6, 4], 2))




