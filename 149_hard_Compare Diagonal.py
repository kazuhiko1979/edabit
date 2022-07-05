"""
Compare Diagonal
Create a function that returns the right diagonal of a matrix if the sum of the right diagonal is greater than or equal to the sum of the left diagonal, else returns the left diagonal.

Examples
compare_diagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) ➞ [3, 5, 7]
Notes
The matrix will be a square matrix of any order.
"""


def compare_diagonal(matrix):

	# v3
	return max([[l[len(matrix)-1-i] for i,l in enumerate(matrix)],  [l[i] for i, l in enumerate(matrix)]], key = sum)


	# v2
	# right = [matrix[i][len(matrix)-i-1] for i in range(len(matrix))]
	# left = [matrix[i][i] for i in range(len(matrix))]
	# return right if sum(right) >= sum(left) else left


	# v1
	# right_index = [i for i in range(0, len(matrix[0]))]
	# left_index = list(reversed(right_index))
	#
	# right_sum = [matrix[r][l] for r, l in zip(right_index, left_index)]
	# left_sum = list(reversed([matrix[l][l] for r, l in zip(right_index, left_index)]))
	#
	# return right_sum if sum(right_sum) >= sum(left_sum) else left_sum


print(compare_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
