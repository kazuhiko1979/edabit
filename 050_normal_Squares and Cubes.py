"""
Create a function that takes a list of two numbers and checks if the square root of the first number is equal to the cube root of the second number.

Examples
check_square_and_cube([4, 8]) ➞ True

check_square_and_cube([16, 48]) ➞ False

check_square_and_cube([9, 27]) ➞ True
Notes
Remember to return either True or False.
All lists contain two positive numbers.
"""

import sympy
import math
#

# # print(math.sqrt(4) == sympy.cbrt(8))
#
# print((a / 2) == (b / 2 / 2))

def check_square_and_cube(lst):

    square_root = lst[0]**(1/2)
    cube_root = lst[1]**(1/3)

    # cube_root = sympy.cbrt(lst[1])
    # print(square_root)
    # print(round(cube_root, 2))

    return square_root == cube_root

print(check_square_and_cube([4, 8]))
print(check_square_and_cube([5, 12]))
print(check_square_and_cube([9, 27]))
print(check_square_and_cube([25, 120]))
print(check_square_and_cube([25, 125]))
print(check_square_and_cube([36, 215]))







