"""
Sort by Answer
Given a list of math expressions, create a function which sorts the list by their answer. It should be sorted in ascending order.

Examples
sort_by_answer(["1 + 1", "1 + 7", "1 + 5", "1 + 4"]) ➞ ["1 + 1", "1 + 4", "1 + 5", "1 + 7"]

sort_by_answer(["4 - 4", "2 - 2", "5 - 5", "10 - 10"]) ➞ ["4 - 4", "2 - 2", "5 - 5", "10 - 10"]

sort_by_answer(["2 + 2", "2 - 2", "2 * 1"]) ➞ ["2 - 2", "2 * 1", "2 + 2"]
Notes
If multiple expressions have the same answer, put them in the order of which they appear (see example #2).
You won't need to worry about divisions by zero.
The symbol used for multiplication is x instead of *.
"""

def sort_by_answer(lst):

	# v3
	return sorted(lst, key=lambda x: eval(x.replace('x', '*')))

	# v2
	# tup_lst = []
	# for exp in lst:
	# 	if "x" not in exp:
	# 		tup_lst.append((eval(exp), exp))
	# 	else:
	# 		tup_lst.append((eval(exp.replace('x', '*')), exp))
	# return [x[1] for x in sorted(tup_lst, key=lambda tup:tup[0])]


	# v1
	# temp_lst = []
	# sorted_list = []
	#
	# for i in lst:
	# 	if "x" in i:
	# 		i = i.replace("x", "*")
	# 		sorted_list.append(eval(i))
	# 		temp_lst.append(i)
	# 	else:
	# 		sorted_list.append(eval(i))
	# 		temp_lst.append(i)
	# sorted_list = sorted(sorted_list)
	#
	# temp = []
	# indexOfLst = 0
	# indexOfSortedLst = 0
	#
	# while len(temp_lst) > 0:
	# 	if eval(temp_lst[indexOfLst]) == sorted_list[indexOfSortedLst]:
	# 		if '*' in temp_lst[indexOfLst]:
	# 			temp_lst[indexOfLst] = temp_lst[indexOfLst].replace("*", "x")
	# 			temp.append(temp_lst[indexOfLst])
	# 			temp_lst.remove(temp_lst[indexOfLst])
	# 			sorted_list.remove(sorted_list[indexOfSortedLst])
	# 			indexOfLst = 0
	# 			indexOfSortedLst = 0
	#
	# 		else:
	# 			temp.append(temp_lst[indexOfLst])
	# 			temp_lst.remove(temp_lst[indexOfLst])
	# 			sorted_list.remove(sorted_list[indexOfSortedLst])
	# 			indexOfLst = 0
	# 			indexOfSortedLst = 0
	# 	else:
	# 		indexOfLst += 1
	# 		indexOfSortedLst = 0
	# return temp


print(sort_by_answer(["1 + 1", "1 + 7", "1 + 5", "1 + 4"]))
print(sort_by_answer(["2 + 2", "2 - 2", "2 x 2", "2 / 2"]))
# print(sort_by_answer(["1 x 1", "3 x 3", "-1 x -1", "-3 x -3"]))
# print(sort_by_answer(["4 - 4", "2 - 2", "5 - 5", "10 - 10"]))
# print(sort_by_answer(["1 x 1", "3 x 3", "-1 x -1", "-3 x -3"]))
# print(sort_by_answer(["1 * 1", "3 * 3", "-1 * -1", "-3 * -3"]))
# print(sort_by_answer(["49 x -6", "21 - 25", "-11 / 26", "6 + -37", "1 / 49", "22 x -46", "-7 / 10", "16 + -34", "-37 x -27", "23 / -41"]))
# print(sort_by_answer(["2 + 2", "2 - 2", "2 * 1"]))
# print(sort_by_answer(["49 x -6", "21 - 25", "-11 / 26", "6 + -37", "1 / 49", "22 x -46", "-7 / 10", "16 + -34", "-37 x -27", "23 / -41"]))

