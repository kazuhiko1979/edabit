"""
Identical Row and Column?
Write a function that returns True if there exists a row that is identical to a column in a 2-D matrix, otherwise False.

To illustrate:

[
  [1, 2, 3, 4],
  [2, 4, 9, 8],
  [5, 9, 7, 7],
  [6, 8, 1, 0]
]

# 2nd row + 2nd column are identical: [2, 4, 9, 8]
Examples
has_identical([
  [4, 4, 4, 4],
  [2, 4, 9, 8],
  [5, 4, 7, 7],
  [6, 4, 1, 0]
]) ➞ True

has_identical([
  [4, 4, 9, 4],
  [2, 1, 9, 8],
  [5, 4, 7, 7],
  [6, 4, 1, 0]
]) ➞ False

has_identical([
  [4, 4]
  [2, 1]
]) ➞ False

has_identical([
  [4, 2]
  [2, 1]
]) ➞ True
Notes
Non-square matrices should return False.
"""
import numpy as np
import pandas as pd

def has_identical(lst):

	for x in lst:
		if len(x) != len(lst):
			return False

	bn = [x for y in lst for x in y]
	print(bn)
	fgh = [bn[x::len(lst)] for x in range(len(lst))]
	# fgh = np.array(lst).T
	print(fgh)
	for x in fgh:
		if x in lst:
			return True
	return False



print(has_identical([
  [4, 4, 4, 4],
  [2, 4, 9, 8],
  [5, 4, 7, 7],
  [6, 4, 1, 0]
]))


