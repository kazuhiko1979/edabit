"""
Incrementing Rows and Columns
Write a function that takes in three parameters: r, c, i, where:

r and c are the number of rows and columns to initialize a zero matrix.
i represents the list of incrementing operations (+1).
And returns the resulting matrix after applying all the increment operations. Each increment operation will add 1 to the rows or columns specified in the incrementing list.

To illustrate:

final(3, 3, ["2r", "2c", "1r", "0c"])

# Initialize a 3 x 3 matrix of zeroes.

[
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

# Apply "2r" (increment index 2 row).

[
  [0, 0, 0],
  [0, 0, 0],
  [1, 1, 1]
]

# Apply "2c" (increment index 2 column).

[
  [0, 0, 1],
  [0, 0, 1],
  [1, 1, 2]
]

# Apply "1r" (increment index 1 row).

[
  [0, 0, 1],
  [1, 1, 2],
  [1, 1, 2]
]

# Apply "0c" (increment index 0 column).
# This is the result you should return.

[
  [1, 0, 1],
  [2, 1, 2],
  [2, 1, 2]
]
Examples
final(2, 2, ["0r", "0r", "0r", "1c"]) ➞ [
  [3, 4],
  [0, 1]
]

final(2, 2, ["0c"]) ➞ [
  [1, 0],
  [1, 0]
]

final(3, 3, ["1c", "2c", "2c", "3c", "3c", "3c"]) ➞ [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

final(3, 3, []) ➞ [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]
Notes
The 2D matrix is 0-indexed.
The matrix created will have at least one row and one column.
All increment operations will be exactly +1.
"""
import numpy as np

def final(r, c, i):

	# v2
	# arr = np.zeros((r, c))
	# for idx, d in i:
	# 	if d == "r":
	# 		arr[int(idx)] += 1
	# 	else:
	# 		arr[:, int(idx)] += 1
	#
	# return arr.tolist()

	# v2
	res = [[0 for i in range(c)] for i in range(r)]

	for n, l in i:
		if i == 'r':
			for j in range(c):
				res[int(n)[j]] += 1
		else:
			for j in range(r):
				res[j][int(n)] += 1

	return res



	# v1
	# lst = []
	#
	# for j in range(0, r):
	# 	lst.append([0] * c)
	#
	# for rc in i:
	# 	try:
	# 		if rc[1] == "r":
	# 			lst[int(rc[0])] = [p+1 for p in lst[int(rc[0])]]
	# 		if rc[1] == "c":
	# 			for k in range(0, r):
	# 				lst[k][int(rc[0])] += 1
	# 	except IndexError:
	# 		pass
	# return lst



print(final(3, 3, ["2r", "2c", "1r", "0c"]))
print(final(2, 2, ["0r", "0r", "0r", "1c"]))
print(final(2, 2, ["0c"]))
print(final(3, 3, ['0c', '1c', '1c', '2c', '2c', '2c']))
print(final(3, 3, ['0r', '2c', '1r', '2c', '1c', '1r', '1r']))
print(final(3, 3, []))
print(final(3, 4, ['1r', '1r', '1r', '3c', '3c', '3c']))
