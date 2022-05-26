"""
Compass Directions
You face 1 out of the 4 compass directions: N, S, E or W.

A left turn is a counter-clockwise turn. e.g. N (left-turn) ➞ W.
A right turn is a clockwise turn. e.g. N (right-turn) ➞ E.
Create a function that takes in a starting direction and a sequence of left and right turns, and outputs the final direction faced.

Examples
final_direction("N", ["L", "L", "L"]) ➞ "E"

final_direction("N", ["R", "R", "R", "L"]) ➞ "S"

final_direction("N", ["R", "R", "R", "R"]) ➞ "N"

final_direction("N", ["R", "L"]) ➞ "N"
Notes
You can only face 1 out of the 4 compass directions: N, S, E or W.
"""

import itertools


def final_direction(initial, turns):

	# v3
	compass = {"N": 0,
			   "E": 90,
			   "S": 180,
			   "W": 270,
			   "R": 90,
			   "L": -90,
			   0: "N",
			   90: "E",
			   180: "S",
			   270: "W"}

	direction = compass[initial]
	# print(direction)
	for turn in turns:
		direction += compass[turn]
	direction = direction % 360
	return compass[direction]

	# v2
	# d = ["N", "E", "S", "W"]
	# return d[d.index(initial) + sum([1 if i == "R" else -1 for i in turns]) % 4]


	# v1
	# a_list = ["N", "E", "S", "W"]
	#
	# initial_index = a_list.index(initial)
	#
	# count = 0
	#
	# for i in turns:
	# 	if i == "L":
	# 		count -= 1
	# 	if i == "R":
	# 		count += 1
	#
	# if count < 0:
	# 	for i in itertools.count(initial_index, -1):
	# 		count += 1
	# 		initial_index -= 1
	# 		if count == 0:
	# 			return a_list[initial_index]
	# 			break
	# if count == 0 or count == 4:
	# 	return a_list[a_list.index(initial)]
	# if 1 <= count < 4:
	# 	for i in itertools.count(initial_index, 1):
	# 		count -= 1
	# 		initial_index += 1
	# 		if count == 0:
	# 			if initial_index >= 4:
	# 				initial_index = initial_index - 4
	# 				return a_list[initial_index]
	# 			else:
	# 				return a_list[initial_index]
	# 			break
	# if count > 4:
	# 	count = count - 4
	# 	for i in itertools.count(initial_index, 1):
	# 		count -= 1
	# 		initial_index += 1
	# 		if count == 0:
	# 			return a_list[initial_index]
	# 			break

print(final_direction("N", ["L", "L", "L"]))
print(final_direction('N', ['R', 'R', 'R', 'R', 'R', 'R', 'R']))
print(final_direction("N", ["R", "R", "R", "L"]))
print(final_direction("N", ["R", "R", "R", "R"]))
# print(final_direction("N", ["R", "L"]))
#
# print(final_direction('S', ['R', 'L', 'R', 'L', 'R']))
# print(final_direction('S', ['R', 'L', 'R', 'L', 'R', 'L']))
# print(final_direction('S', ['R', 'L', 'R', 'L', 'L', 'L']))
# print(final_direction('S', ['R', 'R']))
# print(final_direction('S', ['R']))
# print(final_direction('S', ['L']))
#
# print(final_direction('W', ['L', 'R', 'R']))
# print(final_direction('W', ['R', 'L', 'L']))
# print(final_direction('E', ['L', 'R', 'R']))
# print(final_direction('E', ['R', 'L', 'L']))


