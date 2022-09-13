"""
Combined Vector Sequence
The goal is to test if a consecutive sequence is formed. A consecutive sequence is defined as sequence of incrementing numbers (e.g. 1, 2, 3 or 5, 6, 7, 8). The twist is that you have to consider the combination of vectors as shown.

[3 5 1 -5 ]  =>  [3+4  5+3  1+8  15-5]  =  [7 8 9 10]  =>  true
[4 3 8 15]
Also important is that the vectors can be of different sizes, where excess numbers in the longer one will be paired with 0s from the other one.

[2 2 2  ]  =>  [2+5  2+6  2+7  10+0]  = [ 7 8 9 10]  =>  true
[5 6 7 10]
Notes
Each array has at least two elements.
"""
# v2
# def has_consecutive_series(v1, v2):
#
# 	combined = v1 + v2
# 	for i in range(min(combined), max(combined) + 1):
# 		if i not in combined:
# 			return False
# 	return True



# v1
from itertools import zip_longest

def has_consecutive_series(v1, v2):
	z = []

	for i in list(zip_longest(v1, v2)):
		i = list(i)
		if i[0] is None:
			i[0] = 0
		if i[1] is None:
			i[1] = 0
		else:
			z.append(i[0]+i[1])

	return sorted(z) == list(range(min(z), max(z)+1))

print(has_consecutive_series([1, 2, 3], [1, 1, 1]))
print(has_consecutive_series([1, 2, 3], [1, 2, 1]))
print(has_consecutive_series([4, 6, -5, 8, 4], [-2, -3, 9, -3, 2]))
print(has_consecutive_series([12, 3], [0, 10, 14, 15, 16]))
print(has_consecutive_series([8, 6, 10], [25, 28, 25, 26, 28, 29]))
print(has_consecutive_series([11, 5, 3], [-2, 5, 8, 12]))
print(has_consecutive_series([11, 5, 3], [-2, 5, 8, 11]))



