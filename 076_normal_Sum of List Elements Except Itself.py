"""
Sum of List Elements Except Itself
A list is given. Return a new list having the sum of all its elements except itself. For more clarity, check the examples below.

Clarification
[1, 2, 3, 4] = for first element => sum will be 2+3+4 = [9]
[1, 2, 3, 4] = for second element => sum will be 1+3+4 = [9, 8]
[1, 2, 3, 4] = for third element => sum will be 1+2+4 = [9, 8, 7]
[1, 2, 3, 4] = for fourth element => sum will be 1+2+3 = [9, 8, 7, 6]
Examples
lst_ele_sum([1, 2, 3, 2, 1]) ➞ [8, 7, 6, 7, 8]

lst_ele_sum([1, 2]) ➞ [2, 1]

lst_ele_sum([1, 2, 3]) ➞ [5, 4, 3]

lst_ele_sum([1, 2, 3, 4, 5]) ➞ [14, 13, 12, 11, 10]

lst_ele_sum([10, 20, 30, 40, 50, 60]) ➞ [200, 190, 180, 170, 160, 150]
"""

# def lst_ele_sum(lst):

	# total = sum(lst)
	# return [total -i for i in lst]

lst_ele_sum = lambda l:[sum(l) -x for x in l]

	# res = []
	#
	# for i in range(0, len(lst)):
	# 	temp_lst = lst.copy()
	# 	temp_lst.pop(i)
	# 	res.append(sum(temp_lst))
	# return res

print(lst_ele_sum([1, 2, 3, 2, 1]))
print(lst_ele_sum([1, 2]))
print(lst_ele_sum([1, 2, 3]))
print(lst_ele_sum([1, 2, 3, 4, 5]))
print(lst_ele_sum([10, 20, 30, 40, 50, 60]))
