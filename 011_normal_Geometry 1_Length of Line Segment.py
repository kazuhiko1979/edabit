"""
Write a function that takes coordinates of two points on a two-dimensional plane and
returns the length of the line segment connecting those two points.

三角形の平方根の定理
2か所の座標の距離

Examples
line_length([15, 7], [22, 11]) ➞ 8.06

line_length([0, 0], [0, 0]) ➞ 0

line_length([0, 0], [1, 1]) ➞ 1.41
Notes
The order of the given numbers is X, Y.
This challenge is easier than it looks.
Round your result to two decimal places.
"""
# 三角形の平方根の定理
# 2か所の座標の距離

# c = square root of
# [(xA - xB) ^ 2 + (yA - yB) ^ 2]

import math


def line_length(dot1, dot2):

    x = dot1[0] - dot2[0]
    y = dot1[1] - dot2[1]

    return round(math.sqrt(math.pow(x, 2) + math.pow(y, 2)), 2)


print(line_length([15, 7], [22, 11]))

