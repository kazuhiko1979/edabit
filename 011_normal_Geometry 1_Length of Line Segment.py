"""
2点の座標位置を結ぶ線の長さを返す関数を作成してください。
番号の順序は X, Yとなります。
長さは小数点第2で四捨五入してください。

例題：

line_length([15, 7], [22, 11]) ➞ 8.06
line_length([0, 0], [0, 0]) ➞ 0
line_length([0, 0], [1, 1]) ➞ 1.41
"""

# x = 15
# x = 22

# y = 7
# y = 11

# 2か所の座標の距離
# 直角三角形の辺の長さを求める
# 長い辺（斜辺）を求める方法

# aの2乗＋bの2乗 = cの2乗

# (22-15)**2 + (11-7)**2 = c**2

# 49+16=65

import math

def line_length(dot1, dot2):

	length = math.sqrt((dot1[0] - dot2[0])**2 + (dot1[1] - dot2[1])**2)
	return round(length, 2)


	# [x1, y1] = dot1
	# [x2, y2] = dot2
	#
	# # 2分の1乗(**0.5)はルートと同じ
	# return round(((x1 - x2)**2 + (y1-y2)**2) ** 0.5, 2)

print(line_length([15, 7], [22, 11]))
print(line_length([0, 0], [1, 1]))







































# # 2か所の座標の距離
# # 直角三角形の辺の長さを求める方法
# # 長い辺（斜辺）を求める
#
# x = 15
# x = 22
#
#
# # x軸での辺の長さ（a) : 22 - 15 = 7
# # y軸での辺の長さ（b) : 11 - 7 = 4
#
# # 直角三角形の辺の長さを求める方法（斜辺）c:
#
# # aの2乗 + bの2乗 = cの2乗
#
# # 7^2 + 4^2 = c^2
# # 49 + 16 = 65^2 = 8.000
#
# def line_length(dot1, dot2):
#
# 	[x1, y1], [x2, y2] = dot1, dot2
#
# 	# 2分の1乗（**0.5）はルートと同じ
# 	return ((x1-x2)**2 + (y1-y2)**2) **0.5
#
# print(line_length([15, 7], [22, 11]))




















































# """
# Write a function that takes coordinates of two points on a two-dimensional plane and
# returns the length of the line segment connecting those two points.
#
#
# 2か所の座標の距離
#
# Examples
# line_length([15, 7], [22, 11]) ➞ 8.06
#
# line_length([0, 0], [0, 0]) ➞ 0
#
# line_length([0, 0], [1, 1]) ➞ 1.41
#
# Notes
# The order of the given numbers is X, Y.
# This challenge is easier than it looks.
# Round your result to two decimal places.
# """
# 2か所の座標の距離
# 直角三角形の辺の長さを求める
# 長い辺（斜辺）を求める方法



# c = square root of
# [(xA - xB) ^ 2 + (yA - yB) ^ 2]

# 7*7 (X)+ 4*4 (Y) = c*c(長い斜辺）
# 49 + 16 = 65(C*C) ルート65

# 65 ** 0.5


# import math
#
#
# def line_length(dot1, dot2):
#     length = math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)
#
#     return length
# #
# #     return round(math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2), 2)
# #
# #     # x = dot1[0] - dot2[0]
# #     # y = dot1[1] - dot2[1]
# #     #
# #     # return round(math.sqrt(math.pow(x, 2) + math.pow(y, 2)), 2)
# #
# #
# #     # return round(65 ** 0.5, 2)
# #
# print(line_length([15, 7], [22, 11]))

