"""
Longest Consecutive Run
A consecutive-run is a list of adjacent, consecutive integers. This list can be either increasing or decreasing. Create a function that takes a list of numbers and returns the length of the longest consecutive-run.

To illustrate:

longestRun([1, 2, 3, 5, 6, 7, 8, 9]) ➞ 5
# Two consecutive runs: [1, 2, 3] and [5, 6, 7, 8, 9] (longest).
Examples
longest_run([1, 2, 3, 10, 11, 15]) ➞ 3
# Longest consecutive-run: [1, 2, 3].

longest_run([5, 4, 2, 1]) ➞ 2
# Longest consecutive-run: [5, 4] and [2, 1].

longest_run([3, 5, 7, 10, 15]) ➞ 1
# No consecutive runs, so we return 1.
Notes
If there aren't any consecutive runs (there is a gap between each integer), return 1.
"""



def longest_run(lst):

	flag = ""
	length = 1
	max_length = len(lst)
	result = []

	for i in range(0, len(lst)):
		if i == 0:
			diff = lst[i + 1] - lst[i]
			if diff == 1:
				flag = '+'
				length += 1
				continue
			if diff == -1:
				flag = '-'
				length += 1
				continue
			else:
				if diff > 0:
					flag = '+'
					continue
				else:
					flag = '-'
					continue
		else:
			if i != max_length - 1:
				diff = lst[i + 1] - lst[i]
				if diff == 1:
					if flag == '+':
						length += 1
						continue

				if diff == -1:
					if flag == '-':
						length += 1
						continue
				else:
					result.append(length)
					length = 1
					continue

		result.append(length)
		return max(result)


# def longest_run(lst):

	# total = []
	# sub_plus = []
	# sub_minus = []
	# flag = True
	#
	# try:
	# 	for i in range(0, len(lst)):
	# 		up = abs(lst[i])
	# 		bottom = abs(lst[i+1])
	#
	# 		if lst[i] - lst[i+1] == - 1:
	# 			if flag:
	# 				sub_plus.append(lst[i])
	# 				# 最後尾チェック
	# 				if i == len(lst) - 2:
	# 					sub_plus.append(lst[i+1])
	# 				else:
	# 					continue
	#
	# 		if lst[i] - lst[i + 1] == 1:
	# 			flag = False
	# 			if flag:
	# 				sub_plus.append(lst[i])
	# 				flag = False
	# 				continue
	# 			else:
	# 				sub_minus.append(lst[i])
	# 			# 最後尾チェック
	# 			if i == len(lst) - 2:
	# 				sub_minus.append(lst[i+1])
	# 			else:
	# 				continue
	# 		else:
	# 			if sub_plus:
	# 				if i < len(lst) - 2:
	# 					sub_plus.append(lst[i])
	# 				if i == len(lst) - 2:
	# 					if lst[i-1] - lst[i] == -1:
	# 						sub_plus.append(lst[i])
	#
	# 				sub_plus = list(set(sub_plus))
	# 				total.append(sub_plus)
	# 				sub_plus = []
	#
	# 			elif sub_minus:
	# 				if i < len(lst) - 2:
	# 					sub_minus.append(lst[i])
	# 				if i == len(lst) - 2:
	# 					if lst[i-1] - lst[i] == 1:
	# 						sub_minus.append(lst[i])
	#
	# 				sub_minus = set(sub_minus)
	# 				total.append(sub_minus)
	# 				sub_minus = []
	#
	# except IndexError:
	# 	pass
	#
	# if sub_plus:
	# 	total.append(sub_plus)
	# if sub_minus:
	# 	total.append(sub_minus)
	#
	# # return total
	# return len(max(total, key=len)) if total else 1

print(longest_run([1, 2, 3, 5, 6, 7, 8, 9]))
print(longest_run([1, 2, 3, 10, 11, 15]))
print(longest_run([-7, -6, -5, -4, -3, -2, -1]))
print(longest_run([3, 5, 6, 10, 15]))
print(longest_run([3, 5, 7, 10, 15]))
print(longest_run([5, 4, 3, 2, 1]))
print(longest_run([5, 4, 2, 1]))
print(longest_run([10, 9, 0, 5]))
print(longest_run([1, 2, 3, 2, 1]))
print(longest_run([10, 9, 8, 7, 6, 2, 1]))