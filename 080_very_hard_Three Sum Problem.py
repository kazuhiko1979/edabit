"""
Three Sum Problem
Write a function that returns all sets of three elements that sum to 0.

Examples
three_sum([0, 1, -1, -1, 2]) ➞ [[0, 1, -1], [-1, -1, 2]]

three_sum([0, 0, 0, 5, -5]) ➞ [[0, 0, 0], [0, 5, -5]]

three_sum([1, 2, 3]) ➞ []

three_sum([1]) ➞ []
Notes
The original list may contain duplicate numbers.
Each three-element sublist in your output should be distinct.
Sublists should be ordered by the first element of the sublist.
Sublists themselves should be ordered the same as the original list.
Return an empty list if no three elements sum to zero.
Return an empty list if there are fewer than three elements.
"""
# v3

import itertools

def three_sum(lst):

	return sorted([list(i) for i in set(itertools.combinations(lst, 3)) if sum(i) == 0], key=lambda x: lst.index(x[0]))

# v2
from itertools import combinations

# def three_sum(lst):
#
# 	res = []
# 	for i in combinations(lst, 3):
# 		if not sum(i) and i not in res:
# 			res.append(i)
#
# 	return [list(i) for i in res]


# v1
# def three_sum(lst):
#
# 	patterns = []
# 	n = len(lst)
# 	for i in range(n):
# 		for j in range(i+1, n):
# 			for k in range(j+1, n):
# 				patterns.append((lst[i], lst[j], lst[k]))
#
# 	lst = [list(pattern) for pattern in patterns if sum(pattern) == 0]
#
# 	non_duplicate_lst = []
# 	[non_duplicate_lst.append(sub_lst) for sub_lst in lst if sub_lst not in non_duplicate_lst]
# 	return non_duplicate_lst

print(three_sum([0, 1, -1, -1, 2]))
print(three_sum([0, 0, 0, 5, -5]))
print(three_sum([0, -1, 1, 0, -1, 1]))
print(three_sum([0, 5, 5, 0, 0]))
print(three_sum([1, 2, 3]))
print(three_sum([1]))
print(three_sum([1, 2, 3, -5, 8, 9, -9, 0]))