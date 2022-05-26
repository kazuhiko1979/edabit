"""
All Pairs that Sum to Target
Create a function that returns all pairs of numbers in a list that sum to a target. Sort the pairs in ascending order with respect to the smaller number, then order each pair in this order: [smaller, larger].

Examples
all_pairs([2, 4, 5, 3], 7) ➞ [[2, 5], [3, 4]]
# 2 + 5 = 7, 3 + 4 = 7

all_pairs([5, 3, 9, 2, 1], 3) ➞ [[1, 2]]

all_pairs([4, 5, 1, 3, 6, 8], 9) ➞ [[1, 8], [3, 6], [4, 5]]
# Sorted: 1 < 3 < 4; each pair is ordered [smaller, larger]
Notes
If no pairs are found, return an empty list [].
You are only allowed to use each number once in a pair.
"""
from itertools import combinations

def all_pairs(lst, target):

	# v4
	return [list(i) for i in combinations(sorted(lst), 2) if sum(i) == target]


	# v3
	# result = []
	# comb = list(combinations(lst, 2))
	# # print(comb)
	# for tup in comb:
	# 	if sum(tup) == target:
	# 		result.append(tup)
	# return sorted([sorted(list(i)) for i in result])


	# v2
	# return sorted([sorted([a, b]) for idx, a in enumerate(lst) for b in lst[idx+1:] if sum([a, b]) == target])

	# V1
	# result = []
	# for idx, a in enumerate(lst):
	# 	for b in lst[idx+1:]:
	# 		if sum([a,b]) == target:
	# 			result.append(sorted([a,b]))
	# return sorted(result)

print(all_pairs([2, 4, 5, 3], 7))
print(all_pairs([5, 3, 9, 2, 1], 3))
print(all_pairs([4, 5, 1, 3, 6, 8], 9))
print(all_pairs([5, 2], 14))
print(all_pairs([5, 5, 2], 14))
print(all_pairs([8, 7, 7, 2, 4, 6], 14))
print(all_pairs([8, 7, 2, 4, 6], 14))
print(all_pairs([1, 3, 5, 4, 0], 4))






