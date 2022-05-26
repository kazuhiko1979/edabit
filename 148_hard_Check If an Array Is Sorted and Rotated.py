"""
Check If an Array Is Sorted and Rotated
Given a list of distinct integers, create a function that checks if the list is sorted and rotated clockwise. If so, return "YES"; otherwise return "NO".

Examples
check([3, 4, 5, 1, 2]) ➞ "YES"
# The above list is sorted and rotated.
# Sorted list: [1, 2, 3, 4, 5].
# Rotating this sorted list clockwise
# by 3 positions, we get: [3, 4, 5, 1, 2].

check([1, 2, 3]) ➞ "NO"
# The above list is sorted but not rotated.

check([7, 9, 11, 12, 5]) ➞ "YES"
# The above list is sorted and rotated.
# Sorted list: [5, 7, 9, 11, 12].
# Rotating this sorted list clockwise
# by 4 positions, we get: [7, 9, 11, 12, 5].
"""

def check(lst):

	# v3
	# print(sorted(lst)[1:-1])
	# print(str(lst*2))
	return 'YES' if lst != sorted(lst) and str(sorted(lst))[1:-1] in str(lst*2) else 'NO'


	# v2
	# sorted_lst = sorted(lst)
	# if lst == sorted_lst:
	# 	return 'NO'
	# start = lst.index(min(lst))
	# rotated = lst[start:] + lst[:start]
	# return 'YES' if rotated == sorted_lst else 'NO'


	# v1
	# result = []
	#
	# result.extend(lst[lst.index(min(lst)):])
	#
	# if lst[:lst.index(min(lst))] != []:
	# 	result[len(result):len(result)] = lst[:lst.index(min(lst))]
	# 	if result == sorted(lst):
	# 		return 'YES'
	# return 'NO'


print(check([3, 4, 5, 1, 2]))
print(check([1, 2, 3]))
print(check([7, 9, 11, 12, 5]))
print(check([13, 22, 34, 1, 11]))
print(check([5, 3, 4, 1]))
print(check([100, 120, 130, 50, 120, 111]))
print(check([2,1,3,4]))
print(check([1,4,1,2,3,5]))
print(check([1,1,1]))
print(check([6,10,6]))
print(check([2,1,3,4]))





