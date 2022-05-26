"""
List with Zero Sum
Given an integer n, return any list containing n unique integers such that they add up to 0.

Examples
list_with_zero_sum(5) ➞ [-7, -1, 1, 3, 4] or [-5, -1, 1, 2, 3] or [-3, -1, 2, -2, 4]

list_with_zero_sum(3) ➞ [-1, 0, 1]

list_with_zero_sum(1) ➞ [0]
"""

from random import randint

def list_with_zero_sum(n):

	# v3
	result = []
	for i in range(n // 2):
		result.extend((i + 1, -i - 1))
	if n % 2:
		return result + [0]
	else:
		return result

	# v2
	# if n == 1:
	# 	return [0]
	# answer = list(range(1, n))
	# answer.append(-sum(answer))
	# return answer


	# v1
	# result = [randint(-10, 10) for _ in range(n)]
	#
	# while sum(result) != 0:
	# 	result = [randint(-10, 10) for _ in range(n)]
	# return result

print(list_with_zero_sum(5))
print(list_with_zero_sum(3))
print(list_with_zero_sum(2))
print(list_with_zero_sum(1))





