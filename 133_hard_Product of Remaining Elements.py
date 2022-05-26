"""
Product of Remaining Elements
Write a function that returns True if you can partition a list into one element and the rest, such that this element is equal to the product of all other elements excluding itself.

Examples
can_partition([2, 8, 4, 1]) ➞ True
# 8 = 2 x 4 x 1

can_partition([-1, -10, 1, -2, 20]) ➞ False

can_partition([-1, -20, 5, -1, -2, 2]) ➞ True
Notes
The list may contain duplicates.
Multiple solutions can exist, any solution is sufficient to return True.
"""
import numpy as np

def can_partition(lst):

	# v3
	for i in lst:
		temp = [x for x in lst]
		temp.remove(i)
		if i == np.prod(temp):
			return True
	return False



# v2
# 	for i in range(len(lst)):
# 		if prod(lst, i) == lst[i]:
# 			return True
# 	return False
#
# def prod(lst, idx):
# 	p = 1
# 	for i in range(len(lst)):
# 		if i != idx:
# 			p = p * lst[i]
# 	return p


	# v1
	# lst_master = lst.copy()
	# result = 1
	# index = 0
	#
	# isvalid = False
	#
	# while not isvalid:
	# 	while index < len(lst):
	# 		element = lst.pop(index)
	# 		for i in lst:
	# 			result = result * i
	# 		if result == element:
	# 			isvalid = True
	# 			return isvalid
	# 		else:
	# 			index += 1
	# 			result = 1
	# 			lst = lst_master
	# 	return False

print(can_partition([-1, -10, 1, -2, 20]))
print(can_partition([-1, -20, 5, -1, -2, 2]))
print(can_partition([2, 8, 4, 1]))
print(can_partition([1, 1, -1, 1]))
print(can_partition([-1, -1, 1, 1]))
print(can_partition([0, 5, 1, -1]))
print(can_partition([0, 1, 1, -1]))
print(can_partition([0, 1, 1, 1]))
print(can_partition([0, 0, 1, 1]))
print(can_partition([0, 0, 1]))
print(can_partition([5, 5, 25, 100]))