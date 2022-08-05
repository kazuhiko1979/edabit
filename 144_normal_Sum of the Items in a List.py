"""
Sum of the Items in a List
Create a function that takes a list and returns the sum of all the items in that list.

Examples
sum_list([1, 2, 3]) ➞ 6
# 1 + 2 + 3 = 6

sum_list([1, [2, [1]], 3]) ➞ 7
# 1 + 2 + 1 + 3 = 7
Notes
An item in the list can be another list.
Try solving it in a recursive approach without using the built-in sum() function.
"""
# v3

def sum_list(lst):

	# v3
	total = 0
	for i in lst:
		if type(i) is int:
			total += i
		else:
			total += sum_list(i)
	return total



# v2
# def sum_list(lst):
# 	if type(lst) == int:
# 		return lst
# 	if not lst:
# 		return 0
# 	return sum_list(lst[0]) + sum_list(lst[1:])


# v1
# def sum_flat_list(flat_list, index, total):
#
# 	if index > 0:
# 		total += flat_list[index]
# 		return sum_flat_list(flat_list, index-1, total)
# 	else:
# 		total += flat_list[index]
# 		return total
#
# def sum_list(lst):
#
# 	total = 0
#
# 	flat_list = []
# 	fringe = [lst]
#
# 	while len(fringe) > 0:
# 		node = fringe.pop(0)
# 		if isinstance(node, list):
# 			fringe = node + fringe
# 		else:
# 			flat_list.append(node)
#
# 	return sum_flat_list(flat_list, len(flat_list)-1, total)

print(sum_list([1, 2, 3]))
print(sum_list([1, [2, [1]], 3]))
print(sum_list([1, [1, 2], [3, 1]]))
print(sum_list([[1, 1], [2, 8], 8]))
