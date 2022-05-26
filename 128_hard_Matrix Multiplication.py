"""
Matrix Multiplication
The main condition of matrix multiplication is that the number of columns of the 1st matrix must equal to the number of rows of the 2nd one.
As a result of multiplication you will get a new matrix that has the same quantity of rows as the 1st one has and the same quantity of columns as the 2nd one.
For example if you multiply a matrix of "n" * "k" by "k" * "m" size you"ll get a new one of "n" * "m" dimensions.
Create a function that takes 2 x 2D lists m1 and m2 as arguments and returns a 2D list (matrix C). C = A*B.

If the number of columns of the 1st matrix isn't equal to the number of rows of the 2nd: return "ERROR".
Examples
multiply_matrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
], [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ [
  [30, 36, 42],
  [66, 81, 96],
  [102, 126, 150]
]
"""

def multiply_matrix(m1, m2):


	# v3
	# if len(m1) != len(m2[0]):
	# 	return "ERROR"
	# return [[sum(a*b for a,b in zip(x,y)) for y in zip(*m2)] for x in m1]

	# v2
	total = []
	idx, len_m1, len_m2 = 0, len(m1[0]), len(m2[0])

	if len_m1 != len(m2):
		return "ERROR"

	while idx != len(m1):
		res_arr = [0 for _ in range(len_m2)]
		for i in range(len_m1):
			for j in range(len_m2):
				res_arr[j] += m1[idx][i] * m2[i][j]
		total.append(res_arr)
		idx += 1
	return total





	#
	# My answer but not available
	# t_lst = [list(i) for i in zip(*lst[1])]
	# result, total, sub = [], [], []
	#
	# for y in range(0, len(lst) + 1):
	# 	for i in range(0, len(lst) + 1):
	# 		for x in range(0, len(lst) + 1):
	# 			sub.append(lst[0][y][x] * t_lst[i][x])
	# 			if x == len(lst):
	# 				sub = sum(sub)
	# 				total.append(sub)
	# 				sub = []
	# 		if len(total) == len(lst[0]):
	# 			result.append(total)
	# 			total = []
	# 		else:
	# 			continue
	# return result












print(multiply_matrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
], [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))

# print(multiply_matrix([[1,2,3]],[[1],[2],[3]]))

print(multiply_matrix([[8,8],[8,8]],[[7,7],[7,7]]))