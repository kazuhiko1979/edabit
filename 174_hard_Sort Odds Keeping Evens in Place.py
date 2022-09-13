"""
Sort Odds Keeping Evens in Place
Write a function that sorts only the odd numbers in a list in ascending order, keeping the even numbers in their current place.

For example, if our input list is: [5, 2, 6, 6, 1, 4, 9, 3]:

[_, 2, 6, 6, _, 4, _, _]  # Keep evens in place.

# Sort odds: [5, 1, 9, 3] => [1, 3, 5, 9]

[1, 2, 6, 6, 3, 4, 5, 9] # Final list.
Examples
odd_sort([7, 5, 2, 3, 1]) ➞ [1, 3, 2, 5, 7]

odd_sort([3, 7, 0, 9, 3, 2, 4, 8]) ➞ [3, 3, 0, 7, 9, 2, 4, 8]

odd_sort([2, 2, 8, 4]) ➞ [2, 2, 8, 4]

odd_sort([7, 9, 7]) ➞ [7, 7, 9]
Notes
Lists may contain duplicate numbers.
"""

def odd_sort(lst):

	# v3
	odds = sorted([num for num in lst if num % 2])
	return [odds.pop(0) if num % 2 else num for num in lst]


	# v2
	# odd_lst = [i for i in sorted(lst) if i % 2 != 0]
	# evenidx = [j for j in range(len(lst)) if lst[j] % 2 == 0]
	#
	# for x in evenidx:
	# 	odd_lst.insert(x, lst[x])
	# return odd_lst



	# v1
	# even_dic = {}
	#
	# for key, value in enumerate(lst):
	# 	if value % 2 == 0:
	# 		even_dic[key] = value
	#
	# lst = sorted([value for key, value in enumerate(lst) if value % 2 != 0])
	#
	# for key, value in even_dic.items():
	# 	lst.insert(key, value)
	# return lst

print(odd_sort([7, 5, 2, 3, 1]))
print(odd_sort([3, 7, 0, 9, 3, 2, 4, 8]))
print(odd_sort([2, 2, 8, 4]))
print(odd_sort([7, 9, 7]))