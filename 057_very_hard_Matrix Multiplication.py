"""
Matrix Multiplication
Create a function that multiplies two matricies (n x n each).

Examples
matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]

matrix_mult([[3, 6],[4, 5]], [[8, 1], [7, 2]]) ➞ [[66, 15], [67, 14]]

matrix_mult([[7, 5],[2, 2]], [[6, 7], [3, 2]]) ➞ [[57, 59], [18, 18]]
Notes
Limit yourself to 2 x 2 matricies.
"""

import numpy as np

def matrix_mult(m1, m2):

	return np.dot(m1, m2).tolist()




# import itertools

# import numpy as np
# def matrix_mult(m1, m2):
#
# 	m2 = np.array(m2).T
# 	result = []
# 	sub = []
#
# 	for i in range(2):
# 		for j in range(2):
# 			if (i == 0 and j == 1) or (i == 1 and j == 1):
# 				sub.append(sum(np.multiply(m1[i], m2[j])))
# 				result.append(sub)
# 				sub = []
# 			else:
# 				sub.append(sum(np.multiply(m1[i], m2[j])))
#
# 	return result



print(matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]]))
print(matrix_mult([[3, 6],[4, 5]], [[8, 1], [7, 2]]))
print(matrix_mult([[7, 5],[2, 2]], [[6, 7], [3, 2]]))