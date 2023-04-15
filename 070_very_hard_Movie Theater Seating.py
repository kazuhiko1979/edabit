"""
Movie Theater Seating
A group of n friends are going to see a movie. They would like to find a spot where they can sit next to each other in the same row. A movie theater's seat layout can be represented as a 2-D matrix, where 0s represent empty seats and 1s represent taken seats.

[[1, 0, 0, 0, 1, 1, 1],
[1, 1, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 1, 0, 1],
[1, 1, 0, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1],
[1, 0, 1, 1, 0, 0, 0]]
Create a function that, given a seat layout and the number of friends n, returns the number of available spots for all n friends to sit together. In the above example, if n = 3, there would be 2 spots (the first row and last row).

Examples
group_seats([
  [1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 1, 0],
  [0, 0, 1, 1, 1, 1, 1],
  [1, 0, 1, 1, 0, 0, 1],
  [1, 1, 1, 0, 1, 0, 1],
  [0, 1, 1, 1, 1, 0, 0]
], 2) ➞ 3

group_seats([
  [1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 0, 0, 0, 0],
], 4) ➞ 2
Notes
Multiple free arrangements that overlap still count as distinct arrangements (see example #2).
"""
# v2

def group_seats(lst:list, n:int) -> int:

	spots = 0
	for row in lst:
		for i in range(len(row) - n+1):
			if sum(row[i:i+n]) == 0:
				spots += 1
	return spots





# v1
from itertools import groupby

# def group_seats(lst:list, n:int) -> int:
#
# 	cnt = 0
#
# 	for seats in lst:
# 		for i, j in groupby(seats):
# 			if i == 0:
# 				length = len(list(j))
# 				if length == n:
# 					cnt += 1
# 				elif length > n:
# 					cnt += length - n + 1
# 	return cnt

print(group_seats([
	[1, 0, 1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0, 1, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[1, 0, 1, 1, 0, 0, 1],
	[1, 1, 1, 0, 0, 0, 1],
	[0, 1, 1, 1, 1, 0, 0]
], 7))


print(group_seats([
	[1, 0, 0, 0, 1, 1, 1],
	[1, 1, 1, 0, 1, 1, 1],
	[1, 0, 1, 0, 1, 0, 1],
	[1, 1, 0, 1, 1, 0, 1],
	[1, 0, 1, 1, 1, 1, 1],
	[1, 0, 1, 1, 0, 0, 0]
], 3))

print(group_seats([
	[1, 0, 0, 0, 0, 1, 1],
	[1, 1, 1, 0, 1, 1, 1],
	[1, 0, 1, 0, 1, 0, 1],
	[1, 1, 0, 1, 1, 0, 1],
	[1, 0, 1, 1, 1, 1, 1],
	[1, 0, 1, 1, 0, 0, 0]
], 4))

print(group_seats([
	[1, 0, 1, 0, 0, 1, 1],
	[1, 1, 1, 0, 1, 1, 1],
	[1, 0, 1, 0, 1, 0, 1],
	[1, 1, 0, 1, 1, 0, 1],
	[1, 0, 1, 1, 1, 1, 1],
	[1, 0, 1, 1, 0, 0, 0]
], 5))




print(group_seats([
	[1, 0, 1, 0, 0, 1, 1],
	[1, 1, 1, 0, 1, 1, 1],
	[1, 0, 1, 0, 1, 0, 1],
	[1, 1, 0, 1, 0, 0, 1],
	[1, 0, 1, 1, 1, 1, 1],
	[1, 0, 1, 1, 0, 0, 0]
], 2))

print(group_seats([
	[1, 0, 1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0, 1, 0],
	[0, 0, 1, 1, 1, 1, 1],
	[1, 0, 1, 1, 0, 0, 1],
	[1, 1, 1, 0, 1, 0, 1],
	[0, 1, 1, 1, 1, 0, 0]
], 2))
#
print(group_seats([
	[1, 0, 1, 0, 1, 0, 1],
	[0, 1, 0, 0, 0, 0, 0],
], 4))

