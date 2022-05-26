"""
Shuffled Properly?
Given a list of 10 numbers, return whether or not the list is shuffled sufficiently enough. In this case, if 3 or more numbers appear consecutively (ascending or descending), return False.

Examples
is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]) ➞ False
# 1, 2, 3 appear consecutively

is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]) ➞ False
# 9, 8, 7, 6 appear consecutively

is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]) ➞ True
# No consecutive numbers appear

is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) ➞ True
# No consecutive numbers appear
Notes
Only steps of 1 in either direction count as consecutive (i.e. a sequence of odd and even numbers would count as being properly shuffled (see example #4)).
You will get numbers from 1-10.
"""


def is_shuffled_well(lst) -> bool:

	# v3
	return "11" not in "".join([str(abs(a-b)) for a, b in zip(lst, lst[1:])])



	# v2
	# count_up, count_down = 0, 0
	# for i in range(1, len(lst)):
	# 	if lst[i] == lst[i - 1] + 1:
	# 		count_up += 1
	# 		count_down = 0
	# 	elif lst[i] == lst[i - 1] - 1:
	# 		count_down += 1
	# 		count_up = 0
	# 	else:
	# 		count_up, count_down = 0, 0
	# 	if count_up == 2 or count_down == 2:
	# 		return False
	# return True

	# v1
	# count = 0
	# current_index = 0
	# consequence = True
	# consequence_count = 0
	#
	# try:
	#   while current_index < len(lst):
	# 	if abs(lst[current_index] - lst[current_index+1]) > 1:
	# 	  count = 0
	# 	  current_index += 1
	# 	elif abs(lst[current_index] - lst[current_index+1]) == 1:
	# 	  count += 1
	# 	  if count == 2:
	# 		consequence = False
	# 		count = 0
	# 		consequence_count += 1
	# 	  else:
	# 		current_index += 1
	# except:
	#   return consequence


print(is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]))
print(is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]))
print(is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]))
print(is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))
print(is_shuffled_well([5, 6, 7, 9, 1, 10, 3, 8, 2, 4]))
print(is_shuffled_well([3, 9, 7, 5, 2, 4, 10, 1, 8, 6]))
print(is_shuffled_well([6, 4, 2, 1, 3, 7, 8, 10, 5, 9]))
print(is_shuffled_well([2, 6, 10, 9, 8, 1, 4, 7, 3, 5]))
print(is_shuffled_well([6, 10, 5, 8, 4, 2, 7, 9, 3, 1]))
