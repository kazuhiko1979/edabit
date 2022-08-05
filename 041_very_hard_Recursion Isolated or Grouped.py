"""
Recursion: Isolated or Grouped?
Write a function that extracts the max value of a number in a list. If there are two or more max values, return it as a list, otherwise, return the number. This process could be relatively easy with some of the built-in list functions but the required approach is recursive.

Examples
iso_group([31, 7, 2, 13, 7, 9, 10, 13]) ➞ 31

iso_group([1, 3, 9, 5, 1, 7, 9, -9]) ➞ [9, 9]

iso_group([97, 19, -18, 97, 36, 23, -97]) ➞ [97, 97]

iso_group([-31, -7, -13, -7, -9, -13]) ➞ [-7, -7]

iso_group([-1, -3, -9, -5, -1, -7, -9, -9]) ➞ [-1, -1]

iso_group([107, 19, -18, 79, 36, 23, 97]) ➞ 107
"""
# v2
def iso_group(lst, best=[]):

	if not lst:
		return best if len(best) > 1 else best[0]

	n = lst[0]
	if not best or n > best[0]:
		best = [n]
	elif n == best[0]:
		best.append(n)
	return iso_group(lst[1:], best)


# v1
# import copy
#
# def iso_group(lst, max=[]):
#
# 	if not lst:
# 		result = copy.deepcopy(max)
# 		max.clear()
# 		if len(result) == 1:
# 			result = result[0]
# 		return result
#
# 	if not max:
# 		max.append(lst[0])
# 		return iso_group_helper(lst[1:], max)
# 	else:
# 		return iso_group_helper(lst, max)
#
#
# def iso_group_helper(lst, max):
#
# 	if lst[0] > max[0]:
# 		max.clear()
# 		max.append(lst[0])
# 		return iso_group(lst[1:], max)
#
# 	if lst[0] < max[0]:
# 		return iso_group(lst[1:], max)
#
# 	if lst[0] == max[0]:
# 		max.append(lst[0])
# 		return iso_group(lst[1:], max)



print(iso_group([31, 7, 2, 13, 7, 9, 10, 13]))
print(iso_group([1, 3, 9, 5, 1, 7, 9, -9]))
print(iso_group([97, 19, -18, 97, 36, 23, -97]))
print(iso_group([-31, -7, -13, -7, -9, -13]))
print(iso_group([-1, -3, -9, -5, -1, -7, -9, -9]))
print(iso_group([107, 19, -18, 79, 36, 23, 97]) )
