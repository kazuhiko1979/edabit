"""
Is It a Parallelogram?
Given a list of four points in the plane, determine if they are the vertices of a parallelogram.

Examples
is_parallelogram([(0, 0), (1, 0), (1, 1), (0, 1)]) ➞ True

is_parallelogram([(0, 0), (2, 0), (1, 1), (0, 1)]) ➞ False

is_parallelogram([(0, 0), (1, 1), (1, 4), (0, 3)]) ➞ True

is_parallelogram([(0, 0), (1, 2), (2, 1), (3, 3)]) ➞ True

is_parallelogram([(0, 0), (1, 0), (0, 1), (1, 1)]) ➞ True
Notes
The points may be given in any order (compare examples #1 and #5).
"""


def is_parallelogram(points):
    if len(points) != 4:
        return False

    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    sorted_x = sorted(x_coords)
    sorted_y = sorted(y_coords)

    if sorted_x[0] != sorted_x[1] or sorted_x[2] != sorted_x[3]:
        return False

    if sorted_y[0] != sorted_y[1] or sorted_y[2] != sorted_y[3]:
        return False

    return True

import math
#
# def is_parallelogram(lst):
#
# 	#√(x₂ - x₁)² + (y₂ - y₁)²
#
# 	result = []
#
# 	result.append(math.hypot([0][0] - lst[3][0]) + (abs(lst[0][1] - lst[3][1])**2))
#
# 	# print(math.sqrt(abs(lst[0][0] - lst[3][0] ** 2)))
# 	# print(abs(lst[0][1] - lst[3][1])**2)
#
# 	# while len(lst) > 0:
# 	# 	result.append(math.sqrt(abs(lst[1][0] - lst[0][0])**2) + (abs(lst[1][1] - lst[0][1])**2))
# 	# 	lst = lst[1:]
# 	# 	if len(lst) == 1:
# 	# 		break
# 	# return result



print(is_parallelogram([(0, 0), (1, 2), (2, 1), (3, 3)]))
print(is_parallelogram([(0, 0), (1, 0), (0, 1), (1, 1)]))
#
print(is_parallelogram([(-1, -1), (1, 0), (3, 3), (1, 2)]))
