"""
Matrix Padder
Create a function that takes a matrix of size (m, n) and returns a matrix of size (m+2, n+2) with a pad of 0s around the perimeter.

Examples
pad_matrix([[]]) ➞ [[0, 0], [0, 0], [0, 0]]

pad_matrix([[9]]) ➞ [
  [0, 0, 0],
  [0, 9, 0],
  [0, 0, 0]
]

pad_matrix([["hi", True]]) ➞ [
  [0, 0, 0, 0],
  [0, "hi", True, 0],
  [0, 0, 0, 0]
]

pad_matrix([
  [1, 2, 5],
  [8, 6, 7],
  [3, 4, 9]
]) ➞ [
  [0, 0, 0, 0, 0],
  [0, 1, 2, 5, 0],
  [0, 8, 6, 7, 0],
  [0, 3, 4, 9, 0],
  [0, 0, 0, 0, 0]
]
Notes
All inputs will be lists of lists.
Refer to the first example to handle an empty input.
"""
# v3
def pad_matrix(matrix):
	
	j = len(matrix[0])
	new_lst = [[0] + i + [0] for i in matrix]
	return [[0]*(j+2)] + new_lst + [[0]*(j+2)]


# v2
# def pad_matrix(matrix):
# 	a = [[0] * (len(matrix[0]) + 2)]
# 	for m in matrix:
# 		a.append([0] + m + [0])
# 	a.append([0] * (len(matrix[0]) + 2))
# 	return a


# v1
# def pad_matrix(lst):
#
# 	result = []
#
# 	for i in range(len(lst)):
# 		if lst[i] == []:
# 			result.append([0 for _ in range(len(lst) + 1)])
# 			result.append([0 for _ in range(len(lst) + 1)])
# 			result.append([0 for _ in range(len(lst) + 1)])
# 			return result
#
# 	for j in lst:
# 		lid = [0 for _ in range(len(j) + 2)]
# 		result.append(lid)
# 		for i in lst:
# 			i.insert(0, 0)
# 			i.append(0)
# 			result.append(i)
# 		break
# 	result.append(lid)
#
# 	return result

print(pad_matrix([[]]))
print(pad_matrix([['hi'],['downstairs']]))
print(pad_matrix([["hi", True]]))
print(pad_matrix([[1, 2, 5],[8, 6, 7],[3, 4, 9]]))
print(pad_matrix([[1,'beep',True],['oink',99,1.1],[[1,1],'e',99]]))

