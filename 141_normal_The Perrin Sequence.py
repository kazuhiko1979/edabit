"""
The Perrin Sequence
Each number in the Perrin sequence is created by summing the numbers two positions and three positions before it. The first three numbers are (3, 0, 2), and the sequence is extended as follows:

P(0) P(1) P(2) P(3) P(4) P(5) P(6) P(7) ... P(n)
3, 0, 2, 3, 2, 5, 5, 7, ...
Given a value for n, return the Perrin number P(n).

Examples
perrin(1) ➞ 0

perrin(8) ➞ 10

perrin(26) ➞ 1497
"""

def perrin(n):

	# v3
	# start = [3, 0, 2]
	# if n < 3:
	# 	return start[n]
	# return perrin(n-2) + perrin(n-3)

	# v2 not use recursion
	start = [3, 0, 2]
	for i in range(n-2):
		start.append(start[-2] + start[-3])
	return start[-1]



# v1
# def perrin(n):
# 	lst = [3, 0, 2]
# 	if n < 2:
# 		return lst[n]
# 	return perrin_help(lst, n)
#
# def perrin_help(lst, n):
#
# 	if n == 2:
# 		return lst[-1]
# 	lst.append(sum(lst[:2]))
# 	lst.pop(0)
# 	return perrin_help(lst, n-1)

print(perrin(8))
print(perrin(26))
print(perrin(38))