"""
Write a function that takes the coordinates of three points in the form of a 2d array and returns the perimeter of the triangle. The given points are the vertices of a triangle on a two-dimensional plane.

Examples
perimeter( [ [15, 7], [5, 22], [11, 1] ] ) ➞ 47.08

perimeter( [ [0, 0], [0, 1], [1, 0] ] ) ➞ 3.42

perimeter( [ [-10, -10], [10, 10 ], [-10, 10] ] ) ➞ 68.28
Notes
The given points always create a triangle.
The numbers in the argument array can be positive or negative.
Output should have 2 decimal places

"""
import math

# # x = [11, 1]
# # z = [15, 7]
# # y = [5, 22]
# #
# # xz = ((15-11) ** 2) + (7-1) **2
# # xz = math.sqrt(xz)
# #
# # yz = ((15-5) ** 2) + (22-7) **2
# # yz = math.sqrt(yz)
# #
# # yx = ((11-5) ** 2) + (22-1) **2
# # yx = math.sqrt(yx)
# #
# # total = xz + yz + yx
# # print(round(total, 2))
#
#
# # p = [[15, 7], [5, 22], [11, 1]]
# # p = [[0, 0], [0, 1], [1, 0]]
# p= [ [-10, -10], [10, 10 ], [-10, 10] ]

def perimeter(lst):

    xz = abs(math.sqrt(((lst[0][0] - lst[2][0])**2) + ((lst[0][1]- lst[2][1]))**2))
    yz = abs(math.sqrt(((lst[0][0] - lst[1][0])**2) + ((lst[1][1]- lst[0][1]))**2))
    yx = abs(math.sqrt(((lst[2][0] - lst[1][0])**2) + ((lst[1][1]- lst[2][1]))**2))

    return round(xz + yz + yx, 2)

print(perimeter([[0, 0], [1, 0], [0, 1]]))
print(perimeter([[15, 7], [5, 22], [11, 1]]))
print(perimeter([[7, 6], [0, 11], [0, -3]]))
print(perimeter([[-10, -10], [10, 10], [-10, 10]]))






