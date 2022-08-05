"""
Total Count of Numbers in a MultiDimensional List
Create a function that takes a multidimensional list and returns the total count of numbers in that list.

Examples
count_number([["", 17.2, 5, "edabit"]]) ➞ 2
# 17.2 and 5.

count_number([[[[[2, 14]]], 2, 3, 4]]) ➞ 5
# 2, 14, 2, 3 and 4.

count_number([["number"]]) ➞ 0
Notes
Input may be a list of numbers, strings and empty lists.
"""
# def flatten_list(l):
	#
    # for el in l:
    #     if isinstance(el, list):
    #         yield from flatten_list(el)
    #     else:
    #         yield el

def count_number(lst):

	# v2
	count = 0
	for l in lst:
		if type(l) is list:
			count += count_number(l)
		elif type(l) is float or type(l) is int:
			count += 1
	return count



	# lst = list(flatten_list(lst))
	#
	# temp = []
	# for i in lst:
	# 	if isinstance(i, int):
	# 		temp.append(i)
	# 	if isinstance(i, float):
	# 		temp.append(i)
	# 	else:
	# 		continue
	# return len(temp)


print(count_number([["", 17.2, 5, "edabit"]]))
print(count_number([[[[[3.1415926535, 1.618, "deep"]]], 2, 3, 4]]))
print(count_number([0, [12, "depth", [[2]]]]))
print(count_number([["number"]]))
print(count_number([1, 2, 3, 4, 5, 6]))
