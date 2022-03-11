"""
Sort by Frequency
Create a function that takes a list of integers lst and sort the elements of the list by decreasing frequency of the elements. If two elements have the same frequency, sort them by increasing value.

Examples
sort_freq([2, 3, 5, 3, 7, 9, 5, 3, 7]) ➞ [3, 3, 3, 5, 5, 7, 7, 2, 9]

sort_freq([1, 2, 3, 0, 5, 0, 1, 6, 8, 8, 6, 9, 1]) ➞ [1, 1, 1, 0, 0, 6, 6, 8, 8, 2, 3, 5, 9]

sort_freq([4, 4, 2, 5, 1, 1, 3, 3, 2, 8]) ➞ [1, 1, 2, 2, 3, 3, 4, 4, 5, 8]
Notes
All input numbers will be between 0-9.
"""
from collections import Counter

def sort_freq(lst):

	return sorted(sorted(lst), key=lst.count, reverse=True)


	# lst1 = []
	# lst2 = []
	# for i in lst:
	# 	if lst.count(i) > 1:
	# 		lst2 += [i]
	# 	else:
	# 		lst1 += [i]
	#
	# # return lst2, lst1
	#
	# return sorted(lst2, key=lst2.count, reverse=True) + sorted(lst1)


	# bad!!
	# temp = {}
	#
	# for i in lst:
	# 	if i in temp:
	# 		temp[i] += 1
	# 	else:
	# 		temp[i] = 1
	#
	# # print(temp)
	#
	# res = []
	# for key, value in temp.items():
	# 	if value > 1:
	# 		res.append(str(key) * value)
	#
	# for key, value in temp.items():
	# 	if value == 1:
	# 		res.append(str(key) * value)
	#
	# # return res
	#
	# temp = []
	# txt = ""
	# for i in res:
	# 	txt += i
	# 	temp.append(txt)
	#
	# temp2 = []
	# temp2[:0] = temp[-1]
	#
	# return temp2


print(sort_freq([2, 3, 5, 3, 7, 9, 5, 3, 7]))
print(sort_freq([1, 2, 3, 0, 5, 0, 1, 6, 8, 8, 6, 9, 1]))
print(sort_freq([4, 4, 2, 5, 1, 1, 3, 3, 2, 8]))