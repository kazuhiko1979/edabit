"""
Frequency by Level of Nesting
Create a function that takes in a nested list and an element and returns the frequency of that element by nested level.

Examples
freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1)
➞ [[0, 1], [1, 2], [2, 3]]
# The list has one 1 at level 0, 2 1's at level 1, and 3 1's at level 2.

freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5)
➞ [[0, 3], [1, 4], [2, 0]]

freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2)
➞ [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]
Notes
Start the default nesting (a list with no nesting) at 0.
Output the nested levels in order (e.g. 0 first, then 1, then 2, etc).
Output 0 for the frequency if that particular level has no instances of that element (see example #2).
"""
# v2
def freq_count(lst, el):
	counter = {0: 0}
	for item in lst:
		if isinstance(item, list):
			for key, val in freq_count(item, el):
				counter[key + 1] = counter.get(key + 1, 0) + val
		elif item == el:
			counter[0] += 1
	return [[k, v] for k, v in counter.items()]


# v1
# def freq_count(lst, el):
# 	level = 0
# 	res = []
#
# 	while lst:
# 		res.append([level, lst.count(el)])
# 		level += 1
# 		lst = [x for l in lst if isinstance(l, list)
# 			   for x in l]
#
# 	return res

	# print(type(lst[0]))
	# print(lst[1])
	# print(lst[2])
	# print(lst[3])
	# print(lst[4])
	# print(lst[5])
	# print()
	# print(lst[1:])
	# print(len(lst[0]))

	# while len(lst) > 1:
	# 	if type(lst[0]) == list:
	# 		# for i in lst[0]:
	# 		# 	if type(i) == list:
	#
	# 		total.append(lst[0])
	# 		return freq_count(lst[1:], temp, total)
	# 	else:
	# 		temp.append(lst[0])
	# 		return freq_count(lst[1:], temp, total)
	# return total

	# temp = []
	# total = []
	# for i in lst:
	# 	print(i)
	# 	if type(i) == list:
	# 		total.append(i)
	# 		for j in i:
	# 			print(j)
	#
	# return total
	# 	if type(i) != list:
	# 		temp.append(i)
	# 		total.append(temp)
	# 	else:
	# 		total.append(temp)
	#
	# print(total)


	# 	if type(i) == list:
	# 		temp.append([i])
	# 	else:
	#
	# 		return freq_count(i)
	#
	# print(temp)

print(freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1))
print(freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5))