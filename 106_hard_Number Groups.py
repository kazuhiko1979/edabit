"""
Number Groups
Given three groups of numbers, return a list containing all numbers that appear in more than one group (in ascending order).

Examples
number_groups([7, 8, 7, 3, 4], [2, 9, 1, 2, 1], [5, 6, 6, 6, 5]) ➞ []

number_groups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3]) ➞ [1, 3]

number_groups([4, 10, 9, 2, 2], [5, 3, 7, 3, 8], [6, 2, 9, 4, 2]) ➞ [2, 4, 9]

number_groups([7, 8, 4, 8, 7], [8, 5, 9, 2, 9], [6, 1, 5, 5, 6]) ➞ [5, 8]
"""
from nltk import flatten

# v3
# def number_groups(*groups):
#
# 	g1, g2, g3 = map(set, groups)
# 	return sorted(g1 & g2 | g2 & g3 | g3 & g1)

# v2
# def number_groups(*groups):
# 	g1, g2, g3 = map(set, groups)
# 	# print(g1)
# 	# print(g2)
# 	# print(g3)
# 	I12 = set(g1) & set(g2)
# 	I13 = set(g1) & set(g3)
# 	I23 = set(g2) & set(g3)
# 	I = I12 | I13 | I23
# 	return sorted(I)

# v1

def number_groups(group1, group2, group3):

	result = []

	if set(group1) & set(group2):
		set_num = set(group1) & set(group2)
		num = list(set_num)
		result.append(num)
	if set(group2) & set(group3):
		set_num = set(group2) & set(group3)
		num = list(set_num)
		result.append(num)
	if set(group1) & set(group3):
		set_num = set(group1) & set(group3)
		num = list(set_num)
		result.append(num)

	return sorted(set(flatten(result)))


print(number_groups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3]))
print(number_groups([4, 10, 9, 2, 2], [5, 3, 7, 3, 8], [6, 2, 9, 4, 2]))
print(number_groups([7, 8, 4, 8, 7], [8, 5, 9, 2, 9], [6, 1, 5, 5, 6]))
print(number_groups([4, 6, 3, 9, 9], [4, 7, 10, 6, 9], [7, 9, 1, 1, 5]))