"""
数値が少なくとも1回発生する 、2つの一意の数値を返す関数を記述します。
出力は、入力と同じ順序を維持します。

return_unique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]

return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]

return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]
"""

def return_unique(lst):

	return [i for i in lst if lst.count(i) == 1]

	# dic = dict((i, lst.count(i)) for i in lst)
	# return [k for k, v in dic.items() if v == 1]

	# return dic
	# temp = {}
	# for i in lst:
	# 	if i in temp:
	# 		temp[i] += 1
	# 	else:
	# 		temp[i] = 1
	# # return temp
	#
	# return [k for k, v in temp.items() if v == 1]

print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))


























































# """
# In each input list, every number repeats at least once, except for two. Write a function that returns the two unique numbers.
#
# Examples
# return_unique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]
#
# return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]
#
# return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]
# Notes
# Keep the same ordering in the output.
# """
#
#
# def return_unique(lst):
#
#     # My
#     # temp = {}
#     # for i in lst:
#     #     if i in temp:
#     #         temp[i] += 1
#     #     else:
#     #         temp[i] = 1
#     # # print(temp)
#     #
#     # return [k for k, v in temp.items() if v == 1]
#
#
#     # dic = (dict((i, lst.count(i)) for i in lst))
#     # print(dic)
#     # return [k for k, v in dic.items() if v == 1]
#
#
#     # return [i for i in lst if lst.count(i) == 1]


# print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
# print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
# print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))
# print(return_unique([4, 3, 9, 9, 1, 1, 6, 1, 6, 2, 4]))
# print(return_unique([44, 44, 44, 2, 55, 55, 55, 0, 66, 66, 66]))
# print(return_unique([-9, -9, -9, 7, -9, -9, 1]))
# print(return_unique([2, 2, -19, 2, 7, 7, 4, 9, 9, 0, 0, 3, 3, 3]))